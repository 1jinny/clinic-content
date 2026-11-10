# 불당드림치과 썸네일 표준 v5 (가이드 수치 그대로)
import sys
from PIL import Image, ImageDraw, ImageFont
src, out, off, l1, l2, fontdir = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
W,H=1200,675
im=Image.open(src).convert('RGB')
sc=max(W/im.width,H/im.height); im=im.resize((round(im.width*sc),round(im.height*sc)),Image.LANCZOS)
top=min(off,im.height-H); left=(im.width-W)//2
im=im.crop((left,top,left+W,top+H)).convert('RGBA')
ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
fb=ImageFont.truetype(fontdir+'/Pretendard-Black.otf',58)
fl=ImageFont.truetype(fontdir+'/Pretendard-Bold.otf',28)
X,BOT,PY,PX,GAP=60,36,8,10,12
lines=[l1,l2]; boxes=[]
y=H-BOT
for t in reversed(lines):
    bb=d.textbbox((0,0),t,font=fb); w,h=bb[2]-bb[0],bb[3]-bb[1]
    assert w<=1080, (t,w)
    y0=y-(h+2*PY); boxes.insert(0,(t,bb,y0,w,h)); y=y0-GAP
txt=[]
for t,bb,y0,w,h in boxes:
    d.rectangle((X,y0,X+w+2*PX,y0+h+2*PY),fill=(0x95,0xD0,0x66,235))
    txt.append((X+PX-bb[0],y0+PY-bb[1],t))
# logo tag above title box
lb=d.textbbox((0,0),'불당드림치과',font=fl); lw,lh=lb[2]-lb[0],lb[3]-lb[1]
ly1=boxes[0][2]; ly0=ly1-(lh+2*PY)
d.rectangle((X,ly0,X+lw+2*PX,ly1),fill=(255,255,255,220))
im=Image.alpha_composite(im,ov); d=ImageDraw.Draw(im)
d.text((X+PX-lb[0],ly0+PY-lb[1]),'불당드림치과',font=fl,fill=(110,110,110))
for x,y,t in txt: d.text((x,y),t,font=fb,fill=(15,17,19))
im=im.convert('RGB')
im.save(out+'.webp','WEBP',quality=76,method=6); im.save(out+'.jpg',quality=88)
