#------------------------------------
#     Filename:  hangman.py
#
#     Description:  Hangman Game.
#  user has 10 tries to guess random
#      word from words.txt
#
#        Version:  1.0
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
   with open("words.txt") as file:
      lines = file.readlines()
      lines = [line.rstrip() for line in lines]

   word = random.choice(lines)

   letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   print("Guess the characters!")
   chars_used = ''

   turns = 10
   while turns > 0:
      failed = 0
      preview = ""

      for x in word:

         if x in chars_used:

            preview += x

         else:
            preview += "_"

            failed += 1
      print(" ".join(preview))
      print("Letters you have not used yet: \n" + " ".join(letters))

      if failed == 0:
         print("You win!\nThe word is: " , word)
         break


      guess = input("guess a letter:")

      for char in letters:
         if guess.capitalize() in letters:
            letters = letters.replace(guess.capitalize(), "")





      if len(guess) < 1:
         print("please enter a character")

      elif len(guess) > 1:
         print("you entered more than one character, try again")

       elif ValueError:                  # 01/30/22 added character validation
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
response = input("\nWould you like to play again? Y/N: ")
if response.capitalize() == "Y":
   time.sleep(0.3)
   game()

else:
   print("Thank you for playing!")


