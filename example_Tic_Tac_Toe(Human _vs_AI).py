# -*- coding: utf-8 -*-
"""m
Created on Sun Jun 21 13:25:35 2020

@author: Mimoona Raheel
"""

#----------------------------------
#           Tic Tac Toe
#----------------------------------


import random


EMPTY_SLOT = "-"
HUMAN= 'human'
COMPUTER = "computer"
TIE = "tie"
SYMBOL = ['X','O']


WIN_COMBINATION_INDICES = [
  # Complete row
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Complete column
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Complete diagonal
  [0, 4, 8],
  [2, 4, 6]
]


def initialize_board():
  board = [ EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT ]
  return board


def display_board(board):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

  
def random_turn():
  rand_num = random.randint(0,1)
  
  if rand_num == 0:
      player = HUMAN
  else:
      player = COMPUTER
  return player
  

def assign_symbol(player):
    
    if player == HUMAN:
        current_symbol = input('choose your symbol: (X/O)').upper()
    else:
        current_symbol = SYMBOL[random.randint(0,1)]
    return current_symbol

def switch_symbol(current_symbol):
    if current_symbol == 'X':
        current_symbol = 'O'
    else:
        current_symbol = 'X'
    return current_symbol


def handle_turn(player, board, current_symbol):
    print('---------------------')
    print(f'{player} your turn.')
    print('---------------------')
    position = valid_position(player, current_symbol, board)
    
    # Update the Board
    board[position] = current_symbol
    return board

    
def computer_turn(valid_list,current_symbol,board):
    
    # Going for a Win
    
    for each_list in WIN_COMBINATION_INDICES:
        combi = [ board[i] for i in each_list ]
       
        if combi.count(EMPTY_SLOT)==1 and combi.count(current_symbol)==2:
            position = each_list[ combi.index(EMPTY_SLOT) ]
            return position
        
        
    # Blocking Opponents Win
    
    for each_list in WIN_COMBINATION_INDICES:
        combi = [ board[i] for i in each_list ]
        if combi.count(EMPTY_SLOT)==1 and combi.count(current_symbol)==0:
            position = each_list[ combi.index(EMPTY_SLOT) ]
            return position
        
        
    # Take position in Center or Corners
    # range(start, end, step)
    
    temp = [board[i] for i in range(0,9,2)]
    if EMPTY_SLOT in temp:
        
        # fill corner or centre
        position = temp.index(EMPTY_SLOT) * 2 # 2x to map on board
    else:
        
        # Take Position on Sides
        position = random.choice(valid_list)  
    return position



# Checks the input is valid (user entered only one number, position is not filled)

def valid_position(player, current_symbol, board):
    
    while True:
        valid_list = [ i for i in range(9) if board[i] == EMPTY_SLOT ]
        if player == COMPUTER:
            position = computer_turn(valid_list,current_symbol,board)
            break
        else:
            try:
                position = input('Enter the position: ')
                position = int(position)-1
            
                if position in valid_list:
                    break
                
              #  Check the Repition
                elif position in range(9):
                    print('Sorry, your slot is already filled.')
                else:
                    print('Enter an integer between 1 to 9.')
            except ValueError:
                    print('Sorry,please enter only integers.')
    return position
 


def check_for_winner(board,player,current_symbol):

  winner = None
  filled_slots = 0
  for i in board:
    if i!= EMPTY_SLOT:
        filled_slots+=1
        

  # loop over WIN_COMBINATION_INDICES to check if one of the combination is X-X-X or O-O-O
  
  for each_list in WIN_COMBINATION_INDICES:
    i1 = each_list[0]
    i2 = each_list[1]
    i3 = each_list[2]
    if board[i1]==current_symbol and board[i2]==current_symbol and board[i3]==current_symbol:
        winner = player 
    
  if filled_slots==9 and winner==None:
    winner = TIE
  return winner
 
    
 
def switch_player(player): 
  if player == HUMAN:
      player = COMPUTER
  else:
      player = HUMAN   
  return player


def tic_tac_toe():
  global HUMAN
  winner = None
  game_still_going = True
  
  
  print('\n\n\n')
  print('*********************')
  print('*    TIC TAC TOE    *')
  print('* Computer vs Human *')
  print('*********************')
  
  
  HUMAN= input('Enter your name: ')
  player = random_turn()
 
  current_symbol = assign_symbol(player)
  print(f'{player} has the first turn')
  print(f'{player} has symbol {current_symbol}')
  
# Initialize board
  board = initialize_board()  
  
  # Run this while the game is still going
  while game_still_going:
      
      # Display board
      display_board(board)
            
      # Ask the player for a valid position and write it on the board
      board = handle_turn(player, board, current_symbol)
    
      # Check if there is a winner already
      winner = check_for_winner(board,player,current_symbol)
      if winner == player:
          display_board(board)
          print(f"Congratulations {winner}, you win !!!")
          game_still_going = False

      elif winner == TIE:
          display_board(board)
          print("Game is a tie")
          game_still_going = False

      player = switch_player(player)
      current_symbol = switch_symbol(current_symbol)
      
  #display_board(board)
  print("THE END")
  
  
  
tic_tac_toe()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  