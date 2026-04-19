## Rock, Paper and Scessior Game

import random

def fight(user_choice):
    
    comp_choice = random.choice(['rock','paper','scessior'])

    match user_choice:
        case 'rock':
            if comp_choice == 'paper':
                print("Bot had choosen rock.")
                print("computer Win!🤖 you Lost...🥲")
            else:
                print("Bot had choosen rock.")
                print("Yooohuu...you won!!🥳")
            rematch()
        
        case 'paper':
            if comp_choice == 'scessior':
                print("Bot had choosen paper.")
                print("computer Win!🤖 you Lost...🥲")
            else:
                print("Bot had choosen paper.")
                print("Yooohuu...you won!!🥳")
            rematch()
        
        case 'scessior':
            if comp_choice == 'rock':
                print("Bot had choosen scessior.")
                print("computer Win!🤖 you Lost...🥲")
            else:
                print("Bot had choosen scessior.")
                print("Yooohuu...you won!!🥳")
            rematch()
        

def rematch():
    case = input("Enter 'rematch' to fight again / 'end' to finish :")
    match case:
        case 'rematch':
            user_choice = input("Choose rock/papaer/scessior : ")
            fight(user_choice)
        case 'end':
            print('Exiting Game...')
            

print("="*70)
print(f'{" "*10}ROCK-PAPER-SCESSIOR')
print("="*70)

print()

user_choice = input("Choose rock/papaer/scessior : ")
fight(user_choice)