from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

bidder_list = {}
should_end = False
winner_list = []

def bidding_list(bidder_name, bidder_bid):
  bidder_list[bidder_name] = bidder_bid
  # bidder_list.append(bid_data)
  # print(bidder_list)

#find the highest bidder

def highest_bidder(bidder_list):
  highest_bid = 0
  name = ""
  for key in bidder_list:
    # print(key)
    bid = bidder_list[key]
    if bid > highest_bid:
      highest_bid = bid
      name = key
      # print(highest_bid)
  winner_list.append(name)
  winner_list.append(highest_bid)
           
print(logo)
print("Welcome to the secret auction program.")

while not should_end:
  name = input("What is your name?: ")
  bid = int(input("what's your bid?: $"))
  
  bidding_list(bidder_name=name, bidder_bid=bid)
  
  loop = input("Are there any other bidders? Type 'yes' or 'no': ")
  clear()
  if loop == "no":
    should_end = True
    highest_bidder(bidder_list)
    # print(winner_list)
    print(f"The winner is {winner_list[0]} with a bid of ${winner_list[1]}.")

  


# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   #Try running the program and entering a shift number of 45.
#   #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#   #Hint: Think about how you can use the modulus (%).
#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")