from pathlib import Path
from math import sin, cos, pi
A=Path(__file__).resolve().parents[1]/'assets'
def svg(name, bg, body, w=1200,h=960):
    (A/(name+'.svg')).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>''')
def text(x,y,s,size=30,fill='#171714',weight='400',extra=''):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" {extra}>{s}</text>'
def star(cx,cy,r=100,n=12,fill='#f74426'):
    points=' '.join(f'{cx+(r if i%2==0 else r*.5)*cos(i*pi/n):.2f},{cy+(r if i%2==0 else r*.5)*sin(i*pi/n):.2f}' for i in range(n*2))
    return f'<polygon points="{points}" fill="{fill}"/>'
# Main identity: a tactile multi-piece stationery system.
b='''<defs><filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-opacity=".18"/></filter><pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#c8c2b3" stroke-width=".6"/></pattern></defs><rect width="1200" height="960" fill="url(#grid)" opacity=".4"/><g transform="rotate(-9 370 470)" filter="url(#shadow)"><rect x="110" y="110" width="530" height="720" fill="#fa492b"/>'''
b+=text(152,165,'OFF / GRID',25,'#201e1a','700')+text(145,398,'OFF',190,'#f6f2e8','900', 'letter-spacing="-14"')+text(145,574,'GRID',176,'#f6f2e8','900','letter-spacing="-14"')
b+='<path d="M155 696h429" stroke="#211f1b" stroke-width="2"/>'+text(155,741,'GROW BEYOND THE FRAME.',19,'#211f1b','700')+'</g>'
b+='''<g transform="rotate(12 830 500)" filter="url(#shadow)"><rect x="633" y="234" width="408" height="526" fill="#1d1e19"/>'''+star(837,466,158,10,'#d9e740')+text(671,704,'FREE TO FORM.',30,'#f4f0e5','700')+'</g>'
b+='''<g transform="rotate(-5 842 208)" filter="url(#shadow)"><rect x="716" y="109" width="277" height="128" fill="#f2eddf"/>'''+text(736,162,'off/grid',40,'#1d1e19','900')+text(737,198,'INDEPENDENT BY NATURE',12,'#1d1e19','700')+'</g>'
b+=text(66,907,'IDENTITY SYSTEM  /  01',16,'#57574e')+text(1065,907,'O/G',22,'#292921','700')
svg('off-grid','#d9d4c5',b)
# Expressive typography; form is custom, not an existing type designer's work.
b='<rect x="0" y="0" width="1200" height="960" fill="#ea3923"/>'
b+=text(59,79,'BETWEEN / THE LINES',23,'#f3eee2','700')+text(1030,79,'字间',25,'#f3eee2','700')
b+='<g fill="#f4eee1"><path d="M100 151h342v92H211v101h192v90H211v220H100z"/><path d="M495 151h113v391h219v112H495z"/><path d="M883 151h113v503H883z"/></g>'
b+='<g fill="#f4eee1"><path d="M94 720h1008v14H94z"/><path d="M95 769h555v8H95z"/><path d="M720 769h381v8H720z"/></g>'
b+=text(76,592,'形',335,'#ea3923','900')+text(693,613,'间',355,'#ea3923','900')
b+=text(88,847,'FORM IS A LANGUAGE.',46,'#f3eee2','700')+text(90,903,'TYPE EXPLORATION  /  SPACE · RHYTHM · STRUCTURE',17,'#f3eee2')
svg('between','#ea3923',b)
# Poster pair with deliberate print margins.
b='''<defs><filter id="sh"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-opacity=".18"/></filter><pattern id="dots" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#e5e5db" opacity=".2"/></pattern></defs><g transform="rotate(-6 372 463)" filter="url(#sh)"><rect x="101" y="88" width="528" height="740" fill="#dfeb46"/>'''
b+=text(132,143,'AFTER HOURS',41,'#21251d','900','letter-spacing="-2"')+text(135,183,'SOUND WITHOUT BOUNDARIES',14,'#21251d','700')
for i in range(12):
    b+=f'<ellipse cx="371" cy="465" rx="{223-i*17}" ry="{245-i*19}" fill="none" stroke="#22271e" stroke-width="{8 if i%2 else 5}" transform="rotate({i*2} 371 465)"/>'
b+=text(133,773,'VOLUME 03 / FEEL THE FREQUENCY',17,'#22271e','700')+'</g>'
b+='''<g transform="rotate(7 850 500)" filter="url(#sh)"><rect x="630" y="148" width="434" height="669" fill="#20281e"/>'''
b+=text(661,209,'AFTER',75,'#dfe846','900','letter-spacing="-5"')+text(661,278,'HOURS',75,'#dfe846','900','letter-spacing="-5"')
for i in range(19):
    x=664+i*19;b+=f'<path d="M{x} 355 Q {x+230} 501 {x} 668" stroke="#dce744" stroke-width="7" fill="none"/>'
