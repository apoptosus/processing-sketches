class Leaf:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.reached = False
        
    def show(self):
        stroke(255,255,100)
        pushMatrix()
        translate(self.pos[0],self.pos[1],self.pos[2])
        sphere(1)
        popMatrix()
        
