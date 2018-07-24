num = int(input("Number of table:"))
for i in range (1,num+1):
    for k in range(1,num+1):
        if k*i <10:
            print(k*i,end="   ")
        elif k*i <100:
            print(k*i,end="  ")
        else:
            print(k*i,end=" ")
    print("")
