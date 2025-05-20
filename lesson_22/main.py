import os

# r = read
# a = append
# w = write
# x - create

# Read - error if it doesn't exist

file = open("names.txt")  # "r" is the default
# print(file.read())
# print(file.read(4))

# print(file.readline())
# print(file.readline())

for line in file:
    print(line)

file.close()

try:
    file = open("names.txt")
    print(file.read())
except:
    print("The file you want to read doesn't exist.")
finally:
    file.close()

# Append - creates the file if it doesn't exist

file = open("names.txt", "a")
file.write("Neil\n")
file.close()
print("")
file = open("names.txt")
print(file.read())
file.close()

# Write (overwrite)

file = open("context.txt", "w")
file.write("I deleted all of the context.")
file.close()
print("")
file = open("context.txt")
print(file.read())
file.close()

# Two ways to create a new file

# Opens a file for writing and creates it if it doesn't exist
file = open("name_list.txt", "w")
file.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    file = open("dave.txt", "x")
    file.close()

# Delete a file

# Avoid an error if it doesn't exist
if os.path.exists("name_list.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist.")


with open("more_names.txt") as file:
    content = file.read()

with open("names.txt", "w") as file:
    file.write(content)

with open("names.txt") as file:
    print(file.read())
