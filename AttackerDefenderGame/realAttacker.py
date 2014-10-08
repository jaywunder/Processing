from random import randint

VELOCITYMAX = 9
class Attacker(object):
    def __init__(self,radius,defender,x,y,bgcolor,othersList=None):
        self.radius = radius
        self.defender = defender
        self.x = x
        self.y = y
        self.bgcolor = bgcolor
        self.othersList = []
        
        self.vx = 0
        self.vy = .5
        self.spring = 1
        self.friction = .6
        self.ax = 0.05
        self.ay = 0.05
        self.thrust = 0.9
        
    def orientAccl(self, thrust):
        if self.defender.x - self.x == 0 and self.defender.y - self.y < 0:
            theta = 90
        elif self.defender.x - self.x == 0 and self.defender.y - self.y > 0:
            theta = -90
        else:
            theta = atan((self.defender.y-self.y)/(self.defender.x-self.x))
            if self.defender.x - self.x < 0:
                theta += PI
        
        ay = thrust*sin(theta)
        ax = thrust*cos(theta)
        return (ax,ay)
        
    def update(self):
        self.defy = self.defender.y
        self.defx = self.defender.x
        stroke(randint(self.bgcolor[0]-50,self.bgcolor[0]+50),
               randint(self.bgcolor[1]-50,self.bgcolor[1]+50),
               randint(self.bgcolor[2]-50,self.bgcolor[2]+50))
        
        self.oldSpeed = sqrt((self.vx**2) + (self.vy**2))
        
        self.ax,self.ay = self.orientAccl(self.thrust)
        
        
        self.vx += self.ax
        self.vy += self.ay
        
        if abs(self.vx) > VELOCITYMAX:
            if (self.vx > 0):
                self.vx = VELOCITYMAX
            else:
                self.vx = -VELOCITYMAX
        if abs(self.vy) > VELOCITYMAX:
            if (self.vy > 0):
                self.vy = VELOCITYMAX
            else:
                self.vy = -VELOCITYMAX    
        
        self.x += self.vx
        self.y += self.vy
        
        
        #
        #self.accl += .9
        #self.accl *= (1 - self.oldSpeed/VELOCITYMAX)
        
        #if self.defender.x < self.x:
        #    self.vx -= self.ax 
        #elif self.defender.x > self.x:
        #    self.vx += self.ax 
        #if self.defender.y < self.y:
        #    self.vy -= self.ay 
        #elif self.defender.y > self.y:
        #    self.vy += self.ay 
        self.newSpeed = sqrt((self.vx**2) + (self.vy**2))
        
        
        #ellipse(self.x,self.y,self.radius,self.radius)
        triangle((self.x),(self.y)+(self.radius),
                (self.x)-(self.radius),(self.y)-(self.radius),
                (self.x)+(self.radius),(self.y)-(self.radius))
        
        if self.vx > VELOCITYMAX:
            self.vx = VELOCITYMAX
        if self.vy > VELOCITYMAX:
            self.vy = VELOCITYMAX
    
    def collide(self):
        #for other in self.otherList:
        other = self.defender
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
            
        if self.x + self.radius > width:
            #self.x = width - self.radius
            self.x = 0 + self.x
            #self.vx *= self.friction #WAS *=
        elif self.x - self.radius < 0:
            #self.x = self.radius
            self.x = width - self.x
            #self.vx *= self.friction #WAS *=
        if self.y + self.radius > height:
            #self.y = height - self.radius
            self.y = 0 +self.y
            #self.vy *= self.friction
        elif self.y - self.radius < 0:
            #self.y = self.radius
            self.y = height - self.y
            #self.vy *= self.friction
    
        
