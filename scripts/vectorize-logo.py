import cv2, numpy as np, sys
im=cv2.imread(sys.argv[1],cv2.IMREAD_UNCHANGED)
b,g,r,a=cv2.split(im)
red=((a>128)&(r>150)&(g<120)).astype(np.uint8)*255
white=((a>128)&(r>200)&(g>200)&(b>200)).astype(np.uint8)*255
x0,y0,x1,y1=176,557,1829,1444
def paths(mask,eps=0.6,sep=False):
    cs,h=cv2.findContours(mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    out=[]
    for c in cs:
        if cv2.contourArea(c)<30: continue
        c=cv2.approxPolyDP(c,eps,True)
        d="M"+" L".join(f"{p[0][0]-x0},{p[0][1]-y0}" for p in c)+"Z"
        out.append((d,cv2.boundingRect(c)))
    return out
rays=paths(red)
# sort rays by angle around sun center
cx=(x1-x0)/2; cy=0
import math
def ang(br):
    x,y,w,h=br; return math.atan2((y+h/2)-(972-y0),(x+w/2)-(969-x0))
rays.sort(key=lambda t:ang(t[1]))
words=paths(white)
W,H=x1-x0,y1-y0
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="SUNRISE Bangkok Pattaya">']
s.append('<g id="sun" fill="#D82E2F">')
for i,(d,_) in enumerate(rays): s.append(f'<path class="ray" data-i="{i}" d="{d}"/>')
s.append('</g><g id="wordmark" fill="#FFFFFF" fill-rule="evenodd"><path d="'+" ".join(d for d,_ in words)+'"/></g></svg>')
open(sys.argv[2],'w').write("\n".join(s))
print(len(rays),"rays",len(words),"white parts")
