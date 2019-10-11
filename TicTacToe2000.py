"""
TicTacToe2000 1.0
py 3.7
"""

#chose number from 1-9, if anything else entered, try again
def possible_numbers():
    enter_val = input("Enter field: ")
    ok_numbers = ['1','2','3','4','5','6','7','8', '9']
    if enter_val in ok_numbers:
        return enter_val
    else:
        print("Wrong input. Try again")
        return possible_numbers()
    
#create 9 fields with dict
field = {}
def fields():
    global field
    for i in range(9):
        field[i] = [i+1,0]

def board():
    print(" ----------- ")
    print("|", field[0][0],"|", field[1][0],"|", field[2][0],"|" )
    print(" ----------- ")
    print("|", field[3][0],"|", field[4][0],"|", field[5][0],"|")
    print(" ----------- ")
    print("|", field[6][0],"|", field[7][0],"|", field[8][0],"|")
    print(" ----------- ")

#define win situation
def win():
    for i in range(3):
        if field[3*i]==field[3*i+1]==field[3*i+2]:
            return True
        if field[i]==field[i+3]==field[i+6]:
            return True
        if field[0]==field[4]==field[8] or field[2]==field[4]==field[6]:
            return True        
    
#swap player
def otherplayer(player):
    if player is "X":
        return tictac_z("O")
    if player == "O":
        return tictac_z("X")

#counter: dictionary. start value is 0
plx = {("X"):0}
plo = {("O"):0}    

#enter player to return equivalent dictionary for player x or o
def pl_z(player):
    if player == "X":
        pl_z = plx
        return plx
    if player == "O":
        pl_z = plo
        return plo
    else:
        print("Error")

#score counter, adds one if called
def score_counter(player):
    plz = pl_z(player)
    plz[player] += 1

#displays score
def score():
    print(" ")
    print("Total Score:")
    print("--------------")
    print("Player 'X': ", plx["X"],"   Player 'O': ",plo["O"])

#counts the values of plx and plo and decides who wins    
def who_wins():
    if plx["X"] > plo["O"]:
        return "Player 'X'"
    if plx["X"] < plo["O"]:
        return "Player 'O'"
    else:
        return "No one"

#chose field on board
#eltlist is a list of 1 or 0, taken from the field value  4: ['O', 1]
#before first move, all are 0, when all is full, they are 1 and game_over() will be caused
def move(player, enter_val_int):
    eltlist = []
    if field[enter_val_int-1][0] == "X" or field[enter_val_int-1][0] == "O":
        print("Already occupied. Try again")
        tictac_z(player)    
    else:
        field[enter_val_int-1][0] = player
        field[enter_val_int-1][1] = 1
        for i in range(9):
            eltlist.append(field[i][1])
        if win() == True:
            score_counter(player)
            print(" ")
            board()
            print("Player '" + player + "' wins!")
            score()
            return tictac_retry()
        elif all(eltlist):
            board()
            return game_over()
        else:
            print(" ")
            board()
            otherplayer(player)

#player x / o          
def tictac_z(player):
    print("Player '"+ player+"'s turn")
    enter_val = possible_numbers()
    enter_val_int = int(enter_val)
    move(player, enter_val_int)

#start game
def tictactoe():
    field = fields()
    enter_val = input("Choose Player [X/O]: ")
    if enter_val == "X" or enter_val == "x":
        print(" ")
        board()
        return tictac_z("X")
    if enter_val == "O" or enter_val == "o" or enter_val == "0":
        print(" ")
        board()
        return tictac_z("O")
    else:
        print("Input not valid. Try again.")
        return tictactoe()

#game over in case of board full
def tictac_retry():
    print(" ")
    enter_val = input("Play again? [Y/N]: ")
    if enter_val == "Y" or enter_val == "y":
        field = fields()
        return tictactoe()
    if enter_val == "N" or enter_val == "n":
        player = who_wins()
        print(26*"-")
        print(" ")
        print(player + " wins the game!")
        print(" ")
        print(26*"-")
    else:
        print("Input not valid. Try again.")
        return tictac_retry()

def game_over():
    print(" ")
    print("Game Over!")
    score()
    return tictac_retry()

tictactoe()
