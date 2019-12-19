"""
TycTacToe2000 - II
Pre-Alpha
for use in cmd
version 0.013g01_colored
written with py 3.7.4
"""

"""
t: total matrix = dictionary. 1: [column, row, fieldnumber, occupied(1/0)]
f: numbers of fields of board (=m*n)
x: row of matrix
y: columns of matrix


x_3: marked rows
y_3: marked columns
z_3: marked diagonal top left->bottom right
z_4: marked diagonal top right -> bottom left

"""

from colorama import *

init()
##print(Fore.BLUE + "Hallo")


def explantation():
    print(" <---- m ---->")
    print("^")
    print("|")
    print("|")
    print("n")
    print("|")
    print("|")
    print("v")

#set matrix size
#m,n global so other functions can use it(printmatrix)
#create matrix, then print it. Return m and n
def set_matrix_size():
    global m
    global n
    global win_strike
    n = int(input("Set number height: "))
    m = int(input("Set number width: "))
    win_strike = winning_strike_length()
    matrix_nm(m,n)
    print("")
    return m,n

def possible_numbers():
    enter_val = input("Enter field: ")
    ok_numbers = []
    for i in range(1,m*n):
        ok_numbers.append(str(i))
    if enter_val in ok_numbers:
        return enter_val
    else:
        print_new_matrix(m,n)
        print("Wrong input. Try again")
        return possible_numbers()

    
def is_greater(x,y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return x

def winning_strike_length():
    win_strike = how_many_words()
    if win_strike == 0:
        print("")
        print("Number out of range....Please retry")
        return winning_strike_length()
    elif win_strike <= m or win_strike <= n:
        return win_strike
    else:
        print("")
        print("Number out of range....Please retry")
        return winning_strike_length()

def how_many_words():
    while True:
        try:
            maximum_length = is_greater(m,n)
            print("")
            print("Set winning strike length (max="+str(maximum_length)+"): ",end="")
            enter_val  = int(input(""))
        except ValueError:
            print("")
            print("Wrong input. Try again")
            continue
        else:
            return enter_val

#t: total matrix = dictionary. 1: [column, row, fieldnumber, occupied(1/0)]
t = {}
def matrix_nm(m,n):
    for i in range(1,n+1):
        for j in range(1,m+1):
            t[len(t)+1] = [i,j,len(t)+1,0]

print("")


#Player 'x' 
def move_x():
    eltlist = [] #collects 1 and 0 for "Board full"
    print("Player X's turn: ")
    input_move = possible_numbers()
    print(input_move)
    enter_val_int = int(input_move)
    print("")
    if t[enter_val_int][3] == 1: #if field not occupied t[input_move][3] = 0
        print_new_matrix(m,n)
        print("Already occupied. Try again")
        move_x()
    else:
        t[enter_val_int][2] = Fore.BLUE+'%-2s' % "X"+Fore.WHITE+Style.RESET_ALL #marks field on board
        t[enter_val_int][3] = 1   #all are 1 when board full
        for i in range(1,(m*n)+1):
            eltlist.append(t[i][3])  #creates element list 'eltlist' with len(all elts); all t[i][3]=0 in beginning
        print_new_matrix(m,n)
        update_matrix(t) #updates t 
        if win_line("#", win_strike) == True: #win_strike is set in beginning
            print("")
            print("Player 'X' Wins!")
            print("")
        elif all(eltlist):  #when all elts are 1, print"board full"
            print_new_matrix(m,n)
            update_matrix(t)
            print("Board full")
        else:
            move_o()  #sends to next player after move

#Player 'o'   
def move_o():
    eltlist = []  
    print("Player O's turn: ")
    input_move = possible_numbers()
    print(input_move)
    enter_val_int = int(input_move)
    print("")
    if t[enter_val_int][3] == 1:
        print_new_matrix(m,n)
        print("Already occupied. Try again")
        move_o()
    else:
        t[enter_val_int][2] = Fore.RED+'%-2s' % "O"+Fore.WHITE+Style.RESET_ALL 
        t[enter_val_int][3] = 1 
        for i in range(1,(m*n)+1):
            eltlist.append(t[i][3])
        print_new_matrix(m,n)
        update_matrix(t)
        if win_line("#", win_strike) == True:
            print("")
            print("Player 'O' Wins!")
            print("")
        elif all(eltlist):
            print_new_matrix(m,n)
            update_matrix(t)
            print("Board full")
        else:
            move_q()
            
#Player 'q'   
def move_q():
    eltlist = []
    print("Player #'s turn: ")
    input_move = possible_numbers()
    print(input_move)
    enter_val_int = int(input_move)
    print("")
    if t[enter_val_int][3] == 1:
        print_new_matrix(m,n)
        print("Already occupied. Try again")
        move_q()
    else:
        t[enter_val_int][2] = Fore.YELLOW+'%-2s' % "#"+Fore.WHITE+Style.RESET_ALL 
        t[enter_val_int][3] = 1 
        for i in range(1,(m*n)+1):
            eltlist.append(t[i][3])
        print_new_matrix(m,n)
        update_matrix(t)
        if win_line("#", win_strike) == True:
            print("")
            print("Player '#' Wins!")
            print("")
        elif all(eltlist):
            print_new_matrix(m,n)
            update_matrix(t)
            print("Board full")
        else:
            move_x()

#prints a line of a matrix
def print_line(m,n,x):
    for i in range(1,m+1):
        print('%-4s' % str(t[i+(x-1)*m][2]), end = " ")
        
#puts together lines of matrix and displays it
def print_matrix(m,n):
    for i in range(1,n+1):
        print_line(m,n,i)
        print("")

def print_line_new(line):
    for i in range(1,m+1):
        print('|  %-2s  ' %  str(t[i+(line)*m][2]), end="")
        
def print_new_matrix(m,n):
    print(" "+((m*7)-1)*"-")
    for i in range(n):
        print_line_new(i)
        print("|")
        print(m*7*"-")
        
m,n = set_matrix_size()

print_new_matrix(m,n)

f = []
for i in range(1,len(t)+1):
    f.append(t[i][2])

#creates x with n empty lists which should be filled with lines of matrix
#these lines make winning situation for line wins
x= []

#prints specific line of matrix
def matrixline(number_of_line,t_insert):
    h=[]
    for i in range(1,m+1):
        h.append(t_insert[i+(m*(number_of_line-1))][2]) #change t to t_insert
    return h

#adds matrix lines to x
def matrixline2(t_insert):
##    x= []
    for j in range(n):
        matrix_line = matrixline(j+1,t_insert)
        x.append(matrix_line)
        
matrixline2(t)

y=[]
def matrixrow(number_of_row,t_insert):
    h_row=[]
    for i in range(1,n+1):
        h_row.append(t_insert[(number_of_row-m)+(i*m)][2]) 
    return h_row

#adds matrix lines to x
def matrixrow2(t_insert):
    for j in range(m):
        matrix_row = matrixrow(j+1,t_insert)
        y.append(matrix_row)
matrixrow2(t)

z= []

#goes from left top to right bottom for every index number entered    
def schraeg_von_links_mit_zeile3(win_strike,t_insert,index):
    h_diag = []
    for k in range(win_strike):
        h_diag.append(t_insert[(k*m)+k+index][2])
    return h_diag

#goes from right top to bottom left for every index number entered    
def schraeg_von_rechts_mit_zeile3(win_strike,t_insert,index):
    h_diag = []
    for k in range(win_strike):
        h_diag.append(t_insert[(k*m)-k+index][2])
    return h_diag

def update_matrix(t_insert):
    global x_3
    x_3 = []
    global y_3
    y_3 = []
    global z_3
    z_3 = []
    global z_4
    z_4 = []
    for j in range(n):
        matrix_line = matrixline(j+1,t_insert)
        x_3.append(matrix_line)
    for k in range(m):
        matrix_row = matrixrow(k+1,t_insert)
        y_3.append(matrix_row)
    for i in range(1,m-(win_strike-1)+1): #from left top too bottom right, right up+left bottom  corner out
        for j in range(n-(win_strike-1)): #do it for all upper lines where win_strike possible 
            h_diag = schraeg_von_links_mit_zeile3(win_strike,t,i+j*m)
            z_3.append(h_diag)  
    for i2 in range(win_strike,m+1): #from r top to bottom l, l up and r down out
        for j2 in range(n-(win_strike-1)):#do it for all upper lines where win_strike possible 
            h_diag2 = schraeg_von_rechts_mit_zeile3(win_strike,t,i2+j2*m)
            z_3.append(h_diag2) 

update_matrix(t)

def create_win_row(symbol,k):
    global win_row
    win_row = []
    for i in range(1,k+1):
        win_row.append(symbol)
    return win_row

#checks for winner
def win_line(symbol, win_strike):
    win_row = create_win_row(symbol,win_strike)
    win_row_string = str(win_row).strip("[]")
    for i in range(len(x_3)):
        row_of_matrix_string = str(x_3[i]).strip("[]")
        if win_row_string in row_of_matrix_string:
            return True
    for j in range(len(y_3)):
        column_of_matrix_string = str(y_3[j]).strip("[]")
        if win_row_string in column_of_matrix_string:
            return True
    for k in range(len(z_3)):
        diag_of_matrix_string = str(z_3[k]).strip("[]")
        if win_row_string in diag_of_matrix_string:
            return True
move_x()
##move_q()
