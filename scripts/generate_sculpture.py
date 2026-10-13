from pathlib import Path
from math import sin,cos,pi,sqrt
root=Path(__file__).resolve().parents[1]
def add(a,b):return tuple(a[i]+b[i] for i in range(3))
def sub(a,b):return tuple(a[i]-b[i] for i in range(3))
def mul(a,k):return tuple(x*k for x in a)
def dot(a,b):return sum(a[i]*b[i] for i in range(3))
def norm(a):return mul(a,1/sqrt(dot(a,a)))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def center(t):
 r=1.6+.62*cos(3*t)
 return(r*cos(2*t),r*sin(2*t),.86*sin(3*t))
def rotation(p):
 x,y,z=p;y,z=y*cos(.75)-z*sin(.75),y*sin(.75)+z*cos(.75)
 x,z=x*cos(.42)+z*sin(.42),-x*sin(.42)+z*cos(.42)
 x,y=x*cos(-.3)-y*sin(-.3),x*sin(-.3)+y*cos(-.3)
 return x,y,z
def point(u,v):
 t=2*pi*u; c=center(t); tangent=norm(sub(center(t+.001),center(t-.001)))
 n=norm(cross(tangent,(0,0,1)));b=cross(tangent,n)
 normal=add(mul(n,cos(v)),mul(b,sin(v)))
 return rotation(add(c,mul(normal,.43))),rotation(normal)
def project(p):
 d=8/(8-p[2]);return(700+p[0]*227*d,690-p[1]*227*d)
polys=[];N=660;M=144
light=norm((-1.5,-.5,3));light2=norm((1,2,1));view=(0,0,1)
for i in range(N):
 for j in range(M):
  u=(i+.5)/N;v=2*pi*(j+.5)/M
  p,n=point(u,v)
  diffuse=max(0,dot(n,light));fill=max(0,dot(n,light2))
  halfway=norm(add(light,view));spec=max(0,dot(n,halfway))**30
  # rich lacquer red with defined, soft studio lighting
  base=(238,47,20);shade=.22+.73*diffuse+.16*fill
  rgb=tuple(int(min(255,max(0,b*shade+spec*165))) for b in base)
  pts=[project(point(ui,2*pi*vj/M)[0]) for ui,vj in [(i/N,j),((i+1)/N,j),((i+1)/N,j+1),(i/N,j+1)]]
  coords=' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)
  col='#%02x%02x%02x'%rgb
  polys.append((p[2],f'<polygon points="{coords}" fill="{col}" stroke="{col}" stroke-width=".65"/>'))
polys.sort(key=lambda x:x[0])
svg='<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1380" viewBox="0 0 1400 1380">'+''.join(p[1] for p in polys)+'</svg>'
(root/'assets/sculpture.svg').write_text(svg)
print('Generated original parametric 3D sculpture',len(polys),'faces')
