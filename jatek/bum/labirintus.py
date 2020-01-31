import numpy as np

class Labirintus:
    def __init__(self,mag,mug):
        self.mag,self.mug = mag,mug
        self.labi = np.zeros((mag,mug,5))
    
    def general(self):
        r,c = 0,0
        tomb = [(r,c)]
        
        
        while tomb:
            self.labi[r,c,0]=1
            merre = []
            if c>0 and self.labi[r,c-1,0]!=1:
                merre.append("left")
            if c<self.mug-1 and self.labi[r,c+1,0]!=1:
                merre.append("right")
            if r>0 and self.labi[r-1,c,0]!=1:
                merre.append("up")
            if r<self.mag-1 and self.labi[r+1,c,0]!=1:
                merre.append("down")    
                
            if merre:
                tomb.append((r,c))
                lepes = np.random.choice(merre)
                if lepes=="left":
                    c -=1
                    self.labi[r,c+1,1]=1
                    self.labi[r,c,2]=1
                if lepes=="right":
                    c +=1
                    self.labi[r,c-1,2]=1
                    self.labi[r,c,1]=1    
                if lepes=="up":
                    r -=1
                    self.labi[r+1,c,3]=1
                    self.labi[r,c,4]=1  
                if lepes=="down":
                    r +=1
                    self.labi[r-1,c,4]=1
                    self.labi[r,c,3]=1            
            else:
                r,c = tomb.pop()