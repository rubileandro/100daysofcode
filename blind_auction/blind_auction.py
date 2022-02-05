from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
# name = input('What is your name? Please enter your name. \n')
# bid = input('What is your bid? Pleae enter your bid \n')

#dict to keep track
name_and_bids = {}
# name_and_bids[name] = bid
# print(name_and_bids)
keepGoing = True
while keepGoing:
  #def bid_app():
    #print(logo)
    name = input('What is your name? Please enter your name. \n')
    bid = input('What is your bid? Pleae enter your bid \n')
    name_and_bids[name] = bid
    #print(name_and_bids)
    more_players = input('Are there any other bidders? Please types "Yes" or "No". \n').lower()
    if more_players == 'yes':
      clear()
      keepGoing = True
    else:
      keepGoing = False
      max_bid = max(name_and_bids, key=name_and_bids.get)
    #print('You are the winner! Congratulations')
      print(f'{max_bid} are the winner! Congratulations') 
