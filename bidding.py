from replit import clear
from art import logo

print(logo)
bids = {}  #AN empty dictionary
bidding_finished = False

while bidding_finished == False:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid price: $"))
  #Now add the key and value associated with it in the dictionary bids[key] = value
  bids[name] = bid
  should_continue = input(
      "Is there any bidder who wants to bid type 'yes' or 'no': ")
  if should_continue == "no":
    bidding_finished = True
  elif should_continue == "yes":
    clear()


def find_highest_bidder(bidding_records):
  name = ""
  highest_bid = 0
  for bidder in bidding_records:
    amount = bidding_records[bidder]
    if amount > highest_bid:
      highest_bid = amount
      name = bidder
  print(f"The highest bid is ${highest_bid} by {name} ")


find_highest_bidder(bids)
