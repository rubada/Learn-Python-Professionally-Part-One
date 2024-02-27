# Dictionaries

my_dict = {1: 2, (1, 2): "red", "list": [1, 32, 76], "tuple": (5, 7),
           "set": {5, "yellow"}, "dict": {"a": "banana", "b": 8},
           4: 2}

# dictionaries type is class dict
# print(type(my_dict))

# Use the len() to get the number of items inside the dictionary.
# print(len(my_dict))

# How to define a dictionary?
# 1. Using the curled brackets {}, and fill them with keys and values.

# Example:
new_dict = {}
new_dict["key1"] = ["value1", "value2"]
new_dict["key2"] = "value2"
# print(new_dict)

# 2. Using the dict() constructor or function.
dict_two = dict(key1="value1", num2="value2")
# print(dict_two)

# Iterables such as lists, sets, and tuples can be used to create a dictionary,
# by using sub-lists, sub-tuples, or sub-sets.
# Python will consider the first item in the sub-list or (sub-tuple, sub-set)
# as the key and the second item as the value when creating the dictionary.
my_list = [["fruit", ["banana", "apple"]], {"color", "blue"}, ("number", 4)]

dict_three = dict(my_list, animal="cat")
# print(dict_three)
