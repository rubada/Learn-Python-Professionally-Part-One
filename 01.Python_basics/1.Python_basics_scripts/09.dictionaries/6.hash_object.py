# Hash table & Hash method or function
# Hash tables are one type of data structure used to store and
# retrieve data efficiently.
# Data is stored in an array format in hashtables, each value has a unique
# index or hash_key, that's why values can be can be retrieved and inserted
# efficiently regardless of the data size.

# The implentation of hash tables in python are dictionaries. Dictionary use
# hash tables to store keys and values and provide fast access to values using
# the hash_key or index.
# Dictionary keys are hashable.
# Also the data that are stored in sets are hashable.
# And hashable values should be immutable objects.
# Mutable objetcts are not hashable.

# How to know that an object is hashable?
# Use the hash function, which is used to convert the data to and integer
# value, which is the index or hash_key used in a hash table.
# This is anouther way to check if a value is immutable or not.

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
# Memebership searching in sets and dictionaries is faster than lists,
# in a list the whole list will be searched to find the item.
# While in set and dictionary when new data is created or added, (keys in
# dicitianaies, items in set) the position of this item in memory is determind
# by the hash function, when testing for memebership python will look if the
# item is at the position determind by hash, that's why if the data is large
# lists will be much slower than sets and dicitionaries.
# And this is why keys in a dictionary and items in a set, should be mutable
# objects.


# Why mutable object can't be used?
# The reason because hash "value" of an object can never changed, and mutable
# objects can be changed and once they are changed the logical equality
# (==) will not be the same.
