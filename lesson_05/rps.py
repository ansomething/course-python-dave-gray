import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerchoice = int(input("Enter...\n[1] for Rock\n[2] for Paper\n[3] for Scissors\n"))
computerchoice = random.randint(1, 3)

if playerchoice < 1 or playerchoice > 3:
    sys.exit("You must enter 1, 2 or 3.")

print("")
print("You chose: " + str(RPS(playerchoice)).replace("RPS.", ""))
print("Python chose: " + str(RPS(computerchoice)).replace("RPS.", ""))
print("")

if playerchoice == 1 and computerchoice == 3:
    print("You win!🎉")
elif playerchoice == 2 and computerchoice == 1:
    print("You win!🎉")
elif playerchoice == 3 and computerchoice == 2:
    print("You win!🎉")
elif playerchoice == computerchoice:
    print("Tie game!🫢")
else:
    print("Python wins!🐍")
