# Cách 1: Làm kiểu thừa giấy vẽ voi =))
menu =["Tôm","Cua","Cá","Mực"]
print("Hi there, here you favorite things so far")
for i in range(40):
    print("*",end="")
print("")
for index, items in enumerate(menu,1):
    print("{}.{}".format(index, items))
for i in range (40):
    print("*",end="")
print("")
n = int(input("Position you want to update? "))
k = input("Your replacing favorite? ")
menu[n-1] = k
for i in range(40):
    print("*",end="")
print("")
for index, items in enumerate(menu,1):
    print("{}.{}".format(index, items))
for i in range (40):
    print("*",end="")

# Cách 2
menu = ["Tôm","Cua","Cá","Mực"]
print("Hi there, here is your favorite things so far")
print("*"*50)
for index,item in enumerate(menu,1):
    print("{}.{}".format(index, item))
print("*"*50)
pos = int(input("Position you want to update? "))
fav = input("Your replacing favorite? ")
menu[pos-1]= fav
print("*"*50)
for index,item in enumerate(menu,1):
    print("{}.{}".format(index, item))
print("*"*50)
