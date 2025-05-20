name = "Dave"  # global scope


# greeting("John")


def another():
    color = "blue"  # local scope
    global name
    name += " Gray"

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting(name)


another()
