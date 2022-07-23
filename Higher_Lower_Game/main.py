import random

from art import logo
from art import vs

from game_data import data

# format random selection
def format(selection):
  """Takes in the dictionary entries and return in readable format"""
  random_name = selection['name']
  random_description = selection['description']
  random_country = selection['country']
  return f"{random_name}, a {random_description}, from {random_country}."

# compare A and B
def compare_ab(player_choice, a_followers, b_followers):
  """takes in player choice and checks it against the higher follower count"""
  if b_followers > a_followers and player_choice == "b":
    return player_choice == "b"
  elif a_followers > b_followers and player_choice == "a":
     return player_choice == "a"   

# Print logo
print(logo)

# status at beginning
score = 0
continue_game = True

## Global variables
random_b = random.choice(data)

# Fucntion to continue game
while continue_game:
  random_a = random_b
  random_b = random.choice(data)

  while random_a == random_b:
    random_b = random.choice(data)

  print(f"Compare A: {format(random_a)}")

  print(vs)

  print(f"Against B: {format(random_b)}")

  # Ask user to select A or B
  player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  # follower count for comparison and did player choose correctly?
  a_followers = random_a['follower_count']
  b_followers = random_b['follower_count']
  is_correct = compare_ab(player_choice, a_followers, b_followers)

# user feedback and scorekeeping
  if is_correct:
    print(logo)
    score +=1
    print(f"You're right! Current score: {score}.")
  else:
    continue_game = False
    print(f"Sorry, that's wrong. Final score: {score}.")
