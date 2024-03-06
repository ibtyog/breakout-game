from turtle import Turtle

class BlockManager():
    def __init__(self):
        self.block_list=[]

    def create_block(self):
        new_block = Turtle()
        new_block.shape('square')
        new_block.shapesize(1, 1.5)
        new_block.penup()
        new_block.color('red')
        new_block.goto(10,10)
        self.block_list.append(new_block)

    def set_blocks(self):
        for i in range(0,80):
            self.create_block()
            self.block_list[i].goto(-227 + 50*(i%10),(300 - 30*(i//10)))
            if (i // 10) % 2 == 0:
                self.block_list[i].color('orange')