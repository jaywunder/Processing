from random import randint
from defender import Defender
from attacker import Attacker

defender = Defender(20,640/2,640/2,(170,170,255))
HEADERHEIGHT = 50
ATTACKERAMOUNT = 4
attackers = []
ACCLMAX = 1.5

def setup():
    size(640,640)
    noFill()
    stroke(255, 102, 0)
    line(85, 20, 10, 10)
    line(90, 90, 15, 80)
    stroke(0, 0, 0)
    bezier(85, 20, 10, 10, 90, 90, 15, 80)
    background(200)
    ellipseMode(RADIUS)
    spawnAttackers()
    
def spawnAttackers():
    for a in range(ATTACKERAMOUNT):
        attackers.append(Attacker(15, defender, randint(0,width), HEADERHEIGHT/2, (255,170,170)))
    
def getLoc(x,y):
    return x + (y*(width))

def draw():
    background(200)
    line(0,HEADERHEIGHT,width,HEADERHEIGHT)
    defender.update()
    for attacker in attackers:
        attacker.update()
        attacker.collide()
