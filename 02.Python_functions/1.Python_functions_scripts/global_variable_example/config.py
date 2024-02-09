x = 10
y = 40


def check_x(name):
    global x, y
    if name:
        x = x - 6
        y = y + 1

    else:
        x = x + 3
        y = y - 4

    return x, y
