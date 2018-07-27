from random import *
number = randint(1,100)
playing = True
count = 0
while playing:
    guess = int(input("Guess my number(1-100):"))
    if guess > number:
        print("Too large")
    elif guess < number:
        print("Too small")
    else:
        print("Bingo")
        break
    count += 1
    if count >= 7:
        print("You lose")
        break
