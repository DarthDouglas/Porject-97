import random
y=random.randint(1,9)
chances = 0
guess = random.randint(1,9)
print("Number Guessing Game")
while chances < 5:
    x=int(input("Enter number"))
    if guess > x:
        print("guess to low")

    elif guess < x:
        print("guess is high")

    else: 
        print(" you guessed it")
        break
    chances = chances + 1    

if not chances < 5:
    print("YOU LOSE!!! THE NUMBER IS, number")