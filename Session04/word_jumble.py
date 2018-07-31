from random import *
word = "champion"
list_1 = list(word)
list_2 = []
loop = True
while loop:
    if len(list_1)== 0:
        loop = False
    else:
        random = choice(list_1)
        list_1.remove(random)
        list_2.append(random)
print(list_2)
word_01 = input("Guess the word? ")
if word_01 == word:
    print("Hura")
else:
    print("Sad")
