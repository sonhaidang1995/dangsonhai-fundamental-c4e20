# from turtle import *
# speed(-1)
# color("green")
# times = int(input("Times?"))
# for i in range(times):
#     circle(90)
#     left(360/times)
# mainloop()

from turtle import *
speed(-1)
color("green")
degree = int(input("Degree?"))
for i in range(int(360/degree)):
    circle(90)
    left(degree)
mainloop()