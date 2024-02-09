# Tuples
# A tuple is a built-in sequence, that is used to store a collection of data.
# We can store any type of data in a tuple such as:
# Numbers, strings, booleans, sets, dictionaries, tuples and lists.
# Example:
my_tuple = (9, "cat", 9.7, "dog", [False, True, None], 9, (1, 2))
# print(my_tuple)

# tuple type is a class object
# print(type(my_tuple))

# Tuple rules:
# 1. Tuples are ordered, each item has a position that will not change.
# 2. Tuples are immutable, tuples can't be changed or modified. Items can't be
# added or removed once the tuple is created.
# 3. Tuples can have duplicates objects.

# We can use the len() function to get the tuple length
# print(len(my_tuple))

# How can we define a new tuples?
# 1. Using the round brackets () by assign it to a variable and then
# can be filled with one itme
a = ("a")
# print(a)
# print(type(a))  # Why?


# To create a tuple of one item, comma must be added after this item
b = (9,)
# print(b)
# print(type(b))

# 2. Using the tuple() contructure or function to define a new tuple.
b = tuple((4, 6, 7))
# print(b)

# we can use the tuple() to change a different data type to tuple
my_list = [1, 3, 5, 8]
# print(tuple(my_list))

# Using range() to create a tuple, because tuples are iterables
c = range(0, 10)

# by using tuple()
print(tuple(c))
