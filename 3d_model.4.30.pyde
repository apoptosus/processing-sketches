from tree import *
tree = Tree('test')
def setup():
    size(600, 600, P3D)
    tree.growth_start()
    
def draw():
    background(0)
    
    # camera(mouseX, height/2, (height/2) / tan(PI/6), width/2, height/2, 0, 0, 1, 0)
    # noFill()
    
    tree.show()
    tree.grow()
    camera(mouseX, mouseY, (height/2) / tan(PI/6), mouseY, height/2, 0, 0, 1, 0)

    for branch in tree.branches:
        print(branch)
    
    print('nect')
