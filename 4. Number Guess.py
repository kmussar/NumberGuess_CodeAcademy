#Number Guess.py
"""
Created on Wed May  9 18:58:24 2018
@author: kmuss
"""

"""This seems like a weird game. The program rolls dice. The user inputs a number. If the user's guess is higher than the total value of the dice roll, they win. Why wouldn't the user always guess a high number? ..Ah, they address this later."""
from random import randint 
from time import sleep 
def get_user_guess():
  user_guess = int(input("Please enter a number between 2 and the maximum possible value."))
  return user_guess
def roll_dice(number_of_sides):
    first_roll = randint(1,number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides * 2
    print("The maximum possible value is: %s." % str(max_val))
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val: 
      print("Your number is invalid.")
      return 
    else: 
      print("Rolling...")
      sleep(2)
      print("The first roll is: %d." % first_roll)
      sleep(1)
      print("The second roll is: %d." % second_roll)
      sleep(1)
      total_roll = first_roll + second_roll 
      print("The total roll is: %d." % total_roll)
      print("Result...")
      sleep(1)
      if user_guess > total_roll: 
        print("You win!")
        return
      else: 
        print("Sorry, you have lost this time.")
        return 
roll_dice(8)