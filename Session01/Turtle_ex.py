# from turtle import * 
# shape("turtle")
# color("blue")
# left(90)
# forward(100)
# mainloop()
n = int(input("so canh hinh la: "))
from turtle import *
speed(-1)
shape ("turtle")
color("blue")
# hinh 1
for i in range(n):
    forward(2)
    left(360/n)

mainloop()