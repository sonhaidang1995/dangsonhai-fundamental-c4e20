from random import *
flock =[randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),]
print("Hello, my name is Hai and there is my sheep sizes")
print(flock)
print("")
print ("Now my biggest sheep has size ", max(flock), ". Let's shear it.", sep = "")
print("")
flock[flock.index(max(flock))] = 8
print("After shearing, here is my flock")
print(flock)