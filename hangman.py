#------------------------------------
#     Filename:  hangman.py
#
#     Description:  Hangman Game.
#  user has 10 tries to guess random
#      word from words.txt
#
#        Version:  1.1
#
#      Created:  01/12/22
#
#    Author:  Michoel Mushinsky
#------------------------------------
import random
import time
name = input("What is your name? ")

def game():

   print("Good Luck! " , name)
   time.sleep(1.0)
   with open("words.txt") as file:       #opening words.txt
      lines = file.readlines().    
      lines = [line.rstrip() for line in lines]

   word = random.choice(lines)           #chooses random word from words.txt

   letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".  

   print("Guess the characters!")
   chars_used = ''                       #records letters already used

   turns = 10                            #number of choices decreases every round
   while turns > 0:
      failed = 0
      preview = ""                       #preview of guessed word printed out every turn

      for x in word:

         if x in chars_used:

            preview += x                 #adds letter to 'preview' if letter is correct

         else:
            preview += "_"               #adds underscore if not correct

            failed += 1
      print(" ".join(preview)).                                           #example prints 'H_E_L_ W_R_D ' because letters 'h,e,l,w,r,d' were chosen correctly
      
      print("Letters you have not used yet: \n" + " ".join(letters)).     #prints letters not used yet

      if failed == 0:
         print("You win!\nThe word is: " , word)
         break


      guess = input("guess a letter:")

      for char in letters:
         if guess.capitalize() in letters:
            letters = letters.replace(guess.capitalize(), "").      #removes letters already guessed





      if len(guess) < 1:                                      # 01/30/22 added character validation
         print("please enter a character")

      elif len(guess) > 1:
         print("you entered more than one character, try again")

       elif ValueError:                  
         print("invalid character")  

    

      else:


            chars_used += guess

            if guess not in word:
               turns -= 1

               print("Wrong. You have ", turns , " more guesses")

               if turns == 0:
                  print("You Loose, ", name)

game()
time.sleep(2.5)
response = input("\nWould you like to play again? Y/N: ").   #asks for rematch
if response.capitalize() == "Y":
   time.sleep(0.3)
   game()

else:
   print("Thank you for playing!")    


