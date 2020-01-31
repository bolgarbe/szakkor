import pygame
import numpy as np

grd = np.array([[1,1,0],[-1,1,0],[1,-1,0],[-1,-1,0],
       [1,0,1],[-1,0,1],[1,0,-1],[-1,0,-1],
       [0,1,1],[0,-1,1],[0,1,-1],[0,-1,-1]])

p = np.arange(256)
np.random.shuffle(p)
p = np.hstack([p,p])

def lerp(a,b,t):
    return a + (b-a)*t

def fade(t):
    return t*t*t*(t*(t*6-15)+10)

def dt(h,x,y,z):
    g = grd[h%12]
    return g[:,:,0]*x + g[:,:,1]*y + g[:,:,2]*z

def perlin(size,bs,z):
    x = np.linspace(0.0,size/float(bs),size)
    y = np.linspace(0.0,size/float(bs),size)
    z = z%256
    
    coords = np.meshgrid(x,y)
    xi = coords[0].astype(int)
    yi = coords[1].astype(int)
    zi = int(z)
    xf = coords[0]-xi
    yf = coords[1]-yi
    zf = z-zi
    u = fade(xf)
    v = fade(yf)
    w = fade(zf)
    aaa = p[p[p[xi]+yi]+zi]
    aab = p[p[p[xi]+yi]+zi+1]
    aba = p[p[p[xi]+yi+1]+zi]
    abb = p[p[p[xi]+yi+1]+zi+1]
    baa = p[p[p[xi+1]+yi]+zi]
    bab = p[p[p[xi+1]+yi]+zi+1]
    bba = p[p[p[xi+1]+yi+1]+zi]
    bbb = p[p[p[xi+1]+yi+1]+zi+1]
    
    x1 = lerp(dt(aaa,xf,yf,zf),dt(baa,xf-1,yf,zf),u)
    x2 = lerp(dt(aba,xf,yf-1,zf),dt(bba,xf-1,yf-1,zf),u)
    y1 = lerp(x1,x2,v)
    
    x3 = lerp(dt(aab,xf,yf,zf-1),dt(bab,xf-1,yf,zf-1),u)
    x4 = lerp(dt(abb,xf,yf-1,zf-1),dt(bbb,xf-1,yf-1,zf-1),u)
    y2 = lerp(x3,x4,v)
    
    return (lerp(y1,y2,w)+1)*127

size = 200

pygame.init()
screen = pygame.display.set_mode((size,size))
running = True;
z=0.0

def villam(size,z):
    img = np.outer(255/(1+np.exp(-0.08*np.arange(-size/2,size/2))),np.ones(size))
    per = (perlin(size,10,z*5.3) + perlin(size,64,z))/2
    img = np.clip(255-np.abs(per - img),0,255)
    bimg = 255/(1.0+np.exp(-0.3*(img-220)))
    gimg = 255/(1.0+np.exp(-0.3*(img-230)))
    rimg = 255/(1.0+np.exp(-0.3*(img-240)))
    return rimg,gimg,bimg

def tuz(size,z):
    per = (perlin(size,24,z*1.7) + perlin(size,64,z))/2
    img = np.clip(255-np.abs(per-170),0,255)
    rimg = 255/(1.0+np.exp(-0.1*(img-130)))
    gimg = 255/(1.0+np.exp(-0.1*(img-180)))
    bimg = 255/(1.0+np.exp(-0.1*(img-200)))
    return rimg,gimg,bimg
    
def tuz2(size,z):
    img = perlin(size,64,z)*2 - perlin(size,16,z)
    rimg = 255/(1.0+np.exp(-0.1*(img-180)))
    gimg = 255/(1.0+np.exp(-0.1*(img-200)))
    bimg = 255/(1.0+np.exp(-0.1*(img-220)))
    return rimg,gimg,bimg
    
def fust(size,z):
    img = (perlin(size,64,z/4)*4 + perlin(size,32,z/2)*2 + perlin(size,16,z))/7
    return img,img,img
    
def eter(size,z):
    per = (perlin(size,8,z/4) + perlin(size,32,z/4))/2
    img = np.clip((255-np.abs(per-220)+perlin(size,128,z/4))/2,0,255)
    rimg = 255/(1.0+np.exp(-0.2*(img-170)))
    bimg = 255/(1.0+np.exp(-0.2*(img-220)))
    gimg = 255/(1.0+np.exp(-0.2*(img-220)))
    return rimg,gimg,bimg
    
def jeg(size,z):
    p1 = perlin(size,16,z/8)
    img = (perlin(size,size,z/4) + perlin(size,64,1) + p1)/3
    img2 = np.clip(255-np.abs(p1-200),0,255)
    img2 = 255/(1.0+np.exp(-0.1*(img2-250)))
    bimg = np.clip(255/(1.0+np.exp(-0.05*(img-120))) + img2,0,255)
    gimg = np.clip(255/(1.0+np.exp(-0.05*(img-150))) + img2,0,255)
    rimg = np.clip(255/(1.0+np.exp(-0.05*(img-155)))/2 + img2,0,255)
    return rimg,gimg,bimg

running = True
while running:
    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.QUIT:
            running = False
                
    screen.fill((0,0,0))
    rimg,gimg,bimg = jeg(size,z)
    
    for i in range(size):
        for j in range(size):
            screen.set_at((i,j),(rimg[i,j],gimg[i,j],bimg[i,j]))
       
    pygame.display.flip()
    z+=0.13
