from random import randint

def setup():
    size(600, 600)
    background(0)
    global balls
    
    # Create 50 Ball instances with random coordinates and velocities using list comprehension
    balls = [Ball(randint(100, 500), randint(100, 500), randint(-5, 5), randint(-5, 5)) for _ in range(100)]

class Ball:
    def __init__(self, x, y, xd, yd):
        self.x = x
        self.y = y
        self.xd = xd
        self.yd = yd
        
    def create(self):
        circle(self.x, self.y, 30)
        
    def move(self):
        if self.x < 0 or self.x > width:
            self.xd *= -1
        self.x += self.xd
        
        if self.y < 0 or self.y > height:
            self.yd *= -1    
        self.y += self.yd 

def draw():
    global balls
    background(0)
    

    for ball in balls:
        fill(randint(0,255),randint(0,255),randint(0,255))
        ball.create()
        ball.move()
