# Functions
# Arguments Types:
# 1. Default arguments
# 2. Keyword arguments (named arguments)
# 3. Positional arguments
# 4. Arbitrary arguments (*args and **kwargs)

# 1. Default arguments: are parameters with assigned values when the function
# is defined.
# Such parameters are optional.
def add_fun(a, b=10):
    return a + b


x = 23
# print(add_fun(x, 2))


# 2. Keyword arguments (named arguments): are arguments that use the parameters
# names when calling the function and assigning it to the required values, in
# this case the order of the arguments when calling the function doesn't
# matter.

def multiply_three_lists(a, b, c):
    list_multiplied = []
    for i in range(len(a)):
        num_multiplied = a[i] * b[i] * c[i]
        list_multiplied.append(num_multiplied)
    return list_multiplied


x = [1, 2, 3]
y = [2, 4, 7]
z = [5, 6, 8]

# print(multiply_three_lists(b=y, c=z, a=x))

# Note: Different data types can be set as function arguments such as numbers,
# strings, lists, tuples, sets, and dictionaries, etc., even a function can be
# passed as an argument.


# 3. Positional arguments: are arguments where the order of the arguments
# should be the same as the parameters defined in the function, if the Keyword
# arguments are not used.

def name_age(name, age):
    data = f"My name is {name} and my age is {age}"
    return data


name = "Mohammad Al-Ahmad"
age = 35

# print(name_age(name, age))

# changing the position
# print(name_age(age, name))
