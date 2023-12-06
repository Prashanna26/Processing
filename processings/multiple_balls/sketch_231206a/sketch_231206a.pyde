#PROCESSING-------------------------------------------------------------------
#Q1. 

# from random import randint\
# def setup():
#     size(600, 600)
#     background(0)
#     global balls
#     balls = [Ball(randint(100, 500), randint(100, 500), randint(-5, 5), randint(-5, 5)) for _ in range(100)]
# class Ball:
#     def __init__(self, x, y, xd, yd):
#         self.x = x
#         self.y = y
#         self.xd = xd
#         self.yd = yd
#     def create(self):
#         circle(self.x, self.y, 30)
#     def move(self):
#         if self.x < 0 or self.x > width:
#             self.xd *= -1
#         self.x += self.xd
#         if self.y < 0 or self.y > height:
#             self.yd *= -1    
#         self.y += self.yd 
# def draw():
#     global balls
#     background(0)
#     for ball in balls:
#         fill(randint(0,255),randint(0,255),randint(0,255))
#         ball.create()
#         ball.move()

#Q2. 3x3 Balls
# def setup():
#     size(600, 600)
#     background(0)
#     global x,y
#     x=25
#     y=25 
# def draw():
#     global x,y
#     i=0
#     j=0
#     for i in range(3):
#         x=25    
#         for j in range(3):
#             circle(x,y,50)
#             x +=275
#         y +=275
#


#Q3. 3x3 upper triangle
# def setup():
#     size(600, 600)
#     background(0)
#     global x,y
#     x=25
#     y=25
    
    
# def draw():
#     global x,y
#     i= 0
#     while i<3:
#         x=25
#         j=i
#         while j<3:
#             circle (x,y, 50)
#             x+=275
#             j+=1
#         i+=1
#         y+=275

#Q4. 3x3 lower right angle triangle from left
# def setup():
#     size(600, 600)
#     background(0)
#     global x,y
#     x=25
#     y=25
    
    
# def draw():
#     global x,y
#     for i in range(3):
#         y=x
#         for j in range(3):
#             circle(x,y,50)
#             y+=275
#         x+=275

#Q5. 3x3 lower right angle triangle from right
# def setup():
#     size(600, 600)
#     background(0)
#     global x,y
#     x=25
#     y=25
    
    
# def draw():
#     global x,y
#     i= 0
#     while i<3:
#         x=y
#         j=0
#         while j<3:
#             circle (x,y, 50)
#             x+=275
#             j+=1
#         i+=1
#         y+=275

# Q6. SnowFlakes animation
# snowflake = []
# class Snowflakes:
#     def __init__(self, x, y, sizes, speed):
#         self.x = x
#         self.y = y
#         self.sizes = sizes
#         self.speed = speed
        
#     def update(self):
#         self.y += self.speed
#         gravity = 0.01
#         self.speed  += gravity 
        
#         if self.y > height:
#             self.y = random(-200,-100)
#             self.speed = random(1,15)
        
#     def display(self):
#         noStroke()
#         fill(255)
#         ellipse(self.x,self.y,self.sizes,self.speed)
        
# def setup():
#     size(600,600)
#     for i in range(100):
#         snowflake.append(Snowflakes(random(width),random(-200,-100),random(1, 5),random(1,15)))
    
# def draw():
#     background(0)
#     for flakes in snowflake:
#         flakes.display()
#         flakes.update()

            
            
