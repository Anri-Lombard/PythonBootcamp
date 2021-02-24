import auction_art

print(auction_art.logo)

bidders = {}
is_more_bidders = True
while is_more_bidders:
    name = input("Type your name: ")
    bid_value = int(input("Type in your bid: $"))
    bidders[name] = bid_value
    answer = input("Type 'yes' if there are more bidders and 'no' to check the highest bidder: ")
    if answer == 'no':
        is_more_bidders = False

highest_bid = 0
winner = ""
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
    if highest_bid == bidders[key]:
        winner = key

print(f"\nThe highest bidder is {winner} with a bid of ${highest_bid}.\n")
print("Here were the all the bidders:")
for name in bidders:
    print(name + ": " + str(bidders[name]))
print("Thank you for bidding!")
