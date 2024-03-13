import replit

import art

print(art.logo)
bid_per_person = {}

while input("Enter new bidder? y/n: ").lower() == "y":
  replit.clear()
  name = input("Enter name: ")
  bid = int(input("Enter bid: "))
  bid_per_person[name] = bid

if len(bid_per_person) > 0:
  highest_bid = 0
  highest_bidder = ""
  for bidder in bid_per_person:
    if bid_per_person[bidder] > highest_bid:
      highest_bid = bid_per_person[bidder]
      highest_bidder = bidder
  print(f"Highest bidder is {highest_bidder} with a bid of {highest_bid}")
else:
  print("No bids entered")
