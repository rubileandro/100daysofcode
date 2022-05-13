print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print('You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
choice = input("Left or right?\n").lower()

if choice == "right":
  print('You\'ve come to a dark lake. There is an island in the middle of the lake. Type "wait" to wait for a Charon to come and ferry you across. Type "swim" to attempt to swim across.')
  choice = input("Swim or Wait?\n").lower()
  if choice == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    choice = input("Red, Yellow or Blue?\n").lower()
    if choice == "red":
      print("The door bursts open with flames and you die. Game Over.")

    elif choice == "yellow":
      print("You win. You find a room full of gold from a lost civilization and a key to get out of this nightmare.")

    elif choice == "blue":
      print("You get eaten by strange beasts. Game Over.")
    
    else:
      print("That is not a recognized input - it takes you straight to hell. Game Over.")
      
  else:
    print("You are attacked by Cthulhu. Game Over.")
else:
  print("You fall into a hole. Game Over.")
