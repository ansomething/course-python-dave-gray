import sys
import random
from enum import Enum


def play_game():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = int(
        input("\nEnter...\n[1] for Rock\n[2] for Paper\n[3] for Scissors\n")
    )
    computerchoice = random.randint(1, 3)

    if playerchoice not in [1, 2, 3]:
        print("You must enter 1, 2 or 3.")
        return play_game()

    print("\nYou chose: " + str(RPS(playerchoice)).replace("RPS.", "").title())
    print("Python chose: " + str(RPS(computerchoice)).replace("RPS.", "").title())

    if playerchoice == 1 and computerchoice == 3:
        print("\nYou win!🎉")
    elif playerchoice == 2 and computerchoice == 1:
        print("\nYou win!🎉")
    elif playerchoice == 3 and computerchoice == 2:
        print("\nYou win!🎉")
    elif playerchoice == computerchoice:
        print("\nTie game!🫢")
    else:
        print("\nPython wins!🐍")

    while True:
        playagain = str(input("\nPlay again? (y/n)\n"))
        if playagain.lower() not in ["y", "n"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_game()
    else:
        print("\nThank you for playing!🫰")
        sys.exit("Goodbye!👋")


play_game()
