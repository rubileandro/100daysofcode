import random

from art import logo
from art import vs

from game_data import data

#from replit import clear

# TODO 1: print logo

print(logo)
print("Compare A:")


# TODO 2: print vs

print(vs)
print("Against B:")

print("Who has more followers? Type 'A' or 'B': ")


# TODO 3: select random dictionary from list and print in formatted way under logo - assign A
# def against_a():
#   pass


def against_b():
  random_selection = random.choice(data)
  # print(random_selection)
  random_index = data.index(random_selection)
  random_name = data[random_index]['name']
  random_description = data[random_index]['description']
  random_country = data[random_index]['country']
  print(f"{random_name}, a {random_description}, from {random_country}.")


against_b()

#against_b
  
## status of guess when right
score = 0
#print(f"You're right! Current score is: {score}")

## status of guess when wrong
#print(f"Sorry, that's wrong. Final score is: {score}")



# TODO 4: select another random disctionary from list and print in formatted way under vs - assign B


# TODO 5: ask user to select A or B
player_choice = input("Choose A or B: ").lower()
print(player_choice)


# TODO 6: compare follower account from A and B and determine which is higher. If user's guess matches the result.....
