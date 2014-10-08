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
    #stroke(255, 102, 0)
    background(255)
    ellipseMode(RADIUS)
    spawnAttackers()
    strokeWeight(3)
    
def spawnAttackers():
    for a in range(ATTACKERAMOUNT):
        attackers.append(Attacker(15, defender, randint(0,width), HEADERHEIGHT/2, (255,170,170)))
        
    for a in attackers:
        a.othersList = attackers
        #a.othersList.append(defender)
    
def getLoc(x,y):
    return x + (y*(width))

def draw():
    background(0)
    defender.update()
    defender.drawLines()
    for attacker in attackers:
        attacker.update()
        attacker.collide()
    if len(attackers) < ATTACKERAMOUNT:
        attackers.append(Attacker(15, defender, randint(0,width), HEADERHEIGHT/2, (255,170,170)))
