#Using Python enumerate() With for Loops
#https://youtu.be/nI-jkrJxlz0\
#In Python, a for loop is usually written as a loop over an iterable object. This means that you don’t need a counting variable to access items in the iterable. Sometimes, though, you do want to have a variable that changes on each loop iteration. Rather than creating and incrementing a variable yourself, you can use Python’s enumerate() to get a counter and the value from the iterable at the same time!"

# Method 1
# seasons = ["Spring", "Summer", "Fall", "Winter"]
# count = 1

# for season in seasons:
#     print(count,season)
#     count += 1

# Method 2
# seasons = ["Spring", "Summer", "Fall", "Winter"]

# for count in range(len(seasons)):
#     # +1 so that it starts at 1 and not zero
#     print(count+1, seasons[count])

# Method 3 Enumerate
seasons = ["Spring", "Summer", "Fall", "Winter"]

for count, season in enumerate(seasons, start=1):
    print(count,season)
