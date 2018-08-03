map = {
    "size_x": 5,
    "size_y":5
}
player = {
    "x": 3,
    "y": 4
}

boxes = [
    {"x":1, "y":1},
    {"x":2, "y":2},
    {"x":3, "y":3}
]
for y in range (map["size_y"]):
    for x in range(map["size_x"]):
        box_is_here= False
        for box in boxes:
            if y == box["y"] and x == box["x"]:
                box_is_here = True

        if y == player["y"] and x == player ["x"]:
            print("P ",end ="")
        elif box_is_here == True:
            print("B ",end="")
        else:
            print("- ",end=(""))
    print("")
