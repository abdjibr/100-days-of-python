import random

def easy_mode():

    number = random.randint(1,100)
    attempts_remaining = 10
    keep_going = True

    while keep_going:
        try:
            user_easy = int(input("Guess the number\n"))
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if user_easy == number:

            print("You won! refresh the page to play again")
            keep_going = False

        else:
            if attempts_remaining == 1:
                print(f"The correct number was {number}. Better luck next time!")

                break

            attempts_remaining -= 1
            print(f"you guessed wrong you have {attempts_remaining} attempts left")

def hard_mode():

    number = random.randint(1,100)
    attempts_remaining = 5
    keep_going = True

    while keep_going:
        try:
            user_easy = int(input("Guess the number\n"))
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if user_easy == number:
            print("You won! refresh the page to play again")
            keep_going = False
        else:
            if attempts_remaining == 1:
                print(f"The correct number was {number}. Better luck next time!")

                break

            attempts_remaining -= 1
            print(f"you guessed wrong you have {attempts_remaining} attempts left")


print("Welcome to the guessing game")

user = input("type start to begin the game\n").lower().strip()
print("\n"*40)
easy = 10
hard = 5
if user == "start":
    user_inside_game = input("choose between hard or easy mode\n").lower().strip()
    print("\n" * 40)
    if user_inside_game == "hard":
        print(f"you have {hard} attempts")
        hard_mode()
    else:
        print(f"you have {easy} attempts")
        easy_mode()
