n = input("Press 'Enter' to fell amazing")
print("""Let me get your number
'c' if my guess is correct
'l' if my guess large than your number
's' if my guess is smaller then your number""")
loop = True
low = 1
high = 101
while loop:
    mid = (low+high)//2
    my_number = input("Is {} is your number?".format(mid))
    if my_number == "c":
        print("I knew it!!!")
        loop = False
    elif my_number == "s":
        low = mid
    elif my_number == "l":
        high = mid
    else:
        print("Wrong command, Try again!")
    if high == low:
        print("Dit cu may")
        break

