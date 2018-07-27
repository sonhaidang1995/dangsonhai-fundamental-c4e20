from turtle import *
speed(-1)
colors = ["red","blue","brown","yellow","grey"]
for index, k in enumerate(colors,1):
    color(k)
    begin_fill()
    for i in range (2):
        forward(40)
        right(90)
        forward(100)
        right(90)
    end_fill()
    forward(40)
exitonclick()
mainloop()