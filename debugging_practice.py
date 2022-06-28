############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

def my_function():
  # stop is ommited with range(). Therefore, i never reaches 20.
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
