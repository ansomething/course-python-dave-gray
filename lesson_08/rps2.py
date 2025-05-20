import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:

    playerchoice = int(
        input("\nEnter...\n[1] for Rock\n[2] for Paper\n[3] for Scissors\n")
    )
    computerchoice = random.randint(1, 3)

    if playerchoice < 1 or playerchoice > 3:
        sys.exit("You must enter 1, 2 or 3.")

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

    playagain = str(input("\nPlay again? (y/n)\n"))
    if playagain.lower() == "y":
        continue
    else:
        print("\nThank you for playing!🫰")
        playagain = False

sys.exit("Goodbye!👋")
