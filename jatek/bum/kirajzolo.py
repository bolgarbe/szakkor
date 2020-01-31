import pygame

class Kirajzolo:
    def __init__(self,kepszel,kepmag):
        pygame.init()
        self.screen = pygame.display.set_mode((kepszel,kepmag))
        self.font = pygame.font.SysFont("monospace",25)
        self.kepszel,self.kepmag = kepszel,kepmag
        
    def torol(self):
        self.screen.fill(0x000000)       
    
    def labkirajzol(self,lab):
        labi=lab.labi
        mug=lab.mug
        mag=lab.mag
        k=self.kepmag//mag
        for i in range (mug):
            for j in range (mag):
                if labi[i,j,1]==0:
                    pygame.draw.line(self.screen,0xffffff,(j*k,i*k),(j*k,i*k+k),4)
                if labi[i,j,2]==0:
                    pygame.draw.line(self.screen,0xffffff,(j*k+k,i*k),(j*k+k,i*k+k),4)
                if labi[i,j,3]==0:
                    pygame.draw.line(self.screen,0xffffff,(j*k,i*k),(j*k+k,i*k),4)
                if labi[i,j,4]==0:
                    pygame.draw.line(self.screen,0xffffff,(j*k,i*k+k),(j*k+k,i*k+k),4)
                pygame.draw.circle(self.screen, 0xffffff, (i*k,j*k), 5)
                
    def playkirajzol(self,fiz,log):
        for i in range(log.players):
            if log.elet[i]>0:
                pygame.draw.circle(self.screen, 0xffffff,(fiz.x[i].astype(int),fiz.y[i].astype(int)),7)
                pygame.draw.line(self.screen,0xffffff,((fiz.x[i]+15*fiz.cos[i],fiz.y[i]-15*fiz.sin[i])),(fiz.x.astype(int)[i],fiz.y.astype(int)[i]),2)
        for i in range(log.lovedekek):
            if log.elet[i+log.players]>0:
                pygame.draw.circle(self.screen, 0xffffff,(fiz.x[i+log.players].astype(int),fiz.y[i+log.players].astype(int)),3)
    
    def eletjel(self,elet):
        pontok=self.font.render("Egyes jatekos: {0}, Kettes jatekos: {1}".format(elet[0],elet[1]),1,(255,0,0))
        self.screen.blit(pontok,(10,0))
        
    def vege(self):
        pygame.display.flip()
    
    def nyertes(self,nyer):
        felirat=self.font.render("Nyertes:{}. jatekos".format(nyer+1),3,(255,0,0))
        self.screen.blit(felirat,(200,200))
        