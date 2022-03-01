import random
from hangman_art import stages
from hangman_word import words

#choose a word from the list 
for i in words :
 chosen_word = random.choice(words)
print(chosen_word)

#create an empty list called display 
display=[]
n = len(chosen_word)
for i in range (0, n) :
    display.append("_")
print(display)
#ask the user for a letter 
count = len(stages)-1
while count >= 0 :
 if not "_"  in display :
     print("Congratulations! You have already guessed the word.")
     break
 guess = input("Guess a letter: ").lower()
 

#check if guess matches chosen word
 flag = 1 
 
 for i in range (len(chosen_word)):
    if chosen_word[i] == guess :
        display[i] = guess
        flag = 0
 if flag != 0 :
     print(stages[count])
     count=count-1
    
        
 print(display)
 
 
if count == -1 : 
 print("Game Over !")
 



