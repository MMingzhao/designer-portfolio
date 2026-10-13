from pathlib import Path
from math import sin,cos,pi
A=Path(__file__).resolve().parents[1]/'assets'
def text(x,y,s,size,fill,weight='400',spacing='0'):
 return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" fill="{fill}">{s}</text>'
def star(cx,cy,r,n,fill):
 pts=' '.join(f'{cx+(r if i%2==0 else r*.48)*cos(i*pi/n):.1f},{cy+(r if i%2==0 else r*.48)*sin(i*pi/n):.1f}' for i in range(n*2))
 return f'<polygon points="{pts}" fill="{fill}"/>'
b='''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1100" viewBox="0 0 1800 1100"><defs><filter id="soft"><feDropShadow dx="0" dy="25" stdDeviation="23" flood-color="#28271c" flood-opacity=".22"/></filter><pattern id="paper" width="4" height="4" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".4" fill="#342d20" opacity=".06"/></pattern></defs><rect width="1800" height="1100" fill="#cbc6b7"/><rect width="1800" height="1100" fill="url(#paper)"/><g transform="rotate(-8 510 542)" filter="url(#soft)"><rect x="169" y="78" width="687" height="920" fill="#f14428"/>'''
b+=text(218,134,'OFF/GRID — INDEPENDENT BY NATURE',19,'#23251d','700')
for y,t in [(343,'GROW'),(532,'YOUR'),(721,'OWN'),(910,'WAY.')]:b+=text(209,y,t,191,'#f3eedc','900','-14')
b+='</g><g transform="rotate(8 1278 639)" filter="url(#soft)"><path d="M1055 300V175q0-68 66-68h182q67 0 67 68v126" fill="none" stroke="#272a21" stroke-width="29"/><path d="M956 273h624l-20 714h-584z" fill="#23261f"/><path d="M979 292h580M1000 310l-1 653M1536 310l-1 653" stroke="#515446" fill="none" stroke-width="2"/>'
b+=star(1267,592,206,10,'#dfe84c')+text(1017,898,'off/grid',100,'#f4f0e2','900','-7')+text(1024,949,'FREE TO FORM. FREE TO GROW.',18,'#f4f0e2','500')+'</g>'
b+='<g transform="rotate(11 924 836)" filter="url(#soft)"><rect x="743" y="714" width="397" height="257" fill="#f3f0e4"/>'+text(777,777,'off/grid',46,'#24251e','900','-3')+text(777,866,'A DIFFERENT WAY',20,'#24251e','700')+text(777,894,'TO THINK. TO MAKE. TO BE.',13,'#24251e','500')+'<path d="M777 913h323" stroke="#24251e" stroke-width="1"/></g>'
b+='</svg>'
(A/'off-grid-wide.svg').write_text(b)
old=(A/'field.svg').read_text();start=old.index('>')+1;inner=old[start:old.rfind('</svg>')]
b='''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1040" viewBox="0 0 1800 1040"><defs><filter id="phoneShadow"><feDropShadow dx="-4" dy="24" stdDeviation="19" flood-color="#2c4637" flood-opacity=".22"/></filter></defs><rect width="1800" height="1040" fill="#d3dcc9"/>'''
b+='<svg x="-63" y="-74" width="1560" height="1248" viewBox="0 0 1200 960">'+inner+'</svg>'
b+='''<g transform="rotate(7 1462 535)" filter="url(#phoneShadow)"><rect x="1268" y="115" width="374" height="803" rx="53" fill="#29372e"/><rect x="1278" y="125" width="354" height="782" rx="43" fill="#f5f6ef"/><rect x="1388" y="137" width="133" height="26" rx="13" fill="#29372e"/>'''
b+=text(1306,157,'9:41',12,'#29372e','700')+text(1311,220,'field',36,'#2b4837','700')+text(1567,218,'☰',20,'#2b4837')
b+=text(1311,274,'A moment for you.',27,'#2b4837','400','-.6')+text(1311,308,'Find a little stillness.',15,'#909c83')
b+='<rect x="1309" y="347" width="294" height="306" rx="147" fill="#dce5cc"/><path d="M1339 570q59-199 206-83v112H1340" fill="#879f7a"/><circle cx="1456" cy="454" r="76" fill="none" stroke="#fbfbef" stroke-width="4"/>'+text(1402,465,'12:00',36,'#3b5e43','500')+text(1412,498,'BREATHE IN',10,'#3b5e43','700')
b+=text(1383,707,'The daily pause',23,'#2b4837')+text(1398,739,'GUIDED FOCUS',10,'#869778','500','1.2')+'<circle cx="1456" cy="801" r="33" fill="#2b4837"/><path d="M1448 788l22 13-22 13z" fill="#f3f4e5"/><rect x="1393" y="883" width="126" height="4" rx="2" fill="#29372e"/></g></svg>'
(A/'field-wide.svg').write_text(b)
