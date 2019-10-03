# -*- coding: utf-8 -*-
import random

#7-8-9
#4-5-6
#1-2-3



def display_board(board):
    print("    |   |    ")
    print(" {}  | {} | {} ".format(board[7],board[8],board[9]))
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print(" {}  | {} | {} ".format(board[4],board[5],board[6]))
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print(" {}  | {} | {} ".format(board[1],board[2],board[3]))
    print("    |   |    ")
    
    
    
def player_input():
    global player1
    global player2
    player1 = input("Please pick a marker 'X' or 'O':")
    while player1.lower()!="x" and player1.lower()!="o" :
        print("You entered wrong. You must enter X or O.")
        player1 = input("Please pick a marker 'X' or 'O':")
    
    player1 = player1.upper();
    if player1=="X":
        player2="O"
    else:
        player2="X"
        
def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board, mark):
    for i in range(1,8,3):
        if board[i:i+3]==[mark,mark,mark]:
            return True
        
    for i in range(1,4):
        if board[i::3]==[mark,mark,mark]:
            return True
    
    
    if board[3:8:2]==[mark,mark,mark]:
        return True
    if board[1:10:4]==[mark,mark,mark]:
        return True
    return False

def choose_first():
    return random.randint(1,2)
     
def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        return False
    
def full_board_check(board):
    for i in board:
        if i==" ":
            return False
    else:
        return True
    
def player_choice(board):
    position = int(input("Your next position[1-9]:"))
    while not space_check(board,position):
        position = int(input("Enter again. Your next position[1-9]:"))
    else:
        return position

def replay():
    answer = input("Do you want to play again?(Y/N):")
    if answer[0].lower()=="y":
        return True
    else:
        return False
    
print('Welcome to Tic Tac Toe!')

while True:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1 = None
    player2 = None
    turn=None
    
    player_input()
    if choose_first()==1:
        turn = 1
        print("First player plays first.")
    else:
        turn = 2
        print("Second player plays first.")
    
    while not full_board_check(test_board) :
        if turn == 1:
            print("Player1:")
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player1,position)
            turn = 2
        else : 
            print("Player2:")
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player2,position)
            turn = 1
        
        if win_check(test_board,player1):
            print("Player1 won.")
            break
        elif win_check(test_board,player2):
            print("Player2 won.")
            break
    if not replay():
        break
    
    
    
    
