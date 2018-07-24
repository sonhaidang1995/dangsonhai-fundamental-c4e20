for i in range (1,10):
    if i%2 == 0:
        for k in range(1,10):
            if k%2==0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print("")
    else:
        for k in range(1,10):
            if k%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print("")