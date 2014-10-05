ACCLMAX = 1.5
class Attacker(object):
    def __init__(self,radius,defender,x,y,bgcolor):
        self.radius = radius
        self.defender = defender
        self.x = x
        self.y = y
        self.bgcolor = bgcolor
        
        self.vx = 0
        self.vy = .5
        self.accl = .5
        self.spring = 1
        self.friction = .3
        
    def update(self):
        self.dy = self.defender.y
        self.dx = self.defender.x
        fill(self.bgcolor[0],self.bgcolor[1],self.bgcolor[2])
        
        self.x += self.vx
        self.y += self.vy
        
        if self.defender.x < self.x and self.accl <= ACCLMAX:
            self.vx -= self.accl 
            #/ (self.dx - self.x)
        elif self.defender.x > self.x and self.accl <= ACCLMAX:
            self.vx += self.accl 
            #/ (self.x - self.dx)
        if self.defender.y < self.y and self.accl <= ACCLMAX:
            self.vy -= self.accl 
            #/ (self.y - self.dy)
        elif self.defender.y > self.y and self.accl <= ACCLMAX:
            self.vy += self.accl 
            #/ (self.dy - self.y)
        
        ellipse(self.x,self.y,self.radius,self.radius)
    
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
            
        if self.x + self.radius > width:
            self.x = width - self.radius
            self.vx *= self.friction #WAS *=
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= self.friction #WAS *=
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.vy *= self.friction
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= self.friction
    
        
