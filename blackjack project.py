logo='''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\/
                       _/ |                
                      |__/             
'''

import random as r

import os

from time import sleep

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=r.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score) :
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has Blackjack."
    elif user_score==0:
        return "Win with a Blackjack."
    elif user_score>21:
        return "You went over, You Lose."
    elif computer_score>21:
        return "Opponent went over, You Win."
    elif user_score>computer_score:
        return "You Win."
    else:
        return "you Lose"

def play_game():   
    user_cards=[]

    computer_cards=[]

    is_game_over=False

    for i in range (2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'Computer cards: {computer_cards[0]}')
        if user_score==0 or computer_score==21 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal=="y":
                user_cards.append(deal_cards())
            else:
                is_game_over=True 

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Score: {user_score}.")

    print(f"Computer's final hand: {computer_cards}, Score: {computer_score}")

    print(compare(user_score,computer_score))

while(input("Do you want to play a game of blackjack 'y' or 'n'? ")=="y"):
    os.system("cls")
    print(logo)
    play_game()
    sleep(2)
    os.system('cls')

os.system('cls')
