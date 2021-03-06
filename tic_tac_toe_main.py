import random
import os

# ---------------------------Deepa functions--------
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
 
 
def game_type():
    print("\t--------------------------------------")
    print("\t  What game type do you chose ?       ")
    print("\t  1) computer vs human                ")
    print("\t  2) human vs human                   ")
    print("\t--------------------------------------")
    while True:
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
    
        # Conditions for player choice  
        if choice == 1:
            game_choice = 0
            
        elif choice == 2:
            game_choice = 1
            
        else:
            print("Wrong Game Choice!!!! Try Again\n")
            continue

        return game_choice

# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# Function to check if any player has won
def check_win(player_pos, cur_player):
 
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Function for a single game of Tic Tac Toe
def single_game(cur_player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = cur_player
 
        # Updating player positions
        player_pos[cur_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

# ---------------------------Michael functions, if not using above --------
def game_init():
  _=os.system("cls")
  positions = ["1","2","3","4","5","6","7","8","9"]
  print_tic_tac_toe(positions)
  print(" Your choices are defined, they must be from 1 to 9. The computer will start with X.")
  input ("Press enter to continue")

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




# big function on computer vs human ---------------------------coputer vs human function--------
def com_vs_hum():
        
    while True:

        #Computer starts playing with 'X'
        while True:
            computer = player_computer()    
            if check_emptybox(computer) == True: # must be true, so position is free
                break                               # end while loop of X chosing position
                                     
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
        
        

        #Human starts playing with 'O'
        while True:
            human = int(input("Please choose your box from 1-9  "))
            # human = int(human)  
            if check_emptybox(human) == True: # must be true, so position is free
                break                               # end while loop of X chosing position
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

        # break # required here ???

# big function on human vs human ---------------------------human vs human function--------
def hum_vs_hum():

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    cur_player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the options
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1
 
if __name__ == "__main__":
    
    # ask for game combination a) computer vs human and B) human vs human
    game_choice = game_type()

    if game_choice == 0: # computer vs human
        values = [' ' for x in range(9)]
        game_init()
        com_vs_hum()

    if game_choice == 1: # human vs human
        hum_vs_hum()

    
