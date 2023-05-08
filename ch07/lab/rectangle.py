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
        """returns a string of form x: x value y:y value, height: height value, width: width value
        args: self
        return: str
        """
        return ("x: "+str(self.x)+" , "+"y: "+str(self.y)+" , "+"height: "+str(self.height)+" , "+"width: "+str(self.width))
        