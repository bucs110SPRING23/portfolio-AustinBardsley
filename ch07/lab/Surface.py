import rectangle

class Surface:
    def __init__(self,filename,x,y,h,w):
        self.rect = rectangle.Rectangle(x,y,h,w)
        self.image = str(filename)
    def getRect(self):
        return self.rect