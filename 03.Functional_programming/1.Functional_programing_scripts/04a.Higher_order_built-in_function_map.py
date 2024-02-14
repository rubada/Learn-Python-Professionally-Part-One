# Higher-order built-in functions
# As mentioned before these function can accept function as their arguments and
# or return function as an output.
# map() function
# is used to apply a function on each item in an iterable, lists, dictionaies
# sets etc.
# Syntax
# map(function, iterables)
# Example
num = [2, 6, 7, 9, 3]
num_double_map = map(lambda x: x*2, num)
num_double_list = list(num_double_map)
# print(num_double_map)
# print(num_double_list)

# The above example can be also done by using for loop and list comprehensions,
# but using map function is faster than list comprehension and the for loop,
# and the expression is clean and readable.


def add(a, b):
    return a + b


num = [2, 6, 7, 9, 3]
num1 = [3, 4, 6, 99, 7]

add_two_lists = list(map(add, num, num1))
# print(add_two_lists)

# Get the letters in a list of strings, using built-in functions
fruits = ["cherry", "banana", "apple", "orange"]
letters_list = list(map(list, fruits))

# print(letters_list)

# Using other built-in method
upper_case = list(map(str.capitalize, fruits))
# print(upper_case)

# Using map() Function with dictionaries
my_dict = {"color": "red", "fruit": "banana", "year": "nineteen eighty nine",
           "age": "twenty"}

my_dict_capitalize = dict(map(lambda x: (x[0].capitalize(), x[1].capitalize()),
                              my_dict.items()))

# print(my_dict_capitalize)
# print(my_dict.items())

# Use map to round numbers to a certain digit using range
digits = [1.356, 4.55556, 7.9876543, 9.5939365963]

round_digits = list(map(round, digits, range(1, 5)))
# print(round_digits)

# or
list_ones = [1] * len(digits)
round_digits_one = list(map(round, digits, list_ones))
# print(list_ones)
# print(round_digits_one)
