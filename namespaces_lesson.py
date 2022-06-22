# Scope

# enemies = 1

# def increase_enemies():
# 	enemies = 2
# 	print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside fucntion: {enemies}")

# Local Scope

# def drink_potion():
# 	potion_strength = 2
# 	print(potion_strength)

# drink_potion()
# # error 
# print(potion_strength)

# #Global Scope
# player_health = 10
# def drink_potion():
# 	potion_strength = 2
# 	print(player_health)

# drink_potion()
# print(player_health)

# player_health = 10

# def game():
# 	def drink_potion():
# 		potion_strength = 2
# 		print(player_health)

# game()
# print(player_health)

# There is no Block Scope 

# # This works
# game_level = 3
# enemies = ["Skeleton", "Zombies","Alien"]
# if game_level < 5:
# 	new_enemy = enemies[0]

# print(new_enemy)

# This doesn't work

# game_level = 3
# def create_enemy():
# 	enemies = ["Skeleton", "Zombies","Alien"]
# 	if game_level < 5:
# 		new_enemy = enemies[0]

# 	print(new_enemy)

# if you create a var within a func then it is only available wihtin that func.
# if you creat a vaar within a if/while/for or anyting that has the indentation and colon - then that does not count as creating a seperate local scope.

# Modifying Global Scope

# Global scope
# enemies = 1

# # function with local scope
# def increase_enemies():
# 	enemies = 2
# 	print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside fucntion: {enemies}")

# enemies = "Skeleton"

# # function with local scope
# def increase_enemies():
# 	enemies = "Zombie"
# 	print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside fucntion: {enemies}")

# enemies = 1

# # function with local scope
# def increase_enemies():
# 	# w/o the following line we cannot modify something that is global within a local scope
# 	# avoid modifing global scope in a func that has local scope
# 	global enemies
# 	enemies += 1
# 	print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside fucntion: {enemies}")

enemies = 1

def increase_enemies():
	print(f"enemies inside function: {enemies}")
	return enemies + 1

enemies = increase_enemies()
print(f"enemies outside fucntion: {enemies}")
