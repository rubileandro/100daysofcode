import random

from art import logo
from art import vs

from game_data import data

#from replit import clear

# TODO 1: print logo

print(logo)

## Global variables?
random_selection = random.choice(data)

# format random selection
def format(selection):
  """Takes in the dictionary entries and return in readable format"""
  random_index = data.index(random_selection)
  random_name = data[random_index]['name']
  random_description = data[random_index]['description']
  random_country = data[random_index]['country']
  return f"{random_name}, a {random_description}, from {random_country}."

# follower count for comparison 
a_followers = data[data.index(random_selection)]['follower_count']
b_followers = data[data.index(random_selection)]['follower_count']

# Compare A function


def against_a():
  random_a = random_selection
  print(f"Compare A: {format(random_a)}")
against_a()

# TODO 2: print vs

print(vs)


# TODO 3: select random dictionary from list and print in formatted way under logo - assign A

# Compare B function
def against_b():
  random_b = random_selection
  print(f"Against B: {format(random_b)}")
against_b()

# TODO 5: ask user to select A or B
player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
#print(player_choice)
#against_b
  
## status of guess when right
#score = 0

#CONTINUE FUNCTION update compare_a with previous compare_b and generate new item for compare_b
def continue_game():
  print(logo)

  #calling the details from the previous B results
  def update_a():
   random_index_b = data.index(random_selection_b)
   random_name_b = data[random_index_b]['name']
   random_description_b = data[random_index_b]['description']
   random_country_b = data[random_index_b]['country']
  
   print(f"You're correct. Compare A: {random_name_b}, a {random_description_b}, from {random_country_b}.")   
    
  
  update_a()

  print(vs)

#calling new random B results
  random_selection_new_b = random.choice(data)
  def update_b():
    random_index_b = data.index(random_selection_new_b)
    random_name_b = data[random_index_b]['name']
    random_description_b = data[random_index_b]['description'] 
    random_country_b = data[random_index_b]['country']
    
    print(f"Compare B: {random_name_b}, a {random_description_b}, from {random_country_b}.")  

  update_b()

# TODO 6: compare follower account from A and B and determine which is higher. If user's guess matches the result.....
def compare_ab(a_followers, b_followers):
  score = 0
  if b_followers > a_followers and player_choice == "b":
    score += 1
    continue_game()
  elif b_followers > a_followers and player_choice == "b":
    print(logo)
    print(f"Sorry you are wrong. Your score is {score}")
  elif a_followers > b_followers and player_choice == "a":
    score += 1
    continue_game()
  else:
    print(logo)
    print(f"Sorry you are wrong. Your score is {score}")
   #code to stop game running 

compare_ab(a_followers, b_followers)

# while continue_game == True:
#   continue_game()

## status of guess when wrong
#print(f"Sorry, that's wrong. Final score is: {score}")

# TODO 4: select another random disctionary from list and print in formatted way under vs - assign B


