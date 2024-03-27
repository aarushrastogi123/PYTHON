logo='''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢁⣴⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⢀⣴⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠘⢦⡀⠙⢿⣿⣿⣿⣿⣿⣿⠟⠁⡴⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠓⠀⠉⠀⠀⠙⢿⣿⣿⠟⠁⡠⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠙⠁⠐⠊⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⢤⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣦⡈⠳⠄⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
print(logo)
print("Welcome to the Secret Auction Program.")
print("Enter your names and place bids.")
import os
from time import sleep
bidding_finished=False
bids={}

def find_winner(bidding_record):
    highbid=0
    winner=" "
    for bidder in bidding_record:
        bid_amount=int(bidding_record[bidder])
        if bid_amount > highbid:
            highbid=bid_amount
            winner= bidder
    print(f"The winner is {winner} with the bid of Rs.{highbid}/-")    

while not bidding_finished:   
    name=input("What is your name?: ")
    bid=input("What is your bid? Rs.")
    bids[name]=bid
    a=input("Are there any other bidders(yes or no): ")
    if a=="yes":
        sleep(1)
        os.system('cls')
    elif a=='no':
        bidding_finished=True 
        sleep(1)
        os.system('cls')
        find_winner(bids)
sleep(5)
os.system('cls')        
