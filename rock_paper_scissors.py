import random

'''
>>> Please type your choice : q
"Thanks for playing."
>>> Please type your choice : rock
"You choose rock."
"Your opponent chooses scissors."
"You win!"
>>> Please type your choice : kskfw
"Error, please type rock, paper, scissors or q to quit."
'''

while True:

    choices = ['rock', 'paper', 'scissors', 'q']
    player_choice = input("Please type your choice: ")

    if player_choice not in choices:
        print("Error, please type rock, paper, scissors or q to quit.")
        continue
    if player_choice == 'q':
        print("Thanks for playing.")
        break
    
    exception = 'q'
    choices.remove(exception)
    opponent_choice = random.choice(choices)

    print(f"You choose {player_choice}")
    print(f"Your opponent chooses {opponent_choice}")

    if player_choice == opponent_choice:
        print("It's a tie!")
    elif player_choice == 'rock' and opponent_choice == 'scissors' or player_choice == 'scissors' and opponent_choice == 'paper' or player_choice == 'paper' and opponent_choice == 'rock':
        print("You win!")
    else:
        print("You lose!")

    






        







    






    


