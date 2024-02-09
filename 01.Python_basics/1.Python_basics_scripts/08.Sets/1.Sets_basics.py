# Sets
# A set is a data type used to store a collection of data.
# Sets are used to store numbers, strings and booleans and tuples.
# Sets rules
# 1. Unordered
# Items in a set doesn't have an order, that's why sets are unindexed
# example:
my_set = {"cat", 9.7, "dog", 9, (False, True)}
# print(my_set)

# 2. Items are unchangeable
# Once the set is created, items in it can't be changed, because they are
# unindexed, sets item can't be changed, but items can be added or removed.
# example:
# my_set[1] = 7
# print(my_set)

# 3. Duplicates are not allowed
# example:
my_set = {9, "cat", 9.7, "dog", 9, False, True}
# print(my_set)

# use len() function
# print(len(my_set))      # The length without the duplicate

# Sets type
# print(type(my_set))

# How can we define a new set?
# 1. Use curled brackets {}
new_set = {3}
# print(new_set)

# Use set() contructure or function to define a new set.
a = range(0, 10)
b = set(a)
# print(b)

# or change a list or tuples to a set
c = [3, 4, 5]
d = (5, 7, 9)
# print(set(c), set(d), sep="\n")

# How to access a set?
# To access a set by looping through the set, because the set
# doesn't have indexing.
# When accessing the set through looping, the output will be
# unordered
my_set = {9, "cat", 9.7, "dog", 9, (False, True)}
# for item in my_set:
#     print(item)
