import random

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
