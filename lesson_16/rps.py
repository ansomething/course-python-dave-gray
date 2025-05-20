import sys
import random
from enum import Enum
import argparse


def rps_game(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_game():
        nonlocal player_wins, python_wins, name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = int(
            input(
                f"\n{name}, please enter...\n[1] for Rock\n[2] for Paper\n[3] for Scissors\n"
            )
        )
        computerchoice = random.randint(1, 3)

        if playerchoice not in [1, 2, 3]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_game()

        print(f"\n{name} chose: {str(RPS(playerchoice)).replace('RPS.', '').title()}.")
        print(f"Python chose: {str(RPS(computerchoice)).replace('RPS.', '').title()}.")

        def decide_winner(playerchoice, computerchoice):
            nonlocal player_wins, python_wins, name
            if playerchoice == 1 and computerchoice == 3:
                player_wins += 1
                return f"\n{name} wins!🎉"
            elif playerchoice == 2 and computerchoice == 1:
                player_wins += 1
                return f"\n{name} wins!🎉"
            elif playerchoice == 3 and computerchoice == 2:
                player_wins += 1
                return f"\n{name} wins!🎉"
            elif playerchoice == computerchoice:
                return f"\nTie game!🫢"
            else:
                python_wins += 1
                return f"\nPython wins!🐍\nSorry, {name}..."

        game_result = decide_winner(playerchoice, computerchoice)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"Python wins: {python_wins}")

        while True:
            playagain = str(input(f"\n{name}, do you want to play again? (y/n)\n"))

            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                if playagain.lower() == "y":
                    return play_game()
                else:
                    if __name__ == "__main__":
                        print(f"\nThank you for playing, {name}!🫰")
                        sys.exit("Bye, bye!👋")
                    else:
                        return

    return play_game


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    rock_paper_scissors = rps_game(args.name)
    rock_paper_scissors()
