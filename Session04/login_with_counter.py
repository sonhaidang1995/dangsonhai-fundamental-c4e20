count = 0
loop = True
while loop:
    username = input("username:")
    if username == "c4e":
        password = input("password:")
        if password == "codethechange":
            print("welcome",username)
            break
        else:
            print("password is incorrect")
    else:
        print("user not found")
    count +=1
    if count == 3:
        print("you failed to login 3 times, go away!!")
        loop = False