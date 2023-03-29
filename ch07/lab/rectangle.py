class Rectangle:
    def __init__(self, x,y,h,w):
        x=abs(x)
        y=abs(y)
        h=abs(h)
        w=abs(w)
        self.x = x
        self.y = y
        self.height = h
        self.width = w
    def __str__(self):
        return str("x: "+x+" ,"+"y: "+y+" ,"+"height: "+h+" ,"+"width: "+w)
        
