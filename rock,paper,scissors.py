# -*- coding: utf-8 -*-
"""Rock,Paper,Scissors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fcKuYsIF12D3eTSMftRf4G4fpGnIzv0T

**Rock,Paper,scissors game**
"""

#import modules

import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
  user_input = input("Type Rock , Paper, scissors or Q to Quit : ").lower()
  if user_input == "q":
    break

  if user_input not in options:
    continue

  random_number = random.randint(0,2)
  computer_picks = options[random_number]
  print("Computer_Picked",computer_picks + ".")

  if user_input == "rock" and computer_picks == "scissors":
    print("You Won")
    user_wins += 1

  elif user_input == "paper" and computer_picks == "rock":
    print("You Won!")
    user_wins += 1

  elif user_input == "scissors" and computer_picks == "paper":
    print("You Won!")
    user_wins += 1

  elif user_input == "rock" and computer_picks == "rock":
    print("Its Draw")

  elif user_input == "paper" and computer_picks == "paper":
    print("Its Draw")

  elif user_input == "scissors" and computer_picks == "scissors":
    print("Its Draw")

  else:
    print("OOPS You Lost!")
    computer_wins += 1

print("You Won", user_wins, "times")
print("The computer Won", computer_wins, "times")
print("Good Game")

