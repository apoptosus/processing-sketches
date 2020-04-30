class Branch:
    def __init__(self, parent, pos, dir, grow_width):
        self.parent = parent
        self.pos = pos
        self.dir = dir
        self.num_closest = 0
        self.og_dir = None
        self.grow_length = 3
        self.grow_width = 8

        
    def grow_branch(self):
        self.grow_width *= .9
        next_pos = PVector.add(self.pos, self.dir * self.grow_length)
        next_branch = Branch(self.pos, next_pos, self.dir.copy(), self.grow_width)
        line(next_branch.parent[0], next_branch.parent[1], next_branch.parent[2], 
             next_branch.pos[0], next_branch.pos[1], next_branch.pos[2])
    

        return next_branch
    
    def show(self):
        if self.parent != None:
            stroke(255)
            strokeWeight(self.grow_width)
            line(self.parent[0], self.parent[1], self.parent[2], self.pos[0], self.pos[1], self.pos[2])
    
    def reset(self):
        self.dir = PVector(0,-1,0)
        self.num_closest = 0
