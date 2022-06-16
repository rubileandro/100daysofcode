import random

# deal cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card_dealt = random.choice(cards)
  return card_dealt

user_cards = []
computer_cards = []

for entry in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

# calculate score
def calculate_score(list_of_cards):
  if (11 and 10 in list_of_cards):
    return 0
  return sum(list_of_cards)
  
user_score = calculate_score(user_cards)
print(user_score)
