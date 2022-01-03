# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

# How long is the list?
length_of_list = 0
for height in student_heights:
    length_of_list += 1
#print or return?
print (length_of_list)
        
#Adding the numbers using a loop
combined_heights = 0
for height in student_heights:
    combined_heights += height

# Calc average total / number of items
average_height = combined_heights / length_of_list

# Round result and give result
print(round(average_height))
