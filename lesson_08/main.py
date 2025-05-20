value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
# skips the next commands and go back to the beginning of the loop
#     print(value)
# else:
#     print("Value is now equals to " + str(value))

# for x in names:
#     print(x)

# for x in "Mississipi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)

# for x in range(0, 101, 5):
#     print(x)
# else:
#     print("Glad that's over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")