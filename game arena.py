from tkinter import *
import random
import time

#---Setting up GUI, adjusting Tk window
#--------------------

window = Tk()

window.geometry("610x610")
window.configure(bg='grey')
window.title('Maze game')

canvas = Canvas(window, width=600, height=600, bg='white')
canvas.create_line(0,600,420,600)
canvas.create_line(480,600,601,600)
canvas.create_line(600,0,600,600)
canvas.create_line(2,0,2,600)
canvas.create_line(2,2,360,2)
canvas.create_line(420,2,600,2)
c1 = 360,60,360,240
c2 = 60,120,360,120
c3 = 60,60,60,120
c4 = 60,60,120,60
c5 = 180,0,180,60
c6 = 240,60,240,120
c7 = 300,0,300,60
c8 = 420,0,420,180
c9 = 360,180,480,180
c10 = 0,180,240,180
c11 = 240,180,240,480
c12 = 240,480,300,480
c13 = 300,480,300,180
c14 = 300,300,540,300
c15 = 420,240,420,300
c16 = 540,120,540,300
c17 = 480,120,540,120
c18 = 480,60,480,120
c19 = 540,60,600,60
c20 = 480,180,480,240
c21 = 540,360,600,360
c22 = 300,300,540,300
c23 = 480,300,480,360
c24 = 420,420,600,420
c25 = 420,360,420,480
c26 = 360,360,420,360
c27 = 360,360,360,420
c28 = 180,540,480,540
c29 = 180,420,180,540
c30 = 60,420,180,420
c31 = 60,360,60,420
c32 = 60,360,180,360
c33 = 180,180,180,300
c34 = 60,300,181,300
c35 = 0,240,60,240
c36 = 60,480,60,600
c37 = 60,480,120,480
c38 = 120,480,120,540
c39 = 360,480,360,540
c40 = 480,480,480,600
c41 = 540,480,540,600
x1 = canvas.create_line(c1)
x2 = canvas.create_line(c2)
x3 = canvas.create_line(c3)
x4 = canvas.create_line(c4)
x5 = canvas.create_line(c5)
x6 = canvas.create_line(c6)
x7 = canvas.create_line(c7)
x8 = canvas.create_line(c8)
x9 = canvas.create_line(c9)
x10 = canvas.create_line(c10)
x11 = canvas.create_line(c11)
x12 = canvas.create_line(c12)
x13 = canvas.create_line(c13)
x14 = canvas.create_line(c14)
x15 = canvas.create_line(c15)
x16 = canvas.create_line(c16)
x17 = canvas.create_line(c17)
x18 = canvas.create_line(c18)
x19 = canvas.create_line(c19)
x20 = canvas.create_line(c20)
x21 = canvas.create_line(c21)
x22 = canvas.create_line(c22)
x23 = canvas.create_line(c23)
x24 = canvas.create_line(c24)
x25 = canvas.create_line(c25)
x26 = canvas.create_line(c26)
x27 = canvas.create_line(c27)
x28 = canvas.create_line(c28)
x29 = canvas.create_line(c29)
x30 = canvas.create_line(c30)
x31 = canvas.create_line(c31)
x32 = canvas.create_line(c32)
x33 = canvas.create_line(c33)
x34 = canvas.create_line(c34)
x35 = canvas.create_line(c35)
x36 = canvas.create_line(c36)
x37 = canvas.create_line(c37)
x38 = canvas.create_line(c38)
x39 = canvas.create_line(c39)
x40 = canvas.create_line(c40)
x41 = canvas.create_line(c41)
canvas.pack(padx=10,pady=10)

#---------------------
#---Functions---------

#---Function to obtain the colour of a pixel(From StackOwerflow)
def get_pixel_color(canvas, x, y):
    ids = canvas.find_overlapping(x, y, x, y)

    if len(ids) > 0:
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        color = color.upper()
        print(index)
        if color != '':
            return color.upper()
'''Helper funtcions from (http://stackoverflow.com/questions/28014347/get-pixel
#-colors-of-tkinter-canvas)'''


#---Function to create a new tuple without a certain object,
#---will be needed in order for a robot to  collect coins.
#---When a robot enters the cell with coordinates X,Y, the
#---corresponding element of the tuple will be removed and
#---the robot will obtain the appropriate bonus.
def pop_from_tuple(value,give_tuple):
    t2=tuple()
    for i in range(len(give_tuple)):
            if value!=give_tuple[i]:
                    t2=t2+(t[i],)
    return(t2)

#---------------------            
#---SCRIPT BODY-------

#-Library of bonuses--
bonuses=dict()
bonuses['1p']=()    #Gives 1 point to a robot      
bonuses['2p']=()    #Gives 2 points to a robot
bonuses['3p']=()    #Gives 3 points to a robot
bonuses['sp']=()    #Increments the speed of a robot

ij=tuple

#Algorithm for coordinate placement into dictionary's tuples with random keys
#The coordinates are used to find the middle of a cell and place there a coin with bonus
for x in range(30,630,60):
    for y in range(30,630,60):
        rand_key=random.choice(list(bonuses.keys()))
        xy=(x,y)
        bonuses[rand_key]=bonuses[rand_key]+(xy,)

#Allocating the coins on the arena  
for i in range(len(bonuses['1p'])):
    x,y=bonuses['1p'][i]
    canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='yellow')
for i in range(len(bonuses['2p'])):
    x,y=bonuses['2p'][i]
    canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='red')
for i in range(len(bonuses['3p'])):
    x,y=bonuses['3p'][i]
    canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='blue')
for i in range(len(bonuses['sp'])):
    x,y=bonuses['sp'][i]
    canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='green') 
