"""
py 3.7

TicTacToe 1.035

"""

#chose number from 1-9, if anything else entered, try again
def possible_numbers():
    eingabe = input("Enter number of field: ")
    ok_numbers = ['1','2','3','4','5','6','7','8', '9']
    if eingabe in ok_numbers:
        return eingabe
    else:
        print("Wrong input. Try again")
        return possible_numbers()
    
#create 9 fields
field = []
for i in range(9):
    field.append(str(i+1))
    
#create board with the 9 fields
def board():
    print(field[0],field[1],field[2])
    print(field[3],field[4],field[5])
    print(field[6],field[7],field[8])

#define win situation
def win():
    if field[0]==field[1]==field[2] or field[3]==field[4]==field[5] or field[6]==field[7]==field[8]:
        return True
    if field[0]==field[3]==field[6] or field[1]==field[4]==field[7] or field[2]==field[5]==field[8]:
        return True
    if field[0]==field[4]==field[8] or field[2]==field[4]==field[6]:
        return True

#define when board is full without winner
def full():
    if ((field[0] == "X" or  field[0] == "O") and
        (field[1] == "X" or  field[1] == "O") and
        (field[2] == "X" or  field[2] == "O") and
        (field[3] == "X" or  field[3] == "O") and
        (field[4] == "X" or  field[4] == "O") and
        (field[5] == "X" or  field[5] == "O") and
        (field[6] == "X" or  field[6] == "O") and
        (field[7] == "X" or  field[7] == "O") and
        (field[8] == "X" or  field[8] == "O")):
        print(" ")
        board()
        return True
    else:
        return False

#swap player
def otherplayer(player):
    if player is "X":
        return tictac_z("O")
    if player == "O":
        return tictac_z("X")

#chose field on board
def move(player, eingabe_int):
    if field[eingabe_int-1] == "X" or field[eingabe_int-1] == "O":
        print("Already occupied. Try again")
        otherplayer(player)    
    else:
        field[eingabe_int-1] = player
        if win() == True:
            print(" ")
            board()
            print("Player '" + player + "' wins!")
        elif full() == True:
            return game_over()
        else:
            print(" ")
            board()
            otherplayer(player)

#player x / o          
def tictac_z(player):
    print("Player '"+ player+"'s turn")
    eingabe = possible_numbers()
    eingabe_int = int(eingabe)
    move(player, eingabe_int)

#start game
def tictactoe():
    eingabe = input("Choose Player [X/O]: ")
    if eingabe == "X" or eingabe == "x":
        print(" ")
        board()
        return tictac_z("X")
    if eingabe == "O" or eingabe == "o" or eingabe == "0":
        print(" ")
        board()
        return tictac_z("O")
    else:
        print("Input not valid. Try again.")
        return tictactoe()

#game over in case of board full
def tictac_retry():
    eingabe = input("Play again? [Y/N]: ")
    if eingabe == "Y" or eingabe == "y":
        return tictactoe()
    if eingabe == "N" or eingabe == "n":
        print("----- Bye ;) -----")
    else:
        print("Input not valid. Try again.")
        return tictac_retry()

def game_over():
    print(" ")
    print("      -----------------------------------------------------      ")
    print("-----------No Winner! Both Players lose! Game Over!--------------")
    print("      -----------------------------------------------------      ")
    print(" ")
        
tictactoe()
