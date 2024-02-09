# Dictionaries
# A dictinary is built-in mapping type, used to store a collection of
# data, such as numbers, strings, lists, tuples, sets and dictionaries.
# Example:
my_dict = {1: 2, (1, 2): "red", "list": [1, 32, 76], "tuple": (5, 7),
           "set": {5, "yellow"}, "dict": {"a": "banana", "b": 8},
           4: 2}

# Dictionaries used keys to access the values inside the dictionary.
# For example "list" is the key, [1, 32, 76] is the value.
# In the next video we will discuss accessing a dictionary in details
# Accessing a dictionary will be done as follows:
a = my_dict[1]
b = my_dict["tuple"]

# 1 and "tuple" are dictionary keys.
# The output of a and b is the dictionary values
# print(a)
# print(b)

# Dictionaries rules:
# 1. Dictionaries are ordered, ordered dictionaries started in version 3.6+,
# versions older than 3.6- dictionaries were not ordered.
# 2. Dictionaries are mutable, items can be changed, added and removed from
# a dictionary
# 3. Dictionaries don't allow keys' duplicate, having two items with the same
# key.
# my_dict2 = {1: 2, 2: "red", 4: 2, 2: 4}
# print(my_dict2)

# 4. When defining a key, the key should be an immutable object,
# and it is preferred to use strings
my_dict2 = {False: 2, 2: "red", "4": 2, (2, 4): 4}
# print(my_dict2)
