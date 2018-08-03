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

destination = [
    {"x": 2, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3}
]

playing = True
while playing:
################# Print map
    for y in range (map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            if y == player ["y"] and x == player ["x"]:
                player_is_here = True       
            box_is_here= False
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True
            destination_is_here = False
            for des in destination:
                if y == des["y"] and x == des["x"]:
                    destination_is_here = True
            if player_is_here:
                print("P ",end="")
            elif box_is_here:
                print("B ",end="")
            elif destination_is_here:
                print("D ",end="")
            else:
                print("- ",end=(""))
        print("")
    ################# Choi game nao
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win:
        print("You win!!!")
        break
    move = input("Your move: ").upper()
    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False
    
    if 0 <= player["x"] + dx <= map["size_x"] and \
       0 <= player["y"]+ dy <= map["size_y"]:
            player["x"] += dx
            player["y"] += dy
    for box1 in boxes:
        if player["x"] == box1["x"] and player["y"]== box1["y"]:
            box1["x"]+=dx
            box1["y"]+=dy
# Lam 1 bien dem so box trung destination, khi bien dem = 3 thi win

