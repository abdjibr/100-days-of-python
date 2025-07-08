import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def start ():

    start_the_game = input("Would you start the game yes or no\n").lower()
    if start_the_game == "yes":
        start_the_game = "welcome"
        print("\n"*50)

    return start_the_game



def dealer_gives_card():

    import art
    print(art.logo)
    print("Welcome to the game")
    pick_cards = input("Are you ready to pick cards type yes\n")
    if pick_cards == "yes":

        player = random.choice(cards), random.choice(cards)
        computer = random.choice(cards), random.choice(cards)

    return f"player 1:{player}\ncomputer:{computer}"





keep_running = True

while keep_running:

    gamestart_yes_or_no = start()

    if gamestart_yes_or_no == "no":
        print("goodbye")
        break

    print(dealer_gives_card())



