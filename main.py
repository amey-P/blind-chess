#! usr/bin/python3

import sys,configparser
import chess
import play

WELCOME_MSG = """Welcome to blind-chess v0.01
Type "help" for more information
Type "new" for new a new game"""
HELP = """new/n : New game
quit/q/exit : Quit
"""
move_counter = 1
white = True

def listener():
    while True:
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
            if black == 'e' or white == 'engine':
                engine_name = input('Enter engine name : ')
                black=engine_name.upper()
                raise 
            elif black == "human" or white == "h" or white == "u":
                black='human'
                raise 
            else:
                print("Wrong Entry!")
    except:
        pass
    match = play.Match(white,black)
    verdict = match.play()
    if verdict == 'draw':
        print("Its a draw.")
    elif verdict == 'white':
        print("White won!")
    elif verdict == 'black':
        print("black won!")

def display(text):
    global white, move_counter
    if white:
        print('{0}'.format(move_counter),end='')
    print('\t{0}'.format(text),end='')
    if not white:
        print()
        move_counter+=1
    white = not white


if __name__ == '__main__':
    print(WELCOME_MSG)
    listener()
