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
    print(len(give_tuple))
    for indx in range(len(give_tuple)):
            if value!=give_tuple[indx]:
                    t2=t2+(give_tuple[indx],)
    return(t2)

#---------------------            
#---SCRIPT BODY-------

'''Bonus creation and allocation on the arena'''
#-Library of bonuses--
bonuses=dict()
bonuses['1p']=()    #Gives 1 point to a robot      
bonuses['2p']=()    #Gives 2 points to a robot
bonuses['3p']=()    #Gives 3 points to a robot
bonuses['sp']=()    #Increments the speed of a robot

#Algorithm for coordinate placement into dictionary's tuples with random keys
#The coordinates are used to find the middle of a cell and place there a coin with bonus
for x in range(30,630,60):
    for y in range(30,630,60):
        rand_key=random.choice(list(bonuses.keys()))
        xy=(x,y)
        bonuses[rand_key]=bonuses[rand_key]+(xy,)
        
yellow_circle = []
red_circle = []
blue_circle = []

#Allocating the coins on the arena  
for i in range(len(bonuses['1p'])):
    x,y=bonuses['1p'][i]
    yellow_circle.append(canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='yellow'))
for i in range(len(bonuses['2p'])):
    x,y=bonuses['2p'][i]
    red_circle.append(canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='red'))
for i in range(len(bonuses['3p'])):
    x,y=bonuses['3p'][i]
    blue_circle.append(canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='blue'))
for i in range(len(bonuses['sp'])):
    x,y=bonuses['sp'][i]
    canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='green')

'''Movement of robots starts here'''

# The velocity, or distance moved per time step
vx = 60.0 # x velocity
vy = 0.0 # y velocity


# Boundaries
x_min = 10
y_min = 10
x_max = 590
y_max = 590

#Robots
robot_1=canvas.create_rectangle(10,10,50,50)
robot1_points = 0
#robot_2=canvas.create_rectangle(550,550,590,590)


while True:
    x1,y1,x2,y2=canvas.coords(robot_1)

    x = x1 + 20 # Finding the middle of X coordinatee for ther robot with dimension 40x40
    y = y1 + 20 # Finding the middle of Y coordinatee for ther robot with dimension 40x40
    xy = x , y # Creating a tuple of values to compare with elements in dictionary of bonuses (Dictionary of bonuses only contains middle coordinates)
    
    if xy in bonuses['1p']:
        bonuses['1p']=pop_from_tuple(xy,bonuses['1p']) #Function to remove the found element
        
        #Finding the widget with corresponding coordinates
        for i in range(len(bonuses['1p'])): 
            xx, yy, c1, c2 = canvas.coords(yellow_circle[i])
            
            if x - 5 == xx and y - 5 == yy: 
                print('Bonus + 1p')

                #Remove it when found
                canvas.delete(yellow_circle[i]) 
                yellow_circle.remove(yellow_circle[i]) 
                
                robot1_points += 1
                break
        

#Make the robot change direction randomly with possibility 1/5
    RandomVal=random.randint(1,5)
    if RandomVal == 5:
        RandomVal1 = random.randint(1,4)
        if RandomVal1 == 1 and x1 != x_min: # Left
            print('Left')
            vx -= 60
            vy = 0
            
        elif RandomVal1 == 2 and x2 != x_max: # Right
            print('Right')
            vx += 60
            vy = 0
            
        elif RandomVal1 == 3 and y1 != y_min: # Up
            print('Up')
            vy -= 60
            vx = 0
            
        elif RandomVal1 == 4 and y2 != y_max: # Down
            print('Down')
            vy += 60
            vx = 0
        else:
            print('The random turn points to the edge, therefore skipped')
            
        time.sleep(0.5)           
        # Reposition the robot      
        canvas.coords(robot_1,x1+vx,y1+vy,x2+vx,y2+vy)
        canvas.update()
        continue

# If a boundary has been approached, make turn
    if x2 == x_max and vx == 60:
        vy = 60
        vx = 0
    if y2 == y_max and vy == 60:
        vy = 0
        vx = -60
    if x1 == x_min and vx == -60:
        vy = -60
        vx = 0
    if y1 == y_min and ( vy == -60):
        vy = 0
        vx = 60

        # Reposition the robot      
    canvas.coords(robot_1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
        # Pause for 0.1 seconds, then delete the image
    time.sleep(0.5)

