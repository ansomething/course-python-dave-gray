# recursão
def add_one(num):
    if num >= 5:
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)


# while loop
def add_num(num):
    while num <= 9:
        num += 1
        print(num)


print("")
add_num(0)
