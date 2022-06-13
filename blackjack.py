import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  card_dealt = random.choice(cards)
  return card_dealt

selected_card = deal_card()
print(selected_card)
