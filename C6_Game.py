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


#---Function to create a new tuple without a certain object,
#---will be needed in order for a robot to  collect coins.
#---When a robot enters the cell with coordinates X,Y, the
#---corresponding element of the tuple will be removed and
#---the robot will obtain the appropriate bonus.
def pop_from_tuple(value,give_tuple):
    t2=tuple()
    for indx in range(len(give_tuple)):
            if value!=give_tuple[indx]:
                    t2=t2+(give_tuple[indx],)
    return(t2)

#---------------------            
#---SCRIPT BODY-------

'''Bonus creation and allocation on the arena'''

#-Library of bonuses, values will be tuples with tuples of X,Y coordinates where the bonus is located on the arena--
bonuses=dict()
bonuses['1p']=()    #Key for the tuple containing 1 point bonus coordinates      
bonuses['2p']=()    #Key for the tuple containing 2 point bonus coordinates 
bonuses['3p']=()    #Key for the tuple containing 3 point bonus coordinates 
bonuses['sp']=()    #Key for the tuple containing speed incrementation bonus coordinates 

#Algorithm for bonus coordinate insertion into dictionary's tuples with random keys

for x in range(30,630,60):
    for y in range(30,630,60):
        rand_key=random.choice(list(bonuses.keys()))
        xy=(x,y)
        bonuses[rand_key]=bonuses[rand_key]+(xy,)


#Arrays that will comprise oval objects to track their location and remove from canvas
yellow_circle = []
red_circle = []
blue_circle = []
green_circle = []

# Creating oval objects on the canvas based on their coordinates from the dictionary and assigning them to variables 
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
    green_circle.append(canvas.create_oval(x-5, y-5, x+5, y+5, width=1, fill='green'))

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

r1_speedy_steps = 0 # Counter for remaining steps with reduced freeze time
timr = 0.5 #Default freeze time

while robot1_points < 75:
    
    x1,y1,x2,y2=canvas.coords(robot_1)
    
    x = x1 + 20 # Finding the middle of X coordinatee for ther robot with dimension 40x40
    y = y1 + 20 # Finding the middle of Y coordinatee for ther robot with dimension 40x40
    xy = x , y # Creating a tuple of values to compare with elements in dictionary of bonuses (Dictionary of bonuses only contains middle coordinates)

    
    # Checking whether or not the robot's coordinates match with any record in the bonus dictionary
    if xy in bonuses['1p']:
        
        bonuses['1p']=pop_from_tuple(xy,bonuses['1p']) #Function to remove the found element
        
        #Finding the widget with corresponding coordinates
        for i in range(len(bonuses['1p'])+1): 
            xx, yy, c1, c2 = canvas.coords(yellow_circle[i])
            
            if x - 5 == xx and y - 5 == yy: #Checking the robot's middle coordinates with circle's ones

                #If match remove from the canvas and dictionary
                canvas.delete(yellow_circle[i]) 
                yellow_circle.remove(yellow_circle[i]) 
                
                robot1_points += 1
                break

    elif xy in bonuses['2p']:
        
        bonuses['2p'] = pop_from_tuple(xy,bonuses['2p'])
        
        for i in range(len(bonuses['2p'])+1): 
            xx, yy, c1, c2 = canvas.coords(red_circle[i])
            
            if x - 5 == xx and y - 5 == yy:

                canvas.delete(red_circle[i]) 
                red_circle.remove(red_circle[i]) 
                
                robot1_points += 2
                break

    elif xy in bonuses['3p']:
        
        bonuses['3p'] = pop_from_tuple(xy,bonuses['3p'])
        
        for i in range(len(bonuses['3p'])+1): 
            xx, yy, c1, c2 = canvas.coords(blue_circle[i])
            
            if x - 5 == xx and y - 5 == yy:

                canvas.delete(blue_circle[i]) 
                blue_circle.remove(blue_circle[i]) 
                
                robot1_points += 3
                break
            
    elif xy in bonuses['sp']:
        
        bonuses['sp']=pop_from_tuple(xy,bonuses['sp'])
        
        for i in range(len(bonuses['sp'])+1): 
            xx, yy, c1, c2 = canvas.coords(green_circle[i])
            
            if x - 5 == xx and y - 5 == yy:
 
                canvas.delete(green_circle[i]) 
                green_circle.remove(green_circle[i]) 
                
                timr = 0.25 # Reduce programm's freeze time
                r1_speedy_steps += 2 # Set the amount of steps with reduced freeze time
                break

        
        


#Make the robot change direction randomly with possibility 1/5
    RandomVal=random.randint(1,5)
    if RandomVal == 5:
        
        RandomVal = random.randint(1,4)
        if RandomVal == 1 and x1 != x_min: # Left
            vx = -60
            vy = 0
            
        elif RandomVal == 2 and x2 != x_max: # Right
            vx = 60
            vy = 0
            
        elif RandomVal == 3 and y1 != y_min: # Up
            vy = -60
            vx = 0
            
        elif RandomVal == 4 and y2 != y_max: # Down
            vy = 60
            vx = 0
            
        time.sleep(timr)

        # Reduce amount of remaining speedy steps after a move and
        # reset the timer to the default time when r1_speedy_steps == 0
        
        if r1_speedy_steps > 0:
            r1_speedy_steps -= 1

            if r1_speedy_steps == 0:
                timr = 0.5



            
        
        # Reposition the robot      
        canvas.coords(robot_1,x1+vx,y1+vy,x2+vx,y2+vy)
        canvas.update()
        #continue
        

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

        
    time.sleep(timr)

    #Dealing with speedy steps again
    if r1_speedy_steps > 0:
        r1_speedy_steps -= 1

        if r1_speedy_steps == 0:
            timr = 0.5

    # Reposition the robot        
    canvas.coords(robot_1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
        # Pause for 0.1 seconds, then delete the image
    
canvas.destroy()
print('The robot collected 75 points')