b+=text(663,770,'LISTEN A LITTLE CLOSER.',18,'#e3eacd','700')+'</g>'
svg('after-hours','#b7bda8',b)
# Product interface, rendered as readable original UI composition.
b='''<defs><filter id="shadow"><feDropShadow dx="0" dy="20" stdDeviation="20" flood-opacity=".12"/></filter></defs><circle cx="1044" cy="124" r="247" fill="#dbe4d1"/><circle cx="99" cy="830" r="278" fill="#c4d0b8"/><g filter="url(#shadow)"><rect x="86" y="113" width="1028" height="684" rx="16" fill="#f8f9f4"/><path d="M102 113h996a16 16 0 0116 16v40H86v-40a16 16 0 0116-16" fill="#eaede4"/><circle cx="114" cy="141" r="5" fill="#b9c1b0"/><circle cx="132" cy="141" r="5" fill="#b9c1b0"/><circle cx="150" cy="141" r="5" fill="#b9c1b0"/>'''
b+=text(538,148,'field — a little space to focus',13,'#6d7667')+text(126,226,'field',37,'#293b2b','700')+text(676,218,'Explore',14,'#263c2c')+text(766,218,'My space',14,'#788370')+text(874,218,'Journal',14,'#788370')
b+='<circle cx="1060" cy="211" r="19" fill="#d1dbc6"/>'+text(1052,216,'F',14,'#3e523b','700')
b+=text(130,311,'A calmer kind of everyday.',39,'#293b2b','500','letter-spacing="-1"')+text(130,343,'Find your focus. Make room for what matters.',17,'#87907f')
b+='''<rect x="128" y="380" width="568" height="315" rx="12" fill="#1c4339"/><path d="M128 620C237 406 447 553 542 380h154v315H128z" fill="#56715b"/><path d="M128 649c210-212 333 97 568-143v189H128z" fill="#8ba485"/><circle cx="613" cy="436" r="24" fill="#dce6b6"/>'''
b+=text(155,424,'THE DAILY PAUSE',12,'#e0e7cb','700')+text(155,614,'Come back to yourself.',31,'#f4f6e6','500')+text(155,649,'12 min  ·  Guided focus',14,'#dae3cb')
b+='<circle cx="647" cy="646" r="23" fill="#e0e8c8"/><path d="M641 637l15 9-15 9z" fill="#345346"/>'
b+='<rect x="716" y="380" width="356" height="143" rx="12" fill="#e9ecd5"/>'+text(740,414,'YOUR WEEK, IN BALANCE',12,'#64705b','700')
for i,h in enumerate([30,44,25,51,39,62,46]): b+=f'<rect x="{746+i*42}" y="{497-h}" width="24" height="{h}" rx="5" fill="{"#57724f" if i==5 else "#bcc9a5"}"/>'
b+='<rect x="716" y="542" width="356" height="153" rx="12" fill="#ebe7de"/>'+text(741,579,'SMALL STEPS',12,'#756d5c','700')+text(740,620,'One thing at a time.',24,'#4c5142')+text(740,657,'Open your journal  ↗',14,'#747963')
b+=text(130,751,'A space for a more intentional day.',14,'#8c9481')+text(926,751,'TAKE A BREATH ↗',12,'#3d583c','700')+'</g>'
svg('field','#d3dcc9',b)
# Optical motion art.
b='<defs><style>@media(prefers-reduced-motion:no-preference){.rot{transform-origin:600px 480px;animation:rotate 24s linear infinite}@keyframes rotate{to{transform:rotate(360deg)}}}</style></defs>'+text(64,83,'LOOP / 001',24,'#f0efe7','700')+text(889,83,'MOTION STUDIES',18,'#eeefe4')
b+='<g class="rot">'
for i in range(20):
 a=i*18;b+=f'<ellipse cx="600" cy="480" rx="310" ry="87" transform="rotate({a} 600 480)" fill="none" stroke="{"#f96632" if i%2 else "#f2a54c"}" stroke-width="8"/>'
b+='</g><circle cx="600" cy="480" r="110" fill="#244bc4"/>'+text(521,502,'∞',140,'#f2eee3','400')+text(64,901,'ALWAYS IN MOTION.',36,'#f4f0e6','700')+text(1002,901,'↻',47,'#f4f0e6')
svg('loop','#244bc4',b)
# Original mascot figures.
def mascot(x,y,scale,color='#cab4f1',pose='normal'):
 return f'''<g transform="translate({x} {y}) scale({scale})"><ellipse cx="0" cy="184" rx="132" ry="20" fill="#171a16" opacity=".09"/><path d="M-88 77q-57 10-60-30-2-24 32-37l22 24M88 77q57 10 60-30 2-24-32-37l-22 24" fill="{color}" stroke="#292820" stroke-width="5"/><path d="M-60 115l-9 56q-1 18-31 17h-17q-21-5-5-22l31-25v-37M60 115l9 56q1 18 31 17h17q21-5 5-22l-31-25v-37" fill="{color}" stroke="#292820" stroke-width="5"/><path d="M-100 65c-36-76 3-106 4-154 1-46 28-59 65-21 20 20 42 20 63 0 37-38 63-25 64 21 1 48 40 78 4 154-28 71-170 71-200 0" fill="{color}" stroke="#292820" stroke-width="5"/><ellipse cx="-33" cy="-9" rx="19" ry="24" fill="#fffbed"/><ellipse cx="33" cy="-9" rx="19" ry="24" fill="#fffbed"/><ellipse cx="-26" cy="-7" rx="7" ry="12" fill="#292820"/><ellipse cx="40" cy="-7" rx="7" ry="12" fill="#292820"/><path d="M-20 41q20 19 40 0" fill="none" stroke="#292820" stroke-width="5" stroke-linecap="round"/></g>'''
