from random import *
number = randint(0,100)
count = 0
while True:
    count +=1
    if count < 8:
        guess = int(input("Guess my number:"))
        if guess > number:
            print("Too large")
        elif guess < number:
            print("Too small")
        else:
            print("Bingo")
            break
    else:
        print("You lose")
        break