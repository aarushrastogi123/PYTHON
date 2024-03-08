from hangman_word import word_list ,stages,logo

print(logo)

lives =6

import random as r

chosen_word=r.choice(word_list)

print("Guess The Word")

a="_"
sym_list=[]

for i in chosen_word:
    sym_list+=a

end_of_game=False

while not end_of_game:
   
    guess = input("\nGuess the letter: ").lower()
   
    if guess in sym_list:
        print(f"You have already guesses the letter {guess}")
         
    for position in range(len(chosen_word)):
        l=chosen_word[position]
      
        if l==guess:
            sym_list[position]=l    
        
    if guess not in chosen_word:
        lives-=1
      
        print(f"You guess a letter {guess}, that's not in word, You lose a life")
      
        if lives==0:
            end_of_game=True
            print("Hangman got hung.\nYou lose")
    
    print(stages[lives])
    
    print(f"You reached till = {sym_list}")
    
    if a not in sym_list:
        end_of_game=True
        print("You saved the Hangman.\nYou win!!!")






    


