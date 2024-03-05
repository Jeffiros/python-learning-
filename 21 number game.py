import random
'''
Randoming order...
You are the 2nd.
Bot is the 1st.

the first one who reaches 21 will lose.
GLHF ^_^

bot turn
"bot goes 4 numbers."
1
2
3
4
[1, 2, 3, 4]
player turn
"you go 3 numbers."
5
6
7
[5, 6, 7]
.
.
.
player turn
"you go 2 numbers."
20
21
YOU LOST!
BOT WON!

'''

# def randomed_order():
    
#     namelist = ["player", "bot"]
#     firstp = random.choice(namelist)
#     namelist.remove(firstp)
#     secondp = namelist[0]

#     print('Randoming order...')
#     print(f'''The first one is {firstp}. The second one is {secondp}.''')

def playing(firstp, secondp):

    number_list = [i for i in range(1, 22)]

    if firstp == "player" and secondp == "bot":
        
        while True:
            
            while True:

                player_input = int(input("Enter your times to show number: "))
                if player_input > 0 and player_input <= 4 :
                    print(f"You go {player_input} times.")
                    # print(number_list[0:player_input])
                    player_list = number_list[:player_input]
                    print(player_list)
                    number_list = [ x for x in number_list if x not in player_list]
                    print(number_list)
                    break
                else:
                    print("Please input a number 1-4.")
                    continue
                
        
            if number_list == []:
                print("You lost!")
                break

            bot_choice = [1, 2, 3, 4]

            if len(number_list) == 4:
                deleted_choice = [4]
                bot_choice = [x for x in bot_choice if x not in deleted_choice]
            elif len(number_list) == 3:
                deleted_choice = [3,4]
                bot_choice = [x for x in bot_choice if x not in deleted_choice]
            elif len(number_list) == 2:
                deleted_choice = [2,3,4]
                bot_choice = [x for x in bot_choice if x not in deleted_choice]

            bot_input = random.choice(bot_choice)

            print(f"Bot goes {bot_input} times.")
            # print(number_list[0:bot_input])
            bot_list = number_list[:bot_input]
            print(bot_list)
            number_list = [ x for x in number_list if x not in bot_list]
            print(number_list)

            if number_list == []:
                print("Bot lost!")
                break
    
    elif firstp == "bot" and secondp == "player":

        while True:

            bot_choice = [1, 2, 3, 4]

            if len(number_list) == 4:
                deleted_choice = [4]
                bot_choice = [x for x in bot_choice if x not in deleted_choice]
            elif len(number_list) == 3:
                deleted_choice = [3,4]
                bot_choice = [x for x in bot_choice if x not in deleted_choice]
            elif len(number_list) == 2:
                deleted_choice = [2,3,4]
                bot_choice = [x for x in bot_choice if x not in deleted_choice]

            bot_input = random.choice(bot_choice)

            print(f"Bot goes {bot_input} times.")
            # print(number_list[0:bot_input])
            bot_list = number_list[:bot_input]
            print(bot_list)
            number_list = [ x for x in number_list if x not in bot_list]
            print(number_list)

            if number_list == []:
                print("Bot lost!")
                break

            while True: 
                player_input = int(input("Enter your times to show number: "))
                
                if player_input > 0 and player_input <= 4 :
                    print(f"You go {player_input} times.")
                    # print(number_list[0:player_input])
                    player_list = number_list[:player_input]
                    print(player_list)
                    number_list = [ x for x in number_list if x not in player_list]
                    print(number_list)
                    break
                else:
                    print("Please input a number 1-4.")
                    continue
                
        
            if number_list == []:
                print("You lost!")
                break


def game():

    # randomed_order()
    
    
    while True:

        namelist = ["player", "bot"]
        firstp = random.choice(namelist)
        namelist.remove(firstp)
        secondp = namelist[0]

        print('Randoming order...')
        print(f'''The first one is {firstp}. The second one is {secondp}.''')
        print('''the first one who reaches 21 will lose.
            GLHF ''')
        
        playing(firstp, secondp)
        
        # while True:
            
        #     while True:

        #         player_input = int(input("Enter your times to show number: "))
        #         if player_input > 0 and player_input <= 4 :
        #             print(f"You go {player_input} times.")
        #             # print(number_list[0:player_input])
        #             player_list = number_list[:player_input]
        #             print(player_list)
        #             number_list = [ x for x in number_list if x not in player_list]
        #             print(number_list)
        #             break
        #         else:
        #             print("Please input a number 1-4.")
        #             continue
                
        
        #     if number_list == []:
        #         print("You lost!")
        #         break

        #     bot_choice = [1, 2, 3, 4]

        #     if len(number_list) == 3:
        #         deleted_choice = [4]
        #         bot_choice = [x for x in bot_choice if x not in deleted_choice]
        #     elif len(number_list) == 2:
        #         deleted_choice = [3,4]
        #         bot_choice = [x for x in bot_choice if x not in deleted_choice]
        #     elif len(number_list) == 1:
        #         deleted_choice = [2,3,4]
        #         bot_choice = [x for x in bot_choice if x not in deleted_choice]

        #     bot_input = random.choice(bot_choice)

        #     print(f"Bot goes {bot_input} times.")
        #     # print(number_list[0:bot_input])
        #     bot_list = number_list[:bot_input]
        #     print(bot_list)
        #     number_list = [ x for x in number_list if x not in bot_list]
        #     print(number_list)

        #     if number_list == []:
        #         print("Bot lost!")
        #         break
            
        while True:
                play_again = input("would you like to play again (y/n)?: ").lower()
                if play_again == "y" or play_again == "n":
                    break
                else:
                    print("Invalid")
                        
        if play_again == "n":
            break         
                 
game()




