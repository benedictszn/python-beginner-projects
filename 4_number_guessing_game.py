# project 4: number guessing game
# the computer picks a secret number and you try to guess it.
# after each guess you are told if you need to go higher or lower

import random


def play_round():
    # pick a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guesses = 0

    print()
    print("i'm thinking of a number between 1 and 100")

    while True:
        answer = input("your guess: ").strip()

        # make sure the user typed a whole number
        if not answer.isdigit():
            print("please type a whole number")
            continue

        guess = int(answer)
        guesses = guesses + 1

        if guess < secret_number:
            print("too low, try higher")
        elif guess > secret_number:
            print("too high, try lower")
        else:
            print(f"correct! you got it in {guesses} guesses")
            return guesses


def main():
    best_score = None

    while True:
        score = play_round()

        # keep track of the fewest guesses so far
        if best_score is None or score < best_score:
            best_score = score
        print("your best score is", best_score, "guesses")

        again = input("play again? (y/n): ").strip().lower()
        if again != "y":
            print("thanks for playing!")
            break


if __name__ == "__main__":
    main()
