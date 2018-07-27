menu = ["book1","book2","book3"]
print("Hi there, there are your favorite things:")
print(*menu, sep=", ")
n = input("Need add something more? ")
menu.append(n)
print(*menu,sep =", ")