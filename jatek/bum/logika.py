import numpy as np

class Logika:
    def __init__(self,players,lov):
        self.players = players
        self.lov = lov
        self.lovedekek = lov*players
        self.elet = np.array([15]*self.players + [0]*self.lovedekek)
    
    def indit(self,fiz,mag,kepmag):
        k = kepmag//mag
        fiz.x[:self.players] = np.random.randint(mag,size=self.players).astype(np.float)*k+k/2
        fiz.y[:self.players] = np.random.randint(mag,size=self.players).astype(np.float)*k+k/2
        fiz.szog[:self.players]=np.ones(self.players)*np.pi/2
        
        fiz.px =fiz.x
        fiz.py =fiz.y
        
    def leptet(self,fiz,ir):
        for p in range(self.players):
            if ir.tuzel[p] and self.elet[p]>0:
                plp = p*self.lov+self.players
                pp = np.argmin(self.elet[plp:plp+self.lov])+plp
                if self.elet[pp] < 0:
                    fiz.x[pp] = fiz.x[p]+6*fiz.cos[p]
                    fiz.y[pp] = fiz.y[p]-6*fiz.sin[p]
                    fiz.px[pp] = fiz.x[p]+5.5*fiz.cos[p]
                    fiz.py[pp] = fiz.y[p]-5.5*fiz.sin[p]
                    self.elet[pp] = 2000
                    ir.tuzel[p]=False
        
        self.elet[self.players:]-=1

        talalat = np.sum(fiz.tav<5,axis=1)
        self.elet -= talalat
    
    def veg(self):
        return np.sum(self.elet[:self.players]>0)==1
    
    def nyertes(self):
        return np.argwhere(self.elet[:self.players]>0)[0,0]