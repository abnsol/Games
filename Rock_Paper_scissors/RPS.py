import sys
import random
from enum import Enum

count = 0
player_wins = 0
computer_wins = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    player = input("\nEnter \n1 for ROCK\n2 for PAPER\n3 for SCISSORS\n\n")
    if player not in ["1", "2", "3"]:
        print("you must input 1,2,3")
        return play_rps()
    player_choice = int(player)
    computer = int(random.choice("123"))
    print(f"\nYou chose {str(RPS(player_choice)).replace('RPS.', '')}.")
    print(f"Computer chose {str(RPS(computer)).replace('RPS.','')}.\n")

    if player_choice == 1 and computer == 3:
        global player_wins
        player_wins += 1
        print("🎉😎 YOU WIN!\n")
    elif player_choice == 2 and computer == 1:
        player_wins += 1
        print("🎉😎 YOU WIN!\n")
    elif player_choice == 3 and computer == 2:
        player_wins += 1
        print("🎉😎 YOU WIN!\n")
    elif player_choice == computer:
        print("👽 tie game!\n")
    else:
        global computer_wins
        computer_wins += 1
        print("🐍Computer wins!\n")

    
    global count
    count += 1

    print("\nwanna play again?")
    
    while True:
        playagain = input("if Yes press 1 \nelse press 2\n\n")
        if playagain not in ["1", "2"]:
            continue
        else:
            break

    if playagain == "1":
        return play_rps()
    else:
        print(f"you played RPS {str(count)} time!")
        print(f"computer have won {str(computer_wins)} time!")
        print(f"you have won {str(player_wins)} time!")
        print("Thank you for playing\n\n")
        sys.exit("Bye🖐")

play_rps()
