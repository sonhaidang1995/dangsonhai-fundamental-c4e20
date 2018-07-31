from turtle import *
speed (-1)
color("blue")
n = 20
for k in range (n):
    for i in range(4):
        forward(100)
        left(90)
    left(360/n)
exitonclick()
mainloop()