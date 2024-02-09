# Recursion or recursive functions
# Recursion is defined as the process of the function calling itself, that's
# means that the function is looping itself until a result is reached.
# There is an important note that should be taken in accont when using
# recursion, make sure the function is terminated by giving a result otherwise
# the function will not be terminated and keep looping infinetely, which leads
# to use an excess amount of memory and processor power.
def recursion(x):
    if x > 0:
        value = x + recursion(x - 1)
    else:
        value = 0
    return value


# print(recursion(3))


# recursion function can be written as follows:
def recursion1(x):
    if x <= 0:
        return 0
    return x + recursion1(x-1)


# print(recursion1(3))
