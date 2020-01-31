import numpy as np
import pygame

N=250
size=2
b=2
h=0

pygame.init()
screen = pygame.display.set_mode((N*size,N*size))

s=2*np.random.randint(2,size=(N,N))-1

while(True):
    ev = pygame.event.get();
    for e in ev:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                h+=0.05
                print("h: {:.2f}".format(h))
            if e.key == pygame.K_DOWN:
                h-=0.05
                print("h: {:.2f}".format(h))
            if e.key == pygame.K_LEFT:
                b-=0.45
                print("b: {:.2f}".format(b))
            if e.key == pygame.K_RIGHT:
                b+=0.45
                print("b: {:.2f}".format(b))
    for i in range(N*N):
        x = np.random.randint(0,N)
        y = np.random.randint(0,N)
        H = 2*s[x,y]*(s[(x+1)%N,y]+s[(x-1)%N,y]+s[x,(y+1)%N]+s[x,(y-1)%N]+h)
        E = np.exp(-b*H)
        if E<0 or np.random.rand()<E:
            s[x,y]*=-1
    
    screen.fill(0x000000)
    for i in range(N):
        for j in range(N):
            col = 0x000000
            if s[i,j]<0:
                col = 0xffffff
            pygame.draw.rect(screen,col,[i*size,j*size,size,size])
    pygame.display.flip()
