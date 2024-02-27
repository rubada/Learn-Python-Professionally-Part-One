# Functions in python are considered first-class objects.
# Functions in Python are objects, like lists, dictionaries, strings, etc.,
# which means that functions can be used in different ways like any other
# objects in Python, that's why they are called first-class objects.
# Let's see how can we use these first-class objects:

# 1. Functions and functions objects can be assigned to variables.
def even_odd_number(x):
    if x % 2 == 0:
        return f"Number {x} is even"
    else:
        return f"Number {x} is odd"


# As shown before you can assign the function to variable:
a = even_odd_number(4)
# print(a)

# or assign the function object to variable then call or invoke the variable:
b = even_odd_number
# print(b(5))


# 2. Functions can be passed as arguments to another function:
def even_number(x):
    if x % 2 == 0:
        return f"Number {x} is even"


def odd_number(x):
    if x % 2 != 0:
        return f"Number {x} is odd"


def odd_or_even(func1, func2, x):
    if func1(x):
        num = func1(x)
    else:
        num = func2(x)
    return num


# print(odd_or_even(even_number, odd_number, 10))


# 3. A function can be called from another function or returned inside another
# function.
# Calling function from other function:

def add(a, b):
    return a + b


def multiply(x, y, z):
    result = add(x, y) * z
    return result


# print(multiply(3, 2, 5))


# Returning function inside another function:
def devision(z):
    def add(x, y):
        return (x + y) / z
    return add


div_num = devision(10)
adding = div_num(5, 5)
# print(adding)

# The above function is a nested function and it will be discussed later in
# details (part 9 nested function and part 10 Python closure).

# 4. A function can be stored in data structures such as dictionaries, lists,
# sets, tuple etc.

my_list = [odd_or_even, multiply, even_odd_number]

# print(my_list[0](odd_number, even_number, 3))
# print(my_list[1](4, 5, 6))

# First class objects are a part of functional programming.