b=text(66,162,'mimo',131,'#292820','900','letter-spacing="-9"')+text(728,84,'A LITTLE ODD.',20,'#292820','700')+text(728,113,'A LOT OF CHARACTER.',20,'#292820','700')
b+='<path d="M0 751q288-67 600-12t600-31v252H0" fill="#cbc0e7"/>'+star(1024,263,95,11,'#e97041')+mascot(600,474,1.66)+mascot(242,553,.87,'#e8ec84')+mascot(966,571,.8,'#fb9768')
b+=text(69,896,'MEET YOUR EVERYDAY COMPANION.',24,'#292820','700')+text(1071,899,'☺',49,'#292820')
svg('mimo','#e5daf4',b)
# Packaging: original cylindrical tea labels.
b='''<defs><filter id="s"><feDropShadow dx="6" dy="18" stdDeviation="16" flood-opacity=".14"/></filter><pattern id="p" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M0 28L28 0" stroke="#e1ddd2" stroke-width="1"/></pattern></defs><rect width="1200" height="960" fill="url(#p)"/>'''
for x,y,rot,c,label,num in [(295,432,-13,'#ed6638','DAWN','01'),(609,504,5,'#718450','MOSS','02'),(901,438,17,'#68949d','MIST','03')]:
 b+=f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#s)"><rect x="-123" y="-235" width="246" height="478" rx="25" fill="#e9e4d5"/><ellipse cx="0" cy="-216" rx="121" ry="30" fill="#f8f4e8"/><rect x="-122" y="-153" width="244" height="310" fill="{c}"/>'
 b+=text(-95,-109,'STILL',30,'#f8f0dd','700')+text(-95,-81,'A MOMENT TO YOURSELF',8,'#f8f0dd','700')+text(-98,28,num,110,'#f8f0dd','400','letter-spacing="-8"')+text(-94,110,label,34,'#f8f0dd','500')+text(-94,136,'LOOSE LEAF TEA · 80 g',9,'#f8f0dd')+'</g>'
b+=text(66,884,'STILL / THE RITUAL COLLECTION',27,'#5c6255','500')
svg('still','#ece8dc',b)
# Exhibition graphic with systematic forms, black and cobalt.
b='''<rect x="112" y="77" width="976" height="806" fill="#eeeade"/><path d="M155 135h890M155 806h890" stroke="#22211d" stroke-width="2"/>'''+text(153,119,'FORM / FORM / FORM',17,'#26251f','700')+text(923,119,'展览视觉',17,'#26251f','700')
b+=text(150,310,'FORM',194,'#252520','900','letter-spacing="-12"')+text(154,469,'MATTERS',159,'#252520','900','letter-spacing="-11"')
b+='<rect x="163" y="508" width="251" height="251" fill="#3154d0"/><circle cx="598" cy="633" r="126" fill="#3154d0"/><path d="M777 759l126-251 126 251z" fill="#3154d0"/>'
b+=text(158,845,'SHAPES IN CONVERSATION',23,'#252520','700')+text(905,845,'01 — 03',23,'#252520')
svg('form','#888779',b)
# Hero small collage: transparent background, crafted typography + expressive character.
b='''<defs><filter id="s"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-opacity=".12"/></filter></defs><g transform="rotate(-12 240 230)" filter="url(#s)"><rect x="35" y="77" width="309" height="342" fill="#ef4428"/>'''+text(59,173,'MAKE',73,'#f4f0e5','900','letter-spacing="-5"')+text(59,241,'IT',73,'#f4f0e5','900','letter-spacing="-5"')+text(59,309,'BOLD.',73,'#f4f0e5','900','letter-spacing="-5"')+text(65,384,'IDEAS → VISUALS',14,'#f4f0e5','700')+'</g>'
b+='''<g transform="rotate(9 401 298)" filter="url(#s)"><rect x="264" y="171" width="266" height="284" fill="#3155ce"/>'''
for i in range(12):b+=f'<ellipse cx="395" cy="305" rx="96" ry="25" transform="rotate({i*15} 395 305)" fill="none" stroke="#e9ed9d" stroke-width="3"/>'
b+='</g><g transform="translate(432 109)">'+star(0,0,75,11,'#d6df65')+'</g>'+mascot(453,382,.42,'#cdb5ed')
svg('hero','#f4f2e9',b,600,530)
# favicon
(A/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="13" fill="#ef4428"/>'+star(32,32,24,8,'#f5f1e7')+'</svg>')
print('Generated',len(list(A.glob('*.svg'))),'original SVG assets.')
