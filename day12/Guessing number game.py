import random

def easy_mode():

    number = random.randint(1,100)
    attempts_remaining = 5
    keep_going = True

    while keep_going:
        user_easy = input("Guess the number\n")
        if user_easy == number:
            print("You won! refresh the page to play again")
            keep_going = False
        else:
            if attempts_remaining == 0:
                print(f"you have {attempts_remaining} attempts left. ")
                break

            attempts_remaining -= 1
            print(f"you guessed wrong you have {attempts_remaining}attempts left")



print("Welcome to the guessing game")

user = input("type start to begin the game\n")

easy = 10
hard = 5
if user == "start":
    user_inside_game = input("choose between hard or easy mode\n")
    if user_inside_game == "hard":
        print(f"you have {hard}attempts")
    else:
        print(f"you have {easy} attempts")
        easy_mode()
