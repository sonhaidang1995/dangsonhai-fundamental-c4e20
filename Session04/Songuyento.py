# number = int(input("your number?"))
# count = 0
# for i in range(1,number+1):
#     if number % i == 0:
#         count = count + 1
# if count > 2:
#     print("not")
# else:
#     print("Prime")

# Cách 2:
numb = int(input(""))
is_prime = True
loop = True
i = 2
while loop:
    if numb % i == 0:
        is_prime = False
    i += 1
    if i == numb:
        loop = False
if is_prime == True:
    print("{} is a prime number".format(numb))
else:
    print("{} is not a prime number".format(numb))

# # Cách 3
# numb = int(input(""))
# is_prime = True
# i = 2
# while i <= numb**(1/2):
#     if numb % i == 0:
#         is_prime = False
#     i += 1

# if is_prime == True:
#     print("{} is a prime number".format(numb))
# else:
#     print("{} not a prime number".format(numb))
