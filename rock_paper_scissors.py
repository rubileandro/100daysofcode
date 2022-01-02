import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Instruction and input 
person_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')

# Convert str. to int.
person_choice = int(person_choice)

# Random chocie 
computer_choice = random.randint(0,2)

# Persons chocie
if person_choice == 0:
  print(rock)
elif person_choice == 1:
  print(paper)
else:
  print(scissors)

# Computer's choice
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

# Error message and game status
if person_choice <0 or person_choice >2:
  print('Your input must be 0, 1, 2')
  if person_choice == computer_choice:
    print('Draw')
    if person_choice == 0 and computer_choice == 2:
      print('You win!')
      if person_choice == 2 and computer_choice == 1:
        print('You win!')
        if person_choice == 1 and computer_choice == 0:
          print('You win!')
    else:
      print('You lose.')
