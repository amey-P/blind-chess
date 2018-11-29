#! usr/bin/python3

import sys,configparser
import chess
import play

WELCOME_MSG = """Welcome to blind-chess v0.01"""
NEW_GAME = """Type "help" for more information
Type "new" for new a new game"""
HELP = """new/n : New game
quit/q/exit : Quit
"""

match = None

def listener():
    while True:
        print(NEW_GAME)
        inp = input().strip()
        if inp == 'help' or inp == 'h':
            print(HELP)
        elif inp == 'new' or inp == 'n':
            new_game()
        elif inp == 'quit' or inp == 'q' or inp == 'exit':
            sys.exit(0)
        else:
            print('Incorrect value.\nType "help" for more information\nType "new" for new a new game')


def new_game():
    global match
    white=None
    black=None
    try:
        while True:
            white = input("White Player (engine/e or human/h/u): ").strip()
            if white == 'e' or white == 'engine':
                engine_name = input('Enter engine name : ')
                white=engine_name.upper()
                raise
            elif white == "human" or white == "h" or white == "u":
                white='human'
                raise 
            else:
                print("Wrong Entry!")
    except:
        pass
    try:
        while True:
            black = input("Black Player (engine/e or human/h/u): ").strip()
            if black == 'e' or black == 'engine':
                engine_name = input('Enter engine name : ')
                black=engine_name.upper()
                raise 
            elif black == "human" or black == "h" or black == "u":
                black='human'
                raise 
            else:
                print("Wrong Entry!")
    except:
        pass
    print('\x1b[2J\x1b[2K\x1b[0;0f',end='')
    match = play.Match(white,black, display=display, input_function=inp_function, error=error)
    verdict = match.play()
    if verdict == 'draw':
        print("\nIts a draw.")
    elif verdict == 'white':
        print("\nWhite won!")
    elif verdict == 'black':
        print("\nBlack won!")

def inp_function():
    global match
    white = match.board.turn
    move_counter = len(match.board.move_stack)+1
    move_counter = move_counter//2 + move_counter%2
    if not move_counter:
        move_counter=1
    if white:
        print('{0}.\t'.format(move_counter),end='')
    else:
        print("\t",end="")
    move = input()
    rewrite()
    return move

def rewrite():
    global match
    white = True
    moves = match.moves
    print('\x1b[2J\x1b[2K\x1b[0;0f',end='')
    for x,num in zip(moves,range(1,len(moves)+1)):
        display(x, white, num//2+num%2)
        white = not white

def display(text, white=None, move_counter=None):
    global match
    if white is None:
        white = not match.board.turn
    if move_counter is None:
        move_counter = len(match.board.move_stack)//2+ len(match.board.move_stack)%2
    if white:
        print('{0}.'.format(move_counter),end='')
    print('\t{0}'.format(text),end='')
    if not white:
        print()

def error(msg):
    if msg=="Invalid Move":
        return rewrite()

if __name__ == '__main__':
    print(WELCOME_MSG)
    listener()
