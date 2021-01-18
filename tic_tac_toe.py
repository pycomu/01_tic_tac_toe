# -*- coding: utf-8 -*-

import random


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

values = [' ' for x in range(9)]

print_tic_tac_toe(values)

# function to set up a human player
def setup_player():
  current_player = input('Please enter your name: ')
  # current_symbol = input('choose your symbol: (X/O)').upper()
  print(f"Hello {current_player}, your symbol is 'O'")

#setup_player()



print("Please choose your box from 1-9")

#function for Computer player settings
def player_computer():
  computer_position = random.randint(1, 9)
  print(f"My position: {computer_position}")
  return computer_position

player_computer()

#function to Update the board
def update_board(position,symbol):
  # position=input("Enter a valid position on board")
  # #Ask player to input a position (1-9). Ask while the position is not valid (check using valid_position)

  # while not check_emptybox(position):
  #   position=input(" Enter a valid position on board")
  # #Write player's sign in board
  # position=int(position)-1
  values[position-1] = symbol 
  print_tic_tac_toe(values)

#function to check the availability of the box
def check_emptybox(position):
  #Check if the position is empty     
  if values[position-1]==" ":
    return True
  
   

while True:
# Init
  # values = [' ' for x in range(9)]
  # print_tic_tac_toe(values)
  # positions = ["1","2","3","4","5","6","7","8","9"]
  # print_tic_tac_toe(positions)

#Computer starts playing with 'X'
  while True: 
    computer = player_computer()
    if check_emptybox(computer) == True:
      update_board(computer,"X")
      break
    # else:
    #   continue

#Human starts playing with 'O'
  # player = "O"
    print_tic_tac_toe(values)

  break
