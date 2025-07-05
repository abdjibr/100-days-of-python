
def find_highest_bid(bidding_dic): #def func. to find the highest bid and its logic
    winner = "" #placeholder for the winner
    highest_bid = 0 #placeholder for their bids

    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount #replace if bid_amount is larger
            winner = bidder

    return winner




final_result_auction = {} #every key&value will be collected here

keep_bidding = True #keeps the loop running

while keep_bidding:

    name = input("Whats your name\n ")
    bid = int(input("Whats your bid\n $ "))

    final_result_auction[name]=bid #adds to the dictionary directly

    new_bid = input("New bid Yes or No?\n ").lower()

    if new_bid == "yes":
        print("\n"*100) #creates a new page
        continue # starting the code from the top

    else:
        keep_bidding = False #stops the loop
        print("\n" * 100)
        winner_name = find_highest_bid(final_result_auction) # creating a variable for the winner
        #printing the winner and their bid
        print(f"the winner is {winner_name} with a bid of {final_result_auction[winner_name]}")










