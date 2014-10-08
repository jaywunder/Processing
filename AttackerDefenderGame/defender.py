from random import randint
from laser import Laser

class Defender(object):
    def __init__(self, radius, x, y, bgcolor):
        self.radius = radius
        self.x = x
        self.y = y
        self.bgcolor = bgcolor
        
        self.angle = 0
        self.laserAngle = radians(self.angle)
        self.loadRadius = 10.00
        self.lasers = []
        self.health = 100
        self.damageTime = 0
        self.score = 0
        
#UPDATE FUNCTION
    def update(self):
        self.x = mouseX
        self.y = mouseY
        
        if self.angle <= 360:
            self.angle += 1
        else:
            self.angle = 0
        self.laserAngle = radians(self.angle) 
        
        if mouseButton and self.loadRadius >= 10:
            self.fireLasers()
            self.loadRadius = 0
            
        if len(self.lasers) > 0:
            for laser in self.lasers:
                laser.update()
        
        if self.loadRadius < 10.00:
            self.loadRadius += 0.05
        if self.damageTime < 50:
            self.damageTime += 1
            
        stroke(randint(self.bgcolor[0]-50,self.bgcolor[0]+50),
            randint(self.bgcolor[1]-50,self.bgcolor[1]+50),
            randint(self.bgcolor[2]-50,self.bgcolor[2]+50))
        ellipse(self.x,self.y,self.radius,self.radius)
        
        self.drawLines()
        self.dispVitals()
        
        
#DRAW LINES
    def drawLines(self):
        stroke(120,255,120)
        ellipse(self.x,self.y,self.loadRadius,self.loadRadius)
        
        stroke(randint(self.bgcolor[0]-50,self.bgcolor[0]+50),
               randint(self.bgcolor[1]-50,self.bgcolor[1]+50),
               randint(self.bgcolor[2]-50,self.bgcolor[2]+50))
        strokeWeight(4)
        
        #Right
        line(self.x+self.radius*(cos(self.laserAngle)),
             self.y+self.radius*sin(self.laserAngle), 
             self.x+((self.radius+10)*cos(self.laserAngle)),
             self.y+((self.radius+10)*sin(self.laserAngle)))
        #Bottom
        line(self.x+self.radius*(cos(self.laserAngle+((3.0*PI)/2.0))),
             self.y+self.radius*sin(self.laserAngle+((3.0*PI)/2.0)), 
             self.x+((self.radius+10)*cos(self.laserAngle+((3.0*PI)/2.0))),
             self.y+((self.radius+10)*sin(self.laserAngle+((3.0*PI)/2.0))))
        #Left
        line(self.x+self.radius*(cos(self.laserAngle+PI)),
             self.y+self.radius*sin(self.laserAngle+PI), 
             self.x+((self.radius+10)*cos(self.laserAngle+PI)),
             self.y+((self.radius+10)*sin(self.laserAngle+PI)))
        #Top
        line(self.x+self.radius*(cos(self.laserAngle+(PI/2))),
             self.y+self.radius*sin(self.laserAngle+(PI/2)), 
             self.x+((self.radius+10)*cos(self.laserAngle+(PI/2))),
             self.y+((self.radius+10)*sin(self.laserAngle+(PI/2))))
        strokeWeight(3)
        
#FIREIN' MAH LAZERS
    def fireLasers(self):
        angleList = (0,PI/2,PI,(3*PI)/2)
        self.lasers = []
        
        for i in range(4):
            self.lasers.append(Laser(self.x,self.y,self.radius,self.laserAngle+angleList[i]))
    
    def dispVitals(self):
        textSize(30)
        fill(200,120,120)
        s = (u"\u2665")
        if self.health >= 10:
            text(s,35,45)
        if self.health >= 20:
            text(s,60,45)
        if self.health >= 30:
            text(s,85,45)
        if self.health >= 40:
            text(s,115,45)
        if self.health >= 50:
            text(s,140,45)
        if self.health >= 60:
            text(s,165,45)
        if self.health >= 70:
            text(s,190,45)
        if self.health >= 80:
            text(s,215,45)
        if self.health >= 90:
            text(s,240,45)
        if self.health >= 100:
            text(s,265,45)
        
        fill(220)
        
        text(str(self.score),width-85,45)
        
        noFill()
        
    def damage(self):
        if self.damageTime == 50:
            self.health -= random(7.0,15.0)
            self.loadRadius = 0.0
            self.damageTime = 0
        
