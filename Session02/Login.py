from getpass import *
print("Hello, this is a super gateway")
n = input("username:")
if n != "DSH":
    print("Your user name is invalid")
else:
    m = getpass("Password:",)
    if m != "abc":
        print("Your password is invalid")
    else:
        print("Login sucssesfull, Wellcome", n)