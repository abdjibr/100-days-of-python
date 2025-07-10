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

    keep_running = True
    while keep_running:

        pick_cards = input("Are you ready to pick cards type yes\n").lower()
        if pick_cards == "yes":

            card_1_player = random.choice(cards)
            card_2_player = random.choice(cards)
            card_1_com = random.choice(cards)
            card_2_com = random.choice(cards)
            player_hand = [card_1_player, card_2_player]
            player_total =sum(player_hand)
            computer_hand = [card_1_com, card_2_com]
            computer_total = sum(computer_hand)
            print("\n"* 50)
            return player_hand, player_total, computer_hand, computer_total, card_1_player, card_2_player, card_1_com, card_2_com,
        else:
            print("wrong input try again")
            continue




keep_running = True


while keep_running:

    gamestart_yes_or_no = start()

    if gamestart_yes_or_no == "no":
        print("goodbye")
        break

    pl_hand, pl_total, com_hand, com_total,pl_card1,pl_card2,com_card1,com_card2 = dealer_gives_card()

    print("Player", ":", pl_hand, "=", pl_total,)
    print("computer",":",com_hand,"=", com_total)



    keep_running_1 = True

    pl_hand_total = 0
    com_hand_total = 0

    while keep_running_1:
        draw_new_card = ["yes", "no"]

        player_draw = input("Want to draw a new card? yes or no: \n").lower()

        print("\n"*100)

        if player_draw == "yes":

            new_card = random.choice(cards)  # just an integer now

            if new_card == 11:
                player_pick = int(input(f"You drew an Ace! Choose {cards[0]} or 1: "))
                if player_pick in [1, 11]:
                    pl_hand.append(player_pick)
                else:
                    print("Invalid choice, defaulting to 11.")
                    pl_hand.append(11)
            else:
                pl_hand.append(new_card)

            print("Player:", pl_hand, "=", sum(pl_hand))






        else:
            print("Player", ":", pl_hand, "=", sum(pl_hand),)



        new_card_computer = ["yes", "no"]
        computer_draw = random.choice(new_card_computer)

        if computer_draw == "yes":

            com_hand.append(random.choice(cards))

            print("Computer:",com_hand, "=",sum(com_hand))


        else:
            print("Computer:", com_hand, "=", sum(com_hand))

        if computer_draw == "no" and player_draw == "no":

            player_wins = sum(pl_hand) > sum(com_hand)
            if player_wins:
                print(f"Player wins with highest score:{sum(pl_hand)}")
                break
            computer_wins = sum(com_hand) > sum(pl_hand)
            if computer_wins:
                print(f"Computer wins with highest score:{sum(com_hand)}")
                break
            else:
                print(f"its a draw the scores are the same: {sum(pl_hand)} and {sum(com_hand)}")
                break

        pl_hand_total = sum(pl_hand)
        com_hand_total = sum(com_hand)

        game_stops = pl_hand_total > 21 or com_hand_total > 21
        if game_stops:

            if pl_hand_total > 21 and com_hand_total > 21:
                result = "its a draw, you both lost"
                print(result)
                break

            if pl_hand_total > 21:
                print("Player: you have lost")
                if not com_hand_total > 21:
                    print("Computer: you win")
                    keep_running_1 = False

            if com_hand_total > 21:
                print("Computer: you have lost")
                if not pl_hand_total > 21:
                    print("Player: you win")
                    keep_running_1 = False
















