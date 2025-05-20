import sys
from rps import rps_game
from guess_number import guess_number_game
import argparse


def arcade_menu(player="Player"):

    print(f"\n{player}, welcome to the Arcade! 🤖")
    print(
        "\nPlease, choose a game:\n" "1 = Rock, Paper, Scissors\n" "2 = Guess My Number"
    )
    print('\nOr press "x" to exit the Arcade')

    player_input = str(input(""))

    def player_choice(player_input):
        if player_input.lower() not in ["1", "2", "x"]:
            print(f"\n{player}, please enter 1, 2 or x.")
            return arcade_menu(player)

        if player_input == "1":
            rps = rps_game(player)
            rps()
            return arcade_menu(player)
        elif player_input == "2":
            guess_number = guess_number_game(player)
            guess_number()
            return arcade_menu(player)
        else:
            sys.exit(f"\nSee you next time, {player}!\n\nBye, bye!👋")

    player_choice(player_input)

    return arcade_menu


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the arcade.",
    )

    args = parser.parse_args()

    arcade = arcade_menu(args.name)
    arcade()
