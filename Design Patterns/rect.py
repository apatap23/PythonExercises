class Rectangle():
    def __init__(self, canvas):
        self.canvas = canvas #copy canvas ref
    
    def draw(self, x,y, w, h): #draw the rect
        #canvas rectangle uses x1,y1, x2,y2
        self.canvas.create_rectangle(x,y, x+w, y+h)


class Square(Rectangle):
    def __init__(self, canvas):
        super().__init__(canvas)
    
    