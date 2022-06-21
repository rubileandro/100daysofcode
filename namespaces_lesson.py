# Scope

# enemies = 1

# def increase_enemies():
# 	enemies = 2
# 	print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside fucntion: {enemies}")

# Local Scope

def drink_potion():
	potion_strength = 2
	print(potion_strength)

drink_potion()
# error 
print(potion_strength)

#Global Scope
player_health = 10
def drink_potion():
	potion_strength = 2
	print(player_health)

drink_potion()
print(player_health)

# player_health = 10

# def game():
# 	def drink_potion():
# 		potion_strength = 2
# 		print(player_health)

# game()
# print(player_health)
