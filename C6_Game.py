#---------------------
#---Libraries--------

from tkinter import *
import random
import time

#---Setting up GUI, adjusting Tk window
#--------------------

window = Tk()

window.title("Create a window")
window.geometry("610x610")
window.configure(bg='black')
window.title('Russian Spetsnaz')

canvas = Canvas(window, width=600, height=600, bg='white')
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


