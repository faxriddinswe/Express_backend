import random

n = random.randint(0, 10)
guess = int(input("Guess a number between 0 and 10: "))

if n == 1:
    print("you fint it")
else:
    print("You didnt find it")

