class Defender(object):
    def __init__(self,radius,x,y,bgcolor):
        self.radius = radius
        self.x = x
        self.y = y
        self.bgcolor = bgcolor
        
    def update(self):
        fill(self.bgcolor[0],self.bgcolor[1],self.bgcolor[2])
        self.x = mouseX
        self.y = mouseY
        ellipse(self.x,self.y,self.radius,self.radius)
        
