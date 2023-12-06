def setup():
    size(600, 600)
    background(0)
    global x,y
    x=0
    y=0
    
def draw():
    global x,y
    while x<300:
        while y<300:
            circle(x,y,50)
            y+=200
        x+=200
