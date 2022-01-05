#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Letters
# Shuffle (reorganize the order of the list items)
for letter in letters:
  random.shuffle(letters)
#print(letters) test

# get legnth from random list
  chosen_letters = letters[:nr_letters]
#print(chosen_letters) test

# Numbers
for number in numbers:
  random.shuffle(numbers)
#print(numbers) test

  chosen_numbers = numbers[:nr_numbers]
#print(chosen_numbers) test

# Symbols
for symbol in symbols:
  random.shuffle(symbols)
#print(symbols) test

  chosen_symbols = symbols[:nr_symbols]
#print(chosen_symbols) test

# # combine random lists of user specified length from each category
password = chosen_letters + chosen_numbers + chosen_symbols

# Shuffle final str
random.shuffle(password)
# lst to str
pass_str = ''.join(password)
# print(password)
print(f'Your passowrd is {pass_str}')
