import random

print("GUESSING NUMBER GAME")

s = random.randint(0,101)
b = []

while True:

    a = int(input("Enter a number "))

    if a > s:
        b.append(a)
        print("previous guesses ", b)
        print("Wrong! The number is too high.")
        
    elif a < s:
        b.append(a)
        print("previous guesses ", b)
        print("Wrong! The number is too low.")
        
    else:
        b.append(a)
        print("previous guesses ", b)
        print("Congratulations! You guess the right number.")
        break