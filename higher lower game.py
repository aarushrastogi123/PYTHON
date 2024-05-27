from higher_lowergamedata import logo,vs,data 

import random as r 

from time import sleep

import os

def getData():

    return r.choice(data)

def setdata(account):

    name= account["name"]

    description= account["description"]

    country= account["country"]

    return f"{name}, a {description}, from {country}"

def answer(guess, a_followers, b_followers):

    if a_followers>b_followers:

        return guess=="a"

    else:

        return guess=="b"
    
def game():

    print(logo)

    score=0

    continue_game= True

    account_a=getData()

    account_b=getData()

    while continue_game:

        account_a=account_b

        account_b=getData()

        if account_a==account_b:

            account_b=getData()

        print(f"Compare A: {setdata(account_a)}.")

        print(vs)

        print(f"Against B: {setdata(account_b)}.")        

        guess=input("Who has more followers on INSTAGRAM? 'A' or 'B':").lower()

        a_follower_count= account_a["follower_count"]

        b_follower_count= account_b["follower_count"]

        is_correct=answer(guess,a_follower_count,b_follower_count)

        sleep(1)

        os.system('cls')

        if is_correct:

            score+=1

            print(logo)

            print(f"You r right. Your current score = {score}.")

        else:

            continue_game=False

            print(f"You r wrong. Final score= {score}.")

game()

