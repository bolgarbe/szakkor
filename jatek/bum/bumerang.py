from labirintus import Labirintus
from kirajzolo import Kirajzolo
from iranyitas import Iranyitas
from fizika import Fizika
from logika import Logika

import time

lab = Labirintus(7,7)
lab.general()

kepmag = 600
kir = Kirajzolo(kepmag,kepmag)
iranyito = Iranyitas(2)
log = Logika(2,10)
fiz = Fizika(log.players,log.lovedekek,kepmag)
log.indit(fiz,lab.mag,kepmag)
megy = True

while megy:
    iranyito.feldolgoz()
    fiz.leptet(iranyito,lab,log)
    log.leptet(fiz,iranyito)
    kir.torol()
    kir.playkirajzol(fiz,log)
    kir.labkirajzol(lab)
    kir.eletjel(log.elet)
    kir.vege()
    if log.veg():
        megy = False
    time.sleep(0.001)

kir.nyertes(log.nyertes())
kir.vege()
while True:
    pass
    
