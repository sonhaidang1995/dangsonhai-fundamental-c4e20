map = {
    "size_x": 5,
    "size_y": 5,
}

player = {
    "x": 3,
    "y": 4
}

boxes = [
    { "x": 1, "y": 1 },
    { "x": 2, "y": 2 },
    { "x": 3, "y": 3 }
]

destis = [
    { "x": 2, "y": 1 },
    { "x": 3, "y": 2 },
    { "x": 4, "y": 3 }
]
playing = True
while playing:
    
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            if y == player["y"] and x == player["x"]:
                player_is_here = True
            
            box_is_here = False
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True
            
            destis_is_here = False
            for des in destis:
                if y == des["y"] and x == des["x"]:
                    destis_is_here = True

            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B", end=" ")
            elif destis_is_here:
                print("D", end=" ")
            else:
                print("-", end=" ")
        print()

    win = True
    for box in boxes:
        if box not in destis:
            win = False
    if win:
        print("victory")
        break
    
    move = input("Your move: ").upper()
    dx = 0
    dy = 0

    if move == "A":
        dx = -1
    elif move == "W":
        dy = -1
    elif move == "D":
        dx = 1
    elif move == "S":
        dy = 1
    else:
        playing = False
    count = 0
    if 0 <= player["x"] + dx < map["size_x"] and 0 <= player["y"] + dy < map["size_y"]:
        player["x"] += dx
        player["y"] += dy
    for box in boxes:
        if 0 <= box["x"] + dx < map["size_x"] and 0 <= box["y"] + dy < map["size_y"]:
            if player["x"] == box["x"] and player["y"] == box["y"]:
                box["x"] += dx
                box["y"] += dy
            
#         for des in destis:
#             if box["x"] == des["x"] and box["y"] == des["y"]:
#                 count += 1
#         if count == 3:
#             playing = False
# print("Victory")