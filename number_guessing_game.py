'''
enter a guess : 10
previous guesses : 10
" Wrong! The number is too low."

enter a guess : 20
previous guesses : 10 20 
"Wrong! The number is too high."

enter a guess : 18
previous guesses : 10 20 18
"Congratulations! You guess the right number."

'''
print("GUESSING NUMBER GAME")

b = ''
loop = True
while loop:

    s = 13
    a = int(input("Enter a number "))

    if a > s:
        b = b + str(a) + " "
        print("previous guesses ", b)
        print("Wrong! The number is too high.")
        
    elif a < s:
        b = b + str(a)+" "
        print("previous guesses ", b)
        print("Wrong! The number is too low.")
        
    else:
        b = b + str(a)+" "
        print("previous guesses ", b)
        print("Congratulations! You guess the right number.")
        loop = False
