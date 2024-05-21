art='''

   ___                  _____ _          _  _            _             
  / __|_  _ ___ ______ |_   _| |_  ___  | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-<   | | | ' \/ -_) | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/   |_| |_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|  
                                                                       
'''

print(art)

print('Welcome to the Number guessing game')

print("I'm thinking of a number between 1 to 100")

easy_level=10

hard_level=5

import os

import random as r

from time import sleep

answer=r.randint(1,101)

def game():

    def check_answer(guess,answer,turns):
        
        if guess>answer:

            print('Too high')

            return turns-1
        
        elif guess<answer:

            print("Too low")

            return turns-1
        
        else: 

            print(f"You got it! The number is {answer}. ")

    def difficulty():
        
            level = input("Choose a difficulty. Type 'hard' or 'easy': ")
        
            if level=="easy":
           
                return easy_level
                
            else:
           
                return hard_level
                
    turns= difficulty()

    guess = 0

    while guess!=answer:            
        
        print(f"You have {turns} attempts to guess the number")
        
        guess=int(input('Make a guess: '))
        
        turns = check_answer(guess,answer,turns)
        
        if turns==0:
           
            return "You run out of guesses, You Lose!!!"

game()

sleep(2)

os.system('cls')