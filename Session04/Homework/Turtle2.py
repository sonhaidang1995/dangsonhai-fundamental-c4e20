from turtle import *
speed(-1)
color("blue")
n = 50
k = 0
for i in range(n):
    k += 100/n
    for z in range (4):
        forward(k)
        left(90)
    left(500/n)
exitonclick()
mainloop()