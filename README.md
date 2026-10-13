# Visual Designer / 视觉设计作品集

一个无需构建、无运行时依赖的中英双语视觉设计作品集。适配桌面和移动端，可直接发布到 GitHub Pages。

## 内容维护

所有项目、个人介绍、履历、客户和奖项集中在 `content.js`：

- `profile`：称呼、首页文案、个人介绍、邮箱、简历链接、社交链接。
- `projects`：作品名称、分类、说明、封面、配色和项目细节。
- `experience`：工作经历时间线。
- `awards`：奖项与认可。
- `clients`：合作品牌字标。
- `categories`：作品筛选分类。

图片放在 `assets/`，修改对应项目的 `image` 和 `imageAlt` 即可。推荐封面宽高比为 5:4。联系方式与简历链接只有填写后才会显示，不使用虚假邮箱或无效下载按钮。

### 内容真实性说明

应项目委托要求，本版本包含**虚构的工作经历、工作室、客户与奖项**，用于呈现完整页面，待站点所有者以真实资料替换。它们不是经核实的个人资历或客户背书。没有使用真实知名企业、机构或奖项名称来制造背书。

八个项目及其 SVG 视觉由本次网站制作原创构建，不代表站点所有者真实完成的委托案例。上线用于真实求职、商业提案或个人资历展示前，请把虚构内容和项目替换为本人真实可用资料。页面按委托要求不显示占位说明；这里保留完整审计与替换说明。

未填写真实姓名、邮箱、学校、学历、社会账号或电话号码。当前身份使用中性 `VISUAL DESIGNER / 视觉设计师`。

## 文件结构

- `index.html`：页面语义结构。
- `styles.css`：响应式视觉、交互状态、减少动态效果支持。
- `content.js`：可编辑内容数据。
- `app.js`：项目分类、项目弹窗、历史记录、移动导航。
- `assets/`：本地 SVG/JPG 素材与来源审计。
- `scripts/generate_artwork.py`：原创 SVG 作品的生成源文件。
- `scripts/test-site.cjs`：可选浏览器检查脚本；生产网站不依赖 Node.js。

## 本地预览

在目录中运行：

```sh
python3 -m http.server 8765
```

打开 `http://localhost:8765`。直接双击 `index.html` 也可浏览静态内容与交互。

## GitHub Pages

Repository → Settings → Pages → Deploy from a branch → `main` / `(root)`。

所有生产资源使用相对路径，兼容 `https://<username>.github.io/designer-portfolio/` 这样的项目子路径。`.nojekyll` 关闭不必要的 Jekyll 处理。不需要构建命令、环境变量、API 密钥或第三方 CDN。

## 交互与无障碍

- 6 个设计类别与全部作品筛选，包含屏幕阅读器结果播报。
- 原生 `dialog` 项目详情，支持键盘、Escape、遮罩关闭和焦点恢复。
- `#project/mimo` 等锚点深链接，可使用浏览器前进/后退。
- 移动导航支持菜单关闭、Escape 与页面跳转。
- 全部作品图像有文字说明；装饰元素不重复播报。
- 遵循 `prefers-reduced-motion`，减少动态效果时停止滚动横幅和旋转图形。
- 不设置跟踪器、Cookie、分析服务、外部字体或广告。

## 公开艺术素材来源与许可

生产页面仅使用下面两幅历史作品作为“视觉札记”和编辑性配图。它们不是本作品集设计师的原创项目，不代表与博物馆的合作或背书。所有图像本地保存，没有运行时热链。

1. `assets/visual-notes-wendingen.jpg`
   - El Lissitzky, *Wendingen*, 1921（1923 年出版）
   - 馆藏页：https://www.nga.gov/artworks/93943-wendingen
   - 图像：https://api.nga.gov/iiif/f5b758cb-7d21-4327-bc2f-f869b7317731/full/full/0/default.jpg
   - 使用：关于区域的编辑性图形配图。
2. `assets/visual-notes-nightingales.jpg`
   - Paul Klee, *Persische Nachtigallen (Persian Nightingales)*, 1917
   - 馆藏页：https://www.nga.gov/artworks/71551-persische-nachtigallen-persian-nightingales
   - 图像：https://api.nga.gov/iiif/e3c67705-58e9-494e-a57e-d1ad8640abb1/full/full/0/default.jpg
   - 使用：履历区域的编辑性艺术配图。

许可核验日期：2026-10-13。美国国家美术馆对应馆藏页面明确将这些媒体标记为可免费使用的公有领域资源。机构 Open Access 政策以 CC0 1.0 释出这些图像，可用于商业及非商业用途；署名为建议的礼貌性署名，不是许可要求。

- 机构政策：https://www.nga.gov/terms-and-notices
- CC0：https://creativecommons.org/publicdomain/zero/1.0/
- 完整机器可读来源：`assets/SOURCES.json`

本仓库未为站点代码和原创 SVG 另行声明开源授权；公开仓库本身不等于开放许可。上述 CC0 图像保持其原有许可。
