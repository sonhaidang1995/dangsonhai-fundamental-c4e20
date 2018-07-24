from turtle import *
shape("turtle")
speed(-1)
length = 5
for i in range (80):
    forward(length)
    left(90)
    
    # length = length +5
    length +=10
mainloop()