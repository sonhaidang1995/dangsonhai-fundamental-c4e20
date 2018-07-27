items = ["T-Shirt","Sweater"]
print(len(items))
loop = True
while loop:
    command = input("Welcome to our shop, what do you want (C, R, U, D)? ").upper()
    if command == "R":
        print("Our items:",end=" ")
        print(*items, sep=", ")
    elif command == "C":
        insert = input("Enter new item: ")
        items.append(insert)
        print("Our items:",end=" ")
        print(*items, sep=", ")
    elif command == "U":
        update = int(input("Update position? "))
        if update > len(items):
            update = len(items)-1
        else:
            update = update-1
        replace = input("New item? ")
        items[update] = replace
        print("Our items:",end=" ")
        print(*items, sep=", ")
    elif command == "D":
        delete = int(input("Delete position? "))
        if delete > len(items):
            delete = len(items)-1
        else:
            delete = delete -1
        del items[delete]
        print("Our items:",end=" ")
        print(*items, sep=", ")
    else:
        print("Wrong command")
        print("Bye")
        loop = False