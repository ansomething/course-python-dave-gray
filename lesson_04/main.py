# string data type

# literal assignment
first = "Andressa"
last = "Vieira"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("Pepperoni")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(2000)
print(type(decade))

statement = "I like rock music from the " + decade + "s."
print(statement)

# multiple line
multiline = """
Hey, how are you?

I was just checking in.   
                                All good?   

"""
print(multiline)

# escaping special characters
sentence = "I'm alright.\tHey!\n\nWhere's this at\\located?"
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                "
print(len(multiline))
multiline = "                  " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("")

# string index value
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("A"))
print(first.endswith("Z"))

# boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print("")

# numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print("")

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))
print("")

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))
print()

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data
zip_value = int("New York")
print(type(zip_value))
