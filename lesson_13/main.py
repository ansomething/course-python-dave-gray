person = "Dave"
coins = 3

print("Concatenação:")
print(person + " has " + str(coins) + " coins left.\n")

message = "%s has %s coins left.\n" % (person, coins)
print("%s:")
print(message)

message = "{} has {} coins left.\n".format(person, coins)
print(".format simples:")
print(message)

message = "{1} has {0} coins left.\n".format(coins, person)
print(".format com index:")
print(message)

message = "{person} has {coins} coins left.\n".format(person=person, coins=coins)
print(".format com key=value:")
print(message)

player = {"person": "Dave", "coins": 3}

message = "{person} has {coins} coins left.\n".format(**player)
print(".format com dictionary")
print(message)

# f-strings!

message = f"{person} has {coins} coins left.\n"
print("f-string:")
print(message)

print(f"{person} has {2 * 5} coins left.\n")

print(f"{person.lower()} has {2 * 5} coins left.\n")

print(f"{player['person']} has {2 * 5} coins left.\n")

num = 10
print(f"2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")