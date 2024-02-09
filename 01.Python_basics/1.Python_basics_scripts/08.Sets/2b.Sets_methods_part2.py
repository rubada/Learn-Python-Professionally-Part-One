# Sets methods
# Check below site for more information about all sets methods
# https://docs.python.org/3/library/stdtypes.html#set
# Or any site you prefer
# There is another type of sets, its called frozenset(), it is immutable type,
# we will not talk about it in this course, you can check the frozenset() by
# yourself, if you need to use it in your code.

a = {9, "cat", 9.7, "dog"}
b = {"mouse", 9.7, "banana", 9}

# 5. difference() return items that only exist in the set that is on the
# left side of difference() method, and remove items exist in both sets
# and the new set should be assigned to a new variable.
c = a.difference(b)
d = b.difference(a)
# print(c)
# print(d)

# 6. difference_update() method update the set on the left side of the
# difference_update() by returning the items that exist in this set and
# remove items exist in both sets.
# Can't be assigned to a variable.
# a.difference_update(b)
# print(a)
# b.difference_update(a)
# print(b)
