import random
import sys
import argparse


def guess_number_game(player="Player"):
    game_counts = 0
    player_wins = 0
    win_percentage = 0.0

    def play_game():
        nonlocal player, game_counts, player_wins, win_percentage

        player_guess = int(
            input(f"\n{player}, guess which number I'm thinking of... 1, 2 or 3.\n")
        )

        if player_guess not in [1, 2, 3]:
            print(f"{player}, please enter 1, 2 or 3.\n")
            return play_game()

        computer_guess = random.randint(1, 3)

        print(f"\n{player}, you chose {player_guess}.")
        print(f"I was thinking about the number {computer_guess}.")

        def decide_winner(player_guess, computer_guess):
            nonlocal player_wins
            if player_guess == computer_guess:
                player_wins += 1
                return f"\n{player}, you win! 🎉"
            else:
                return f"\nSorry, {player}. Better luck next time. 😢"

        winner = decide_winner(player_guess, computer_guess)
        print(winner)

        game_counts += 1
        win_percentage = player_wins / game_counts

        print(f"\nGame counts: {game_counts}")
        print(f"\nPlayer's wins: {player_wins}")
        print(f"\nYour winning percentage: {win_percentage:.2%}")

        while True:
            play_again = str(input(f"\nPlay again, {player}? (y/n)\n"))

            if play_again.lower() not in ["y", "n"]:
                continue
            else:
                if play_again.lower() == "y":
                    return play_game()
                else:
                    if __name__ == "__main__":
                        print(f"\nThank you for playing, {player}!🫰")
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

    guess_number = guess_number_game(args.name)
    guess_number()
