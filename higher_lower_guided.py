from art import logo, vs
from game_data import data
import random

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  
# Display art 
print(logo)

# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Compare B: {format_data(account_b)}")

# Ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct
## Get follower count of each account.
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]



# Give user feedback on thier guess.

# Score keeping.

# Make the game repeatable.

# Making teh account at position B become the next account at position A 

# Clear the screen between rounds.

