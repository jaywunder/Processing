from random import randint

VELOCITYMAX = 7
class Attacker(object):
    def __init__(self,radius,defender,x,y,bgcolor,othersList=None):
        self.radius = radius
        self.defender = defender
        self.x = x
        self.y = y
        self.bgcolor = bgcolor
        self.othersList = othersList
        if othersList != None:
            self.othersList.append(self.defender)
        
        self.vx = 0
        self.vy = .5
        self.accl = .2
        self.spring = .9
        self.friction = .6
    
    def update(self):
        self.defy = self.defender.y
        self.defx = self.defender.x
        stroke(randint(self.bgcolor[0]-50,self.bgcolor[0]+50),
               randint(self.bgcolor[1]-50,self.bgcolor[1]+50),
               randint(self.bgcolor[2]-50,self.bgcolor[2]+50))
        
        self.x += self.vx
        self.y += self.vy
        
        if self.defender.x < self.x:
            self.vx -= self.accl 
        elif self.defender.x > self.x:
            self.vx += self.accl 
        if self.defender.y < self.y:
            self.vy -= self.accl 
        elif self.defender.y > self.y:
            self.vy += self.accl 
            
        #ellipse(self.x,self.y,self.radius,self.radius)
        triangle((self.x),(self.y)+(self.radius),
                (self.x)-(self.radius),(self.y)-(self.radius),
                (self.x)+(self.radius),(self.y)-(self.radius))
        
        if self.vx >= VELOCITYMAX:
            self.vx = VELOCITYMAX
        if self.vy >= VELOCITYMAX:
            self.vy = VELOCITYMAX
    
    def collide(self):
        dx = self.defender.x - self.x
        dy = self.defender.y - self.y
        minDist = self.defender.radius + self.radius
        if dist(self.defender.x, self.defender.y, self.x, self.y) < minDist:
            angle = atan2(dy, dx)
            
            targetX = self.x + cos(angle) * minDist
            targetY = self.y + sin(angle) * minDist
            
            ax = (targetX - self.defender.x) * self.spring
            ay = (targetY - self.defender.y) * self.spring
            self.vx -= ax
            self.vy -= ay
        
        for other in self.othersList:
            dx = other.x - self.x
            dy = other.y - self.y
            minDist = other.radius + self.radius
            if dist(other.x, other.y, self.x, self.y) < minDist:
                angle = atan2(dy, dx)
                
                targetX = self.x + cos(angle) * minDist
                targetY = self.y + sin(angle) * minDist
                
                ax = (targetX - other.x) * self.spring
                ay = (targetY - other.y) * self.spring
                self.vx -= ax
                self.vy -= ay
                other.vx += ax
                other.vy += ay

        for laser in self.defender.lasers:
            dx = laser.x0 - self.x
            dy = laser.y0 - self.y
            minDist = self.radius + 15
            if dist(laser.x0, laser.y0, self.x, self.y) < minDist:
                if self.othersList != None:
                    self.othersList.remove(self)
                
                
        if self.x + self.radius > width:
            self.x = width - self.radius
            self.vx *= self.friction
            #self.x = 0 + self.x
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= self.friction
            #self.x = width - self.x
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.vy *= self.friction
            #self.y = 0 +self.y
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= self.friction
            #self.y = height - self.y
    
        
