import pygame
import numpy as np

class Iranyitas:
    def __init__(self,players):
        self.players = players
        self.gyorsit=np.zeros(players,dtype=np.bool)
        self.lassit=np.zeros(players,dtype=np.bool)
        self.forog_bal=np.zeros(players,dtype=np.bool)
        self.forog_jobb=np.zeros(players,dtype=np.bool)
        self.tuzel=np.zeros(players,dtype=np.bool)
        
    def feldolgoz(self):
        ev = pygame.event.get()
        for e in ev:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.gyorsit[0]=True
                if e.key == pygame.K_DOWN:
                    self.lassit[0]=True
                if e.key == pygame.K_RIGHT:
                    self.forog_jobb[0]=True
                if e.key == pygame.K_LEFT:
                    self.forog_bal[0]=True
                if e.key == pygame.K_RSHIFT:
                    self.tuzel[0]=True
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    self.gyorsit[0]=False
                if e.key == pygame.K_DOWN:
                    self.lassit[0]=False
                if e.key == pygame.K_RIGHT:
                    self.forog_jobb[0]=False
                if e.key == pygame.K_LEFT:
                    self.forog_bal[0]=False
                if e.key == pygame.K_RSHIFT:
                    self.tuzel[0]=False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    self.gyorsit[1]=True
                if e.key == pygame.K_s:
                    self.lassit[1]=True
                if e.key == pygame.K_d:
                    self.forog_jobb[1]=True
                if e.key == pygame.K_a:
                    self.forog_bal[1]=True
                if e.key == pygame.K_f:
                    self.tuzel[1]=True
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_w:
                    self.gyorsit[1]=False
                if e.key == pygame.K_s:
                    self.lassit[1]=False
                if e.key == pygame.K_d:
                    self.forog_jobb[1]=False
                if e.key == pygame.K_a:
                    self.forog_bal[1]=False
                if e.key == pygame.K_f:
                    self.tuzel[1]=False