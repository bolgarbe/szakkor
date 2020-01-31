import numpy as np

class Fizika:
    def __init__(self,players,lovedekek,kepmag):
        self.players = players
        self.lovedekek = lovedekek

        self.x = np.zeros(players+lovedekek)
        self.y = np.zeros(players+lovedekek)
        self.szog=np.ones(players+lovedekek)*np.pi/2
        self.px=np.copy(self.x)
        self.py=np.copy(self.y)
        self.surlodas = np.array([0.99]*players + [1.0]*lovedekek)
        self.kepmag = kepmag
        self.sin=np.sin(self.szog[:self.players])
        self.cos=np.cos(self.szog[:self.players])
        
    def pattint(self,x1,x2,y1,y2,px1,px2,py1,py2,d):
        dx=(x1-x2)/d
        dy=(y1-y2)/d
        v1x,v1y,v2x,v2y=x1-px1,y1-py1,x2-px2,y2-py2
        
        
        ev1=dx*v1x+dy*v1y
        ev2=dx*v2x+dy*v2y
        
        pk1x=(ev1)*dx
        pk1y=(ev1)*dy
        pk2x=(ev2)*dx
        pk2y=(ev2)*dy
        
        v1x -= -pk2x+pk1x
        v1y -= -pk2y+pk1y
        v2x -= -pk1x+pk2x
        v2y -= -pk1y+pk2y
        
        return x1-v1x,x2-v2x,y1-v1y,y2-v2y
    
    def szetlok(self,i,j):
        rx = self.x[i]-self.x[j]
        ry = self.y[i]-self.y[j]
        r3 = np.sqrt(rx**2+ry**2)**3
        Fx = 0.5*rx/r3
        Fy = 0.5*ry/r3
        self.x[i] += Fx
        self.y[i] += Fy  
        self.x[j] -= Fx
        self.y[j] -= Fy             
                
                
            
    def leptet(self,ir,lab,log):
        # Iranyitas
        self.py,self.y=self.y,self.y+(self.y-self.py)*self.surlodas
        self.px,self.x=self.x,self.x+(self.x-self.px)*self.surlodas
        
        self.sin=np.sin(self.szog[:self.players])
        self.cos=np.cos(self.szog[:self.players])
        
        self.x[:self.players] += 0.003*self.cos*ir.gyorsit
        self.y[:self.players] -= 0.003*self.sin*ir.gyorsit
        self.x[:self.players] -= 0.001*self.cos*ir.lassit
        self.y[:self.players] += 0.001*self.sin*ir.lassit
        self.szog[:self.players] -= 0.01*ir.forog_jobb
        self.szog[:self.players] += 0.01*ir.forog_bal
        
        # Pattanas
        halott = log.elet <= 0
        self.tav = np.sqrt(np.subtract.outer(self.x,self.x)**2 + np.subtract.outer(self.y,self.y)**2) + np.add.outer(halott,halott)*1000 + np.eye(self.players+self.lovedekek)*1000
        
        # Player - player
        if self.tav[0,1]<=15:
                    self.px[0],self.px[1],self.py[0],self.py[1] = self.pattint(
                        self.x[0],self.x[1],self.y[0],self.y[1],
                        self.px[0],self.px[1],self.py[0],self.py[1],
                        self.tav[0,1])
        
        # Player - golyo            
        for i in range(2,self.tav.shape[0]):
            for j in range(2):
                if self.tav[i,j]<5:
                    self.px[i],self.px[j],self.py[i],self.py[j] = self.pattint(
                        self.x[i],self.x[j],self.y[i],self.y[j],
                        self.px[i],self.px[j],self.py[i],self.py[j],
                        self.tav[i,j])
        
        # Golyo - golyo
        for i in range(2,self.tav.shape[0]):
            for j in range(2,i):
                if self.tav[i,j]<=5:
                    self.px[i],self.px[j],self.py[i],self.py[j] = self.pattint(
                        self.x[i],self.x[j],self.y[i],self.y[j],
                        self.px[i],self.px[j],self.py[i],self.py[j],
                        self.tav[i,j])
                #if self.tav[i,j]<100:
                #    self.szetlok(i,j)
        
        # Falpattanas
        k = self.kepmag//lab.mag
        
        sor=np.floor(self.y/k).astype(int)
        oszlop=np.floor(self.x/k).astype(int)
        
        felfal = np.abs(sor*k-self.y)
        lefal = np.abs((sor+1)*k-self.y)
        balfal = np.abs(oszlop*k-self.x)
        jobbfal = np.abs((oszlop+1)*k-self.x)
        
        fy = np.logical_or(((felfal<6) & (lab.labi[sor,oszlop,3]==0)) ,
                           ((lefal<6) & (lab.labi[sor,oszlop,4]==0)))
        fx = np.logical_or(((balfal<6) & (lab.labi[sor,oszlop,1]==0)) ,
                           ((jobbfal<6) & (lab.labi[sor,oszlop,2]==0)))
        
        fbsarok = (felfal**2 + balfal**2)<25
        fjsarok = (felfal**2 + jobbfal**2)<25
        lbsarok = (lefal**2 + balfal**2)<25
        ljsarok = (lefal**2 + jobbfal**2)<25
           
        fy = np.logical_or(fy,fbsarok)
        fy = np.logical_or(fy,fjsarok)
        fy = np.logical_or(fy,lbsarok)
        fy = np.logical_or(fy,ljsarok)
        fx = np.logical_or(fx,fbsarok)
        fx = np.logical_or(fx,fjsarok)
        fx = np.logical_or(fx,lbsarok)
        fx = np.logical_or(fx,ljsarok)
        
        self.y = fy*(2*self.py-self.y) + (1-fy)*self.y
        self.x = fx*(2*self.px-self.x) + (1-fx)*self.x