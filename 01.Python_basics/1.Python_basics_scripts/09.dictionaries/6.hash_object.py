# Hash table & Hash method or function
# Hash tables are one type of data structure used to store and retrieve
# data efficiently.
# Data is stored in an array format in a hashtables, each value has a unique
# index or hash_key, that's why values can be retrieved and inserted
# efficiently regardless of the data size.

# The implementation of hash tables in Python are dictionaries. The dictionary
# uses hash tables to store keys and values and provide fast access to values
# using the hash_key or index.
# Dictionary keys are hashable.
# Also the data that are stored in sets are hashable.
# And hashable values should be immutable objects.
# Mutable objects are not hashable.


# How to know that an object is hashable?
# Use the hash function, which is used to convert the data to an integer
# value, which is the index or hash_key used in a hash table.
# This is another way to check whether an object is immutable.

my_dict = {1: 2, (1, 2): "red", "list": [1, 32, 76], "tuple": (5, 7),
           "set": {5, "yellow"}, "dict": {"a": "banana", "b": 8},
           4: 2}
my_list = [2, 6, "red"]
my_set = {"cat", 9.7, "dog", 9, (False, True)}
My_tuple = (1, 3, 4, 4)

# print(hash((my_dict)))
# print(hash(my_list))
# print(hash((my_set)))
print(hash((My_tuple)))

a = 8
b = 900
# print(hash(a))
# print(hash(b))

str1 = "red"
str2 = "red"
# print(hash(str1))
# print(hash(str2))
# print(hash(True))


# Why using hashtables is more efficient?
# Let's take an example:
# Membership searching in a set and dictionary is faster than a list,
# in a list the whole list will be searched to find an item.
# While in a set or a dictionary when new data is created or added, (keys in
# a dictionary, items in a set) the position of this item in memory is
# determined by the hash function, when testing for membership Python will
# look if the item is at the position determined by the hash function, that's
# why if the data is large lists will be much slower than sets and
# dictionaries.
# And this is why keys in a dictionary and items in a set, should be immutable
# objects, because their values can't be changed.


# Why mutable objects can't be used or are not hashable?
# The reason because the hash "value" of an object can never be changed, and
# mutable objects can be changed, and once they are changed the logical
# equality (==) will not be the same.
