from tkinter import *
import time
import random

#---Setting up GUI, adjusting Tk window
#--------------------


window = Tk()

window.title('Escape The Maze')

#------- script canvas body -------#

block = 20
width = 31
height = 31
maze = [[1 for x in range(width)]for y in range(height)]



def Direction(x,y,necessity):
    direction = 15
    if y==1 or y-2<0 or (y-2>0 and maze[y-2][x]==necessity): direction-=8
    if y==height-2 or y+2>height or(y+2<height-1 and maze[y+2][x]==necessity): direction-=4
    if x==1 or x-2<0 or (x-2>0 and maze[y][x-2]==necessity): direction-=2
    if x==width-2  or x+2>width  or(x+2<width-1  and maze[y][x+2]==necessity): direction-=1
    if direction != 0:
        direction = bin(direction)[2:].zfill(4)
        choices = []
        for m in re.finditer('1', direction): choices.append(m.start())
        direction = random.choice(choices)
    else:
        direction=-1
        Random()
    return direction

def Random():
    choices = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if x%2==1 and y%2==1 and maze[y][x]==1:
                choices.append((x,y))
    if len(choices)>0:
        cell = random.choice(choices)
        x = cell[0]
        y = cell[1]
        direction = Direction(x,y,1)
        if direction != -1:
            if direction == 0: maze[y-1][x]=0
            if direction == 1: maze[y+1][x]=0
            if direction == 2: maze[y][x-1]=0
            if direction == 3: maze[y][x+1]=0
            Next(x,y)

def Next(x,y):
    maze[y][x]=0
    direction = Direction(x,y,0)
    if direction!=-1:
        ydir = 0
        xdir = 0
        if direction == 0: ydir=-1
        if direction == 1: ydir=1
        if direction == 2: xdir=-1
        if direction == 3: xdir=1
        maze[y+ydir][x+xdir]=0
        maze[y+ydir*2][x+xdir*2]=0
        Next(x+xdir*2,y+ydir*2)



Next(1,1)




canvas = Canvas(window,width=width*block,height=height*block,bg="white")
canvas.pack(padx=10,pady=10)
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 1: maze[y][x] = canvas.create_rectangle(x*block,y*block,x*block+block,y*block+block,fill='black',width=0)
        elif maze[y][x] == 0: maze[y][x] = canvas.create_rectangle(x*block,y*block,x*block+block,y*block+block,fill='gold',width=0)
window.mainloop()


