from random import *
flock =[randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),]
time = int(input("How long are you going to be a shepherd (months): "))
print("Hello, my name is Hai and there is my sheep sizes")
print(*flock, sep=", ")
print("Now my biggest sheep has size",max(flock),"let's shear it")
flock[flock.index(max(flock))] = 8
for k in range (1,time+1):
    print("")
    print("Month",k)
    flock =[x+50 for x in flock]
    print("One month has pass, now here is my flock")
    print(*flock,sep=", ")
    if k != time:
            print("Now my biggest sheep has size",max(flock),"let's shear it")
            flock[flock.index(max(flock))] = 8
            print("After shearing, here is my flock")
            print(*flock,sep=", ")
    else:
        sum(flock)
        print("My flock has size in total:",sum(flock))
        print("I would get",sum(flock),"* 2$ = ", sum(flock)*2,"$"  )
