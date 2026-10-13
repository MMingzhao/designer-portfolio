(() => {
  'use strict';
  const content = window.PORTFOLIO;
  if (!content) return;
  const $ = (selector, root = document) => root.querySelector(selector);
  const escapeHTML = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  const allowedURL = value => /^(https?:|mailto:|\.\/|assets\/)/.test(value) ? value : '';
  const pad = number => String(number).padStart(2, '0');
  let activeFilter = 'all';
  let lastTrigger = null;
  let activeProject = null;
  const grid = $('#project-grid');
  const dialog = $('#project-dialog');
  const filters = $('#filters');
  document.querySelectorAll('[data-profile]').forEach(element => {
    const value = content.profile[element.dataset.profile];
    if (typeof value === 'string') element.textContent = value;
  });
  $('#total-count').textContent = pad(content.projects.length);
  filters.innerHTML = content.categories.map(category => `<button class="filter-button" type="button" data-filter="${escapeHTML(category.id)}" aria-pressed="${category.id === 'all'}">${escapeHTML(category.label)}</button>`).join('');
  function renderProjects(category = 'all', announce = false) {
    activeFilter = content.categories.some(item => item.id === category) ? category : 'all';
    const projects = content.projects.filter(project => activeFilter === 'all' || project.category === activeFilter);
    filters.querySelectorAll('button').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === activeFilter)));
    grid.innerHTML = projects.map((project, index) => `<button class="project-card" type="button" data-project="${escapeHTML(project.id)}" style="--project-bg:${escapeHTML(project.background)};--project-accent:${escapeHTML(project.color)};animation-delay:${Math.min(index * 35, 140)}ms" aria-label="查看 ${escapeHTML(project.title)}，${escapeHTML(project.discipline)} 项目详情"><div class="project-image"><img src="${escapeHTML(allowedURL(project.image))}" width="1200" height="960" alt="${escapeHTML(project.imageAlt)}" loading="lazy" decoding="async"><span class="project-index">${escapeHTML(project.number)} / ${escapeHTML(project.english.toUpperCase())}</span><span class="project-open" aria-hidden="true">↗</span></div><div class="project-meta"><div><h3>${escapeHTML(project.title)}</h3><p class="project-subtitle">${escapeHTML(project.subtitle)}</p></div><div class="project-discipline">${escapeHTML(project.discipline)}<span>${escapeHTML(project.english.toUpperCase())}</span></div></div></button>`).join('');
    $('#results-count').textContent = `${pad(projects.length)} PROJECT${projects.length === 1 ? '' : 'S'}`;
    if (announce) $('#filter-status').textContent = `${content.categories.find(item => item.id === activeFilter).label}：${projects.length} 个项目`;
  }
  filters.addEventListener('click', event => {
    const button = event.target.closest('[data-filter]');
    if (button) renderProjects(button.dataset.filter, true);
  });
  document.querySelectorAll('[data-filter-link]').forEach(link => link.addEventListener('click', () => renderProjects(link.dataset.filterLink, true)));
  function renderDialog(project) {
    activeProject = project;
    const index = content.projects.indexOf(project);
    const next = content.projects[(index + 1) % content.projects.length];
    dialog.style.setProperty('--project-accent', project.color);
    $('#dialog-index').textContent = `${project.number} / ${pad(content.projects.length)} — ${project.english.toUpperCase()}`;
    $('#dialog-content').innerHTML = `<header class="dialog-header"><p class="eyebrow">${escapeHTML(project.discipline)} / ${escapeHTML(project.english.toUpperCase())}</p><h2 id="dialog-title">${escapeHTML(project.title)}</h2><p class="dialog-subtitle">${escapeHTML(project.subtitle)}</p></header><div class="dialog-hero"><img src="${escapeHTML(allowedURL(project.image))}" width="1200" height="960" alt="${escapeHTML(project.imageAlt)}"></div><div class="dialog-body"><aside><div><p class="dialog-label">DESIGN SCOPE / 设计内容</p><ul class="scope-list">${project.scope.map(item => `<li>${escapeHTML(item)}</li>`).join('')}</ul></div><div><p class="dialog-label">COLOR SYSTEM / 色彩</p><div class="palette" aria-label="项目色彩：${escapeHTML(project.palette.join('、'))}">${project.palette.map(color => `<span style="background:${escapeHTML(color)}" title="${escapeHTML(color)}"></span>`).join('')}</div><p class="palette-labels">${project.palette.map(escapeHTML).join(' · ')}</p></div></aside><div><p class="dialog-label">THE IDEA / 设计思路</p><p class="dialog-summary">${escapeHTML(project.summary)}</p><p class="dialog-approach">${escapeHTML(project.approach)}</p></div></div><div class="design-notes">${project.details.map((detail, i) => `<p><span>DESIGN NOTE / ${pad(i + 1)}</span>${escapeHTML(detail)}</p>`).join('')}</div><button class="dialog-next" type="button" data-next-project="${escapeHTML(next.id)}"><span><small>NEXT PROJECT / 下一个作品</small><strong>${escapeHTML(next.title)}</strong></span><span aria-hidden="true">↗</span></button>`;
    dialog.scrollTop = 0;
  }
  function openProject(id, trigger, updateURL = true) {
    const project = content.projects.find(item => item.id === id);
    if (!project) return;
    if (trigger) lastTrigger = trigger;
    renderDialog(project);
    if (!dialog.open) {
      dialog.showModal();
      document.body.classList.add('modal-open');
    }
    $('.dialog-close').focus({preventScroll: true});
    if (updateURL) history.pushState({project: id}, '', `#project/${encodeURIComponent(id)}`);
  }
  function closeProject(updateURL = true) {
    if (!dialog.open) return;
    dialog.close();
    document.body.classList.remove('modal-open');
    activeProject = null;
    if (updateURL && location.hash.startsWith('#project/')) history.replaceState(null, '', '#work');
    const fallback = grid.querySelector(`[data-project="${lastTrigger?.dataset.project || ''}"]`);
    const trigger = lastTrigger?.isConnected ? lastTrigger : fallback;
    if (trigger) trigger.focus({preventScroll: true});
  }
  grid.addEventListener('click', event => {
    const trigger = event.target.closest('[data-project]');
    if (trigger) openProject(trigger.dataset.project, trigger);
  });
  $('.dialog-close').addEventListener('click', () => closeProject());
  dialog.addEventListener('cancel', event => { event.preventDefault(); closeProject(); });
  dialog.addEventListener('click', event => {
    const next = event.target.closest('[data-next-project]');
    if (next) {
      const project = content.projects.find(item => item.id === next.dataset.nextProject);
      renderDialog(project);
      $('.dialog-close').focus({preventScroll: true});
      history.replaceState({project: project.id}, '', `#project/${encodeURIComponent(project.id)}`);
      return;
    }
    if (event.target === dialog) {
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) closeProject();
    }
  });
  function syncHash() {
    if (location.hash.startsWith('#project/')) {
      let id;
      try { id = decodeURIComponent(location.hash.slice(9)); } catch { return; }
      openProject(id, null, false);
    } else if (dialog.open) closeProject(false);
  }
  window.addEventListener('hashchange', syncHash);
  const menu = $('.menu-toggle');
  const mobileNav = $('#mobile-nav');
  function closeMenu() { menu.setAttribute('aria-expanded', 'false'); menu.setAttribute('aria-label', '打开导航'); mobileNav.hidden = true; }
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open)); menu.setAttribute('aria-label', open ? '关闭导航' : '打开导航'); mobileNav.hidden = !open;
  });
  mobileNav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); } });
  document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });
  window.matchMedia('(min-width: 601px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
  const profileLinks = $('#profile-links');
  const links = [];
  if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(content.profile.email)) links.push({label: '联系邮箱 ↗', url: `mailto:${content.profile.email}`});
  if (allowedURL(content.profile.resumeUrl)) links.push({label: '查看简历 ↗', url: content.profile.resumeUrl});
  (content.profile.socialLinks || []).filter(link => allowedURL(link.url)).forEach(link => links.push(link));
  if (links.length) { profileLinks.hidden = false; profileLinks.innerHTML = links.map(link => `<a href="${escapeHTML(link.url)}">${escapeHTML(link.label)}</a>`).join(''); }
  document.querySelectorAll('.archive-image').forEach(image => {
    image.addEventListener('error', () => { image.classList.add('is-failed'); image.alt = ''; });
    if (image.complete && !image.naturalWidth) image.classList.add('is-failed');
  });
  $('#experience-list').innerHTML = (content.experience || []).map(item => `<article class="experience-item"><p class="experience-period">${escapeHTML(item.period)}</p><h4>${escapeHTML(item.role)}</h4><p class="experience-company">${escapeHTML(item.company)}</p><p class="experience-description">${escapeHTML(item.description)}</p></article>`).join('');
  $('#awards-list').innerHTML = (content.awards || []).map(item => `<article class="award-item"><span class="award-year">${escapeHTML(item.year)}</span><div><h4>${escapeHTML(item.name)}</h4><p>${escapeHTML(item.detail)}</p><small>${escapeHTML(item.project)}</small></div><span class="award-star" aria-hidden="true">✳</span></article>`).join('');
  $('#client-list').innerHTML = (content.clients || []).map(item => `<div class="client-wordmark ${escapeHTML(item.style)}"><strong>${escapeHTML(item.name)}</strong><span>${escapeHTML(item.english)}</span></div>`).join('');
  renderProjects();
  syncHash();
})();
