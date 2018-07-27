from turtle import *
speed(-1)
colors = ["red","blue","brown","yellow","grey"]
for index,k in enumerate(colors,3):
    color(k)
    for i in range (index):
        forward(100)
        left(360/index)
mainloop()