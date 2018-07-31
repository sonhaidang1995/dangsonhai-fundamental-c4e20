from random import *
word = ["champion","hello","goodbye","yeah","Goodjob"]
random_list = choice(word)
right_word = random_list
list_1 = list(random_list)
list_2 = []
loop = 0
while len(list_1)!=0:
    random = choice(list_1)
    list_1.remove(random)
    list_2.append(random)
print(list_2)
while loop != 4:
    loop += 1
    word_01 = input("Guess the word? ")
    if word_01 == right_word:
        print("Hura")
        loop = 4
    else:
        print("Sad")
print("Game over")
    
