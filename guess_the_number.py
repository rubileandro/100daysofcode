#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

print(logo)
print("Welcome to the number guessing game!")

ANSWER = randint(1, 100)
print(ANSWER)

difficulty = input("Choose a difficulty. Type 'e' for Easy or 'h' for Hard.")
print(difficulty)
#turns_remaining = 0
if difficulty == "e":
  turns_remaining = 10
elif difficulty == "h":
  turns_remaining = 5

guess = int(input("Guess a number between 1-100:"))

def guess_game(): 
  if guess > ANSWER:
    print("Too high.")
  elif guess < ANSWER:
    print("Too low.")
  elif guess == ANSWER:
    print(f"You guessed the correct {ANSWER}, you win!")
  else:
    print("Not a valid number.")

while turns_remaining > 0:
  if guess != ANSWER:
    turns_remaining -= 1
    print(turns_remaining)
    guess = int(input("Guess another number between 1-100:"))
    guess_game()
print ("game over")

guess_game(guess, ANSWER)
