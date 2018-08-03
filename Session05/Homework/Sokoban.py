map ={
    "x":6,
    "y":6
}
boxes =[
    {"x":0,"y":2},
    {"x":1,"y":2},
    {"x":2,"y":2},
    {"x":3,"y":2}
]
n =[
    {"x":0,"y":2},
    {"x":1,"y":2},
    {"x":2,"y":2},
    {"x":3,"y":2}
]
destination =[
    {"x":0,"y":3},
    {"x":0,"y":5},
    {"x":1,"y":4},
    {"x":3,"y":5},
]
obstacle = [
    {"x":1,"y":3},
    {"x":4,"y":5}
]
player = {"x":1,"y":1}
player1 = {"x":1,"y":1}
playing = True
from copy import *
p = deepcopy(player1)
b = deepcopy(n)
# b = deepcopy (play)
while playing:
    for y in range(map["y"]):
        for x in range(map["x"]):
            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True
            box_is_here = False
            for box in boxes:
                if x == box["x"] and y == box["y"]:
                    box_is_here = True
            destination_is_here = False
            for des in destination:
                if x == des["x"] and y == des["y"]:
                    destination_is_here = True
            obstacle_is_here = False
            for obs in obstacle:
                if x == obs["x"] and y == obs["y"]:
                    obstacle_is_here = True
            if player_is_here:
                print("P ",end="")
            elif box_is_here:
                print("B ",end="")
            elif destination_is_here:
                print("D ",end="")
            elif obstacle_is_here:
                print("O ",end="")
            else:
                print("- ",end="")
        print("")
# Check win:
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win == True:
        print("Congratuation!! You win!")
        break
# Vẽ map xong
    dx = 0
    dy = 0
    move = input("Your move: (W/S/D/A or Z to Undo)").upper()
    if move == "Z":
        player = p
        boxes = b
        n = k
        # Không hiểu đoạn này luôn =)))
    else:
        p = deepcopy(player)
        b = deepcopy(boxes)
        if move == "W":
            dy = -1
        elif move == "S":
            dy = 1
        elif move == "A":
            dx = -1
        elif move == "D":
            dx = +1
        else:
            print("bleeezzz")
# check không đi ra ngoài map
    if 0 <= player["x"] + dx <= map["x"]-1 and 0 <= player["y"] + dy <= map["y"]-1:
            player["x"] += dx
            player["y"] += dy
# Check không đi được vào Obs
    for obs in obstacle:
        if player["x"] == obs["x"] and player["y"] == obs["y"]:
            player["x"] -= dx
            player["y"] -= dy
# Check 2 hộp cạnh nhau không đẩy được
    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            box["x"] += dx
            box["y"] += dy
            k = deepcopy(n)
            bien = True
            for box1 in k:
                if box["x"]==box1 ["x"] and box["y"]==box1["y"]:
                    boxes = k
                    bien = False
                else:
                    for obs in obstacle:
                        if box["x"] == obs["x"] and box["y"] == obs["y"]:
                            boxes = k
                            bien = False
                        elif box["x"] == map["x"] or box["y"] == map["y"]:
                            bien = False
                            boxes = k 
                        else:
                            kd = k 
                            # hoàn toàn không hiểu có chuyện gì xảy ra ở dòng này :))))
                            n = deepcopy(boxes)
            if bien == False:
                player["x"] -= dx
                player["y"] -= dy

# Đẩy bay mẹ box ra khỏi map =)))