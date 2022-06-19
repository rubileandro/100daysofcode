import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card_dealt = random.choice(cards)
  return card_dealt

def calculate_score(list_of_cards):
  """Take a list of cards and return the score calculated from the cards"""
  #if 11 in list_of_cards and 10 in list_of_cards and len(list_of_cards) == 2:
  if sum(list_of_cards) == 21 and len(list_of_cards) ==2:
    return 0
  if 11 in list_of_cards and sum(list_of_cards) > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
  return sum(list_of_cards)

user_cards = []
computer_cards = []
end_of_game = False

for entry in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not end_of_game:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f" Your cards: {user_cards}, current score: {user_score}")
  print(f" Computer's first card: {computer_cards[0]}")
  
  if user_score == 0 or computer_score == 0 or user_score > 21:
    end_of_game = True
  else:
    deal_another_card = input("Type 'y' to get another card, type 'n' to pass.\n")
    if deal_another_card == "y":
      user_cards.append(deal_card())
    else:
      end_of_game = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
