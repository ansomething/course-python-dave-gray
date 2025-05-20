import sys
import random
from enum import Enum


def game():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_game():
        nonlocal player_wins, python_wins

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

        print(f"\nYou chose: {str(RPS(playerchoice)).replace('RPS.', '').title()}.")
        print(f"Python chose: {str(RPS(computerchoice)).replace('RPS.', '').title()}.")

        def decide_winner(playerchoice, computerchoice):
            nonlocal player_wins, python_wins
            if playerchoice == 1 and computerchoice == 3:
                player_wins += 1
                return "\nYou win!🎉"
            elif playerchoice == 2 and computerchoice == 1:
                player_wins += 1
                return "\nYou win!🎉"
            elif playerchoice == 3 and computerchoice == 2:
                player_wins += 1
                return "\nYou win!🎉"
            elif playerchoice == computerchoice:
                return "\nTie game!🫢"
            else:
                python_wins += 1
                return "\nPython wins!🐍"

        game_result = decide_winner(playerchoice, computerchoice)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\nPlayer wins: {player_wins}")
        print(f"Python wins: {python_wins}")

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

    return play_game


rock_paper_scissors = game()

if __name__ == "__main__":
    rock_paper_scissors()
