from tkinter import *
import random
import re

#---Setting up GUI

window = Tk()
window.title('Maze')

#------- script canvas body -------#

block = 20
width = 31  #sets the maze grid to 30 x 30
height = 31
maze = [[1 for x in range(width)]for y in range(height)]

def Direction(x,y,necessity):
    direction = 15
    if y==1 or y-2<0 or (y-2>0 and maze[y-2][x]==necessity):
        direction-=8
    if y==height-2 or y+2>height or(y+2<height-1 and maze[y+2][x]==necessity):
        direction-=4
    if x==1 or x-2<0 or (x-2>0 and maze[y][x-2]==necessity):
        direction-=2
    if x==width-2  or x+2>width  or(x+2<width-1  and maze[y][x+2]==necessity):
        direction-=1
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



def pathFinder(x,y):

    up = maze[y+1][x]
    down = maze[y-1][x] #sets the movement for the algorithm
    left = maze[y][x+1]
    right = maze[y][x-1]

    if up == 4 or down == 4 or left == 4 or right == 4: #4 is the end goal
        return                                          #if the next space is 4, then the maze ends

    elif up == 0 or down == 0 or left == 0 or right == 0: maze[y][x]=2 #if the next space is 0, or empty, then it moves to that block
    else: maze[y][x]=3                                  #if that space has been moved over then a purple line is left behind


    if up == 0: pathFinder(x,y+1)       #the algorithm prioritizes up, left, down then right
    elif down == 0: pathFinder(x,y-1)   #it will move into the first empty space it finds
    elif left == 0: pathFinder(x+1,y)
    elif right == 0: pathFinder(x-1,y)


    elif up == 2:               #if no untravelled space is found, it will move onto a space it went over before
        pathFinder(x, y + 1)
    elif down == 2:
        pathFinder(x, y - 1)
    elif left == 2:
        pathFinder(x + 1, y)
    elif right == 2:
        pathFinder(x - 1, y)



maze[29][29] = 4    #sets the spawn location of the end goal
pathFinder(1,1)     #sets the spawn location for 

canvas = Canvas(window,width=width*block,height=height*block,bg="white")
canvas.pack(padx=10,pady=10)
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 4:
            maze[y][x] = canvas.create_rectangle(x * block, y * block, x * block + block,y * block + block,
                                                 fill='red', width=0)       #sets the end goal block to red
        elif maze[y][x] == 1:
            maze[y][x] = canvas.create_rectangle(x*block,y*block,x*block+block,y*block+block,
                                                 fill='black',width=0)      #sets the wall block to black
        elif maze[y][x] == 0:
            maze[y][x] = canvas.create_rectangle(x*block,y*block,x*block+block,y*block+block,
                                                 fill='gray',width=0)       #sets the empty space to gray
        elif maze[y][x] == 2:
            maze[y][x] = canvas.create_rectangle(x * block, y * block, x * block + block, y * block + block,
                                                 fill='blue', width=0)      #sets the travelled over path to blue
        elif maze[y][x] == 3:
            maze[y][x] = canvas.create_rectangle(x * block, y * block, x * block + block, y * block + block,
                                                 fill='purple', width=0)    #sets the travelled over twice path to purple
window.mainloop()



