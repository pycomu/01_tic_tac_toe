# -*- coding: utf-8 -*-

import random
import os

def game_init():
  _=os.system("cls")
  positions = ["1","2","3","4","5","6","7","8","9"]
  print_tic_tac_toe(positions)
  print(" Your choices are defined, they must be from 1 to 9. The computer will start with X.")
  input ("Press enter to continue")

# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____') 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____') 
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Computer chose position
def player_computer():
  computer_position = random.randint(1, 9)
  print (computer_position)
  return computer_position

# Check if the position is empty 
def check_emptybox(position):      
  if values[position-1]==" ":
    return True 

def is_winning(symbol):
    if (values[0] == symbol and values[1] == symbol and values[2] == symbol) or \
        (values[3] == symbol and values[4] == symbol and values[5] == symbol) or \
        (values[6] == symbol and values[7] == symbol and values[8] == symbol) or \
        (values[0] == symbol and values[3] == symbol and values[6] == symbol) or \
        (values[1] == symbol and values[4] == symbol and values[7] == symbol) or \
        (values[2] == symbol and values[5] == symbol and values[8] == symbol) or \
        (values[0] == symbol and values[4] == symbol and values[8] == symbol) or \
        (values[2] == symbol and values[4] == symbol and values[6] == symbol):
      return True
    else:
      return False

def is_tic_tac_toe_full():
	if " " in values:
		return False
	else:
		return True

# ---------------------------------------Start + Loop programm-------------------------

values = [' ' for x in range(9)]
game_init()


while True:

  # _=os.system("cls")
  # print_tic_tac_toe(values)

  #Computer starts playing with 'X' -------------
  while True:
    computer = player_computer()    
    if check_emptybox(computer) == True:  # must be true, so position is free
      break                                 # end while loop of X chosing position
  values[computer-1] = "X"
  print_tic_tac_toe(values)
  print(f"Computer position was: {computer}")
  print(values)
  
  if is_winning("X"):
      _=os.system("cls")
      print_tic_tac_toe(values)
      print ("X, the computer wins! Congratulations")
      break


  if is_tic_tac_toe_full():
		  print("Tie!")
		  break
  
  
  #Human starts playing with 'O' -------------------
  while True:
    human = int(input("Please choose your box from 1-9  "))
    # human = int(human)  
    if check_emptybox(human) == True:  # must be true, so position is free
      break                                 # end while loop of X chosing position
  values[human-1] = "O"
  print_tic_tac_toe(values)
  print(f"Human position was: {human}")  
  print(values)

  if is_winning("O"):
    _=os.system("cls")
    print_tic_tac_toe(values)
    print ("O, human player wins! Congratulations")
    break

  if is_tic_tac_toe_full():
      print("Tie!")
      break
  






# while True:
#   a = input("Drücke eine Zahl 1-10  ")
#   a = int(a)
#   if a == 3:
#     print("richtig")
#     break


  
