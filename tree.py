import random
import time

from leaf import Leaf
from branch import Branch
# from branch import Branch

class Tree:
    def __init__(self, species):
        self.species = species
        self.leaves = []
        self.branches = []
        self.generate_leaves()
        self.max_distance = 100
        self.min_distance = 5
        self.start = PVector(300,600,300)
    
    def generate_leaves(self):
        [self.leaves.append(Leaf(PVector(random.randint(0, 700), random.randint(
            0, 300), random.randint(0, 600)), 'sun')) for i in range(400)]
    
    def show(self):
        for leaf in self.leaves:
            leaf.show()
            
        for branch in self.branches:
            branch.show()
            
    def growth_start(self):
        # Grow the shoot apical meristem until it is w/in sensing distance of a leaf
        found = False
        sam = Branch(None, self.start, PVector(0,0,0,), 10)
        self.branches.append(sam)
        while not found:
            for leaf in self.leaves:
                d = leaf.pos.dist(sam.pos)
                if d < self.max_distance:
                    found = True
                  
            """  
            # This chunk finds normalized vectors of all leaves to determine growth dir, very SLOW
            if not found:
                print('nf')
                vsum = PVector(0,0,0)
                for leaf in self.leaves:
                    print(leaf.pos - sam.pos)
                    vsum += leaf.pos - sam.pos
        
                vsum.normalize()
                print("vsum : {}".format(vsum))

                sam.dir = vsum
                sam = sam.grow_branch()
                """
           # delete this if statement if you want above code instead 
            if not found:
                sam.dir = PVector(0, -1, 0)
                sam = sam.grow_branch()
        sam.parent = self.start
        self.branches.append(sam)
        
        for branch in self.branches:
            branch.reset()
            
            
    def grow(self):
        # look for closest branch to leaf
        for leaf in self.leaves:
            closest_branch = None
            lowest_d = self.max_distance
            
            for branch in self.branches:
                d = leaf.pos.dist(branch.pos)
                
                if d < self.min_distance:
                    leaf.reached = True
                    closest_branch = None
                    break
                
                elif d < lowest_d:
                    closest_branch = branch
                    lowest_d = d
            
            # add vector to closest branch
            if closest_branch is not None:
                new_dir = leaf.pos - closest_branch.pos
                new_dir.normalize()
                
                # add new direction to existing direction (creative choice)
                closest_branch.dir.add(new_dir)
                closest_branch.num_closest += 1
                
        # make new leaves
        for branch in self.branches:
            if branch.num_closest > 0:
                branch.dir /= branch.num_closest
                branch.num_closest = 0
                
                new_branch = branch.grow_branch()
                new_branch.reset()
                self.branches.append(new_branch)
            
        # delete reached leaves
        self.leaves = [leaf for leaf in self.leaves if leaf.reached is False]
            
                
                    
        
