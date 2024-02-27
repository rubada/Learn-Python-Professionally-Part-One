# Lists
# A list is a built-in sequence, that is used to store a collection of data.
# In other programming they are sometimes called arrays.
# We can store any type of data in a list such as:
# Numbers, strings, Booleans, sets, dictionaries, tuples, and lists.
# Example:

my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]
# print(my_list)

# list type is a class object
# print(type(my_list))

# List rules:
# 1. Lists are ordered, when adding values to a list they will be added
# at the end of the list
# 2. Lists are mutable, objects inside a list, can be modified, and can be
# added or removed.
# 3. Lists can have duplicate objects.

# We can use the len() function to get the list length
# print(len(my_list))

# How can we define a new list?
# 1. Using the square brackets [] by assigning it to a variable, creating an
# empty list and then it can be filled with any type of data.

a = []

# 2. Using the list() constructor or function to define a new list.
b = list()

# we can use the list() to change a different data type to list
my_tuple = (1, 3, 5, 8)
# print(list(my_tuple))

# range() can be used to create a list
# Range syntax: range(start, stop-1, step)
c = range(10)

# print(c)
# by using list()
# print(list(c))

# or using [*]
print([*c])

# Using [*] will be more efficient than using list() fucntion.
