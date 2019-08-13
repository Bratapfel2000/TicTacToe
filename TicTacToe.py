"""
py 3.7

TicTacToe 1.0

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
##board()

#define win situation
def win():
    if field[0]==field[1]==field[2] or field[3]==field[4]==field[5] or field[6]==field[7]==field[8]:
        return True
    if field[0]==field[3]==field[6] or field[1]==field[4]==field[7] or field[2]==field[5]==field[8]:
        return True
    if field[0]==field[4]==field[8] or field[2]==field[4]==field[6]:
        return True

# player x. enter number with possible_numbers().
# If field occupied go back to start.
# If not, assign place with "X".
# if win() is True, player wins.
# If not win() is True, call player "O" tictac_o()

def tictac_x():
    print("Player 'X's turn")
    eingabe = possible_numbers()
    eingabe_int = int(eingabe)
    if field[eingabe_int-1] == "X" or field[eingabe_int-1] == "O":
        print("Already occupied. Try again")
        tictac_x()
    else:
        field[eingabe_int-1] = "X"
        if win() == True:
            print(" ")
            board()
            print("Player 'X' wins!")
        else:
            print(" ")
            board()
            tictac_o()
            
# Same procedure as with player "X"        
def tictac_o():
    print("Player 'O's turn")
    eingabe = possible_numbers()
    eingabe_int = int(eingabe)
    if field[eingabe_int-1] == "X" or field[eingabe_int-1] == "O":
        print("Already occupied. Try again")
        tictac_o()
    else:
        field[eingabe_int-1] = "O"
        if win() == True:
            print(" ")
            board()
            print("Player 'O' wins!")
        else:
            print(" ")
            board()
            tictac_x()

            
#Chose player for start
def tictactoe():
    eingabe = input("Who starts? Chose Player 'X' or Player 'O': ")
    if eingabe == "X" or eingabe == "x":
        print(" ")
        board()
        tictac_x()
    if eingabe == "O" or eingabe == "o":
        print(" ")
        board()
        tictac_o()
    else:
        print("Input not valid. Try again")
        return tictactoe()

        
tictactoe()
