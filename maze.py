from tkinter import *
myGui = Tk()

myGui.geometry("650x650+300+100")
myGui.title("Virtual Robot Simulator Game")

#creating the canvas
w = Canvas(myGui,height=600,width=600,bg="white")

w.create_rectangle(2,2,600,600)

#coordinates x1,y1,x2,y2
"""x axis coordinates"""
c1 = 60,600,60,0
c2 = 120,600,120,0
c3 = 180,600,180,0
c4 = 240,600,240,0
c5 = 300,600,300,0
c6 = 360,600,360,0
c7 = 420,600,420,0
c8 = 480,600,480,0
c9 = 540,600,540,0
x1 = w.create_line(c1)
x2 = w.create_line(c2)
x3 = w.create_line(c3)
x4 = w.create_line(c4)
x5 = w.create_line(c5)
x6 = w.create_line(c6)
x7 = w.create_line(c7)
x8 = w.create_line(c8)
x9 = w.create_line(c9)
"""y axis coordinates"""
a1 = 0,60,600,60
a2 = 0,120,600,120
a3 = 0,180,600,180
a4 = 0,240,600,240
a5 = 0,300,600,300
a6 = 0,360,600,360
a7 = 0,420,600,420
a8 = 0,480,600,480
a9 = 0,540,600,540
y1 = w.create_line(a1)
y2 = w.create_line(a2)
y3 = w.create_line(a3)
y4 = w.create_line(a4)
y5 = w.create_line(a5)
y6 = w.create_line(a6)
y7 = w.create_line(a7)
y8 = w.create_line(a8)
y9 = w.create_line(a9)
w.pack()
