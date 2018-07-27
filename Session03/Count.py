# Cách 2
n = int(input("Number: "))
count = 0
while True:
    if n >= 1:
       n= n/10 
       count += 1
    else:
        print(count)
        break

# Cách 3
counting = True
count = 0
n = int(input("Number: "))
while counting:
    n = n//10
    count = count + 1
    if n == 0:
        counting = False
        print(count)

# Cách 4:
numb = int(input("Enter a number: "))
count = 0
while numb !=0:
    numb = numb//10
    count +=1
print(count)
