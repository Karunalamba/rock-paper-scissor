import random
Cnumber= random.randrange(1,101)
Userinput=int(input("enter your number"))
if Cnumber>Userinput:
    print("Computer number",Cnumber)
    print("Your guess number is too low")
elif Userinput>Cnumber:
    print("Computer number",Cnumber)
    print("Your guess number is too high")
else:
    print("Computer number",Cnumber)
    print("Your guess number is equal")