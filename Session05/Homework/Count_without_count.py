number = [1,6,8,1,2,1,5,6]
numb = int(input("Enter a number: "))
count = 0
for num in number:
    if num == numb:
        count +=1
print("{} appears {} times in my list".format(numb,count))