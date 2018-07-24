from turtle import *
speed(-1)
# for i in range(3,7)
n = 2
for i in range(4):
    n +=1
    numb = n%2
    if numb == 1:
        color("blue")
    else:
        color("red")
    for i in range (n):
        forward(100)
        left(360/n)
mainloop()
