# file = open("myfile.txt")
# contents = file.read()
# print(contents)
# file.close()

# # with - don't have to remember to close the file.
# with open("myfile.txt") as file:
#     contents = file.read()
#     print(contents)

# w parameter to make file writable
with open("myfile.txt", mode="w") as file:
    file.write("Today was a calm day.")

# a parameter to add to file instead of writing over what was there. "a" as in append.
with open("myfile.txt", mode="a") as file:
    file.write("\nWe saw paintings exibition at the shops today.")

with open("doesnotexist.txt", mode="a") as file:
    file.write("\nWe saw paintings exibition at the shops today.")
