# Higher-order built-in functions
# As mentioned before these functions can accept a function or functions as
# their arguments and/or return a function or functions as an output.
# filter()
# It applies a function on an iterable and returns the value of the items in
# the iterable that satisfies the condition/s in the function.
# Syntax
# filter(func, iterable)

# Example
def check_vowels(letter):
    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        return True
    else:
        return False


misc_letters = ["a", "u", "y", "b", "f", "A", "e", "E"]
vowels_letters = list(filter(check_vowels, misc_letters))
# print(vowels_letters)


# Another example
# Even and odd numbers
numbers = [44, 66, 79, 63, 13, 79, 90, 55, 24]

even_num = list(filter(lambda num: num % 2 == 0, numbers))
# print(even_num)

# The above lambda function returns True or False, then the filter() will
# will take the items in the sequence that satisfy the condition in the
# function same for the above example.

odd_num = list(filter(lambda num: num % 2 != 0, numbers))
# print(odd_num)


# Using filter without function:

misc_list = [False, True, "Banana", 0, 34, "Red", 5, [], [2, 5]]

filter_list = list(filter(None, misc_list))
# print(filter_list)


# Using filter() with a list of dictionaries:
personal_data = [
    {'name': 'John', 'age': 22, 'country': 'USA'},
    {'name': 'Mary', 'age': 30, 'country': 'UK'},
    {'name': 'Luca', 'age': 15, 'country': 'Italy'},
    {'name': 'Mohammad', 'age': 34, 'country': 'Eygpt'},
    {'name': 'Leen', 'age': 25, 'country': 'Jordan'},
    ]

data_new = filter(lambda dict: dict["age"] > 24, personal_data)

# "for" loops can be used with filter() to get filtered data.
# Applying for loop on iterable object will make the code faster than get
# the list or iterable of the filter() then apply the for loop, in this case
# one step is removed.

# for dict in data_new:
#     print(dict['name'], dict["country"])

# or
# print(list(data_new))
