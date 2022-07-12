import random

from art import logo
from art import vs

from game_data import data

#from replit import clear

# TODO 1: print logo

print(logo)

## Global variables?
random_selection_a = random.choice(data)
random_selection_b = random.choice(data)

# follower count for comparison 
a_followers = data[data.index(random_selection_a)]['follower_count']
b_followers = data[data.index(random_selection_b)]['follower_count']


# Compare A function
def against_a():
  #random_selection_a = random.choice(data)
  # print(random_selection)
  random_index_a = data.index(random_selection_a)
  random_name = data[random_index_a]['name']
  random_description = data[random_index_a]['description']
  random_country = data[random_index_a]['country']
  
  print(f"Compare A: {random_name}, a {random_description}, from {random_country}.")
  
against_a()

# TODO 2: print vs

print(vs)


# TODO 3: select random dictionary from list and print in formatted way under logo - assign A

# Compare B function
def against_b():
  #random_selection_b = random.choice(data)
  # print(random_selection)
  random_index_b = data.index(random_selection_b)
  random_name = data[random_index_b]['name']
  random_description = data[random_index_b]['description']
  random_country = data[random_index_b]['country']
  
  print(f"Compare B: {random_name}, a {random_description}, from {random_country}.")


against_b()

# TODO 5: ask user to select A or B
player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
#print(player_choice)
#against_b
  
## status of guess when right
score = 0

# Compare function
def compare_ab(a_followers, b_followers):
  if b_followers > a_followers:
    print(f"B Wins with {b_followers}")
  elif b_followers == a_followers:
    print("No one Wins")
  if b_followers < a_followers:
    print(f"A Wins with {a_followers}")

compare_ab(a_followers, b_followers)
#print(f"You're right! Current score is: {score}")

## status of guess when wrong
#print(f"Sorry, that's wrong. Final score is: {score}")



# TODO 4: select another random disctionary from list and print in formatted way under vs - assign B





# TODO 6: compare follower account from A and B and determine which is higher. If user's guess matches the result.....
