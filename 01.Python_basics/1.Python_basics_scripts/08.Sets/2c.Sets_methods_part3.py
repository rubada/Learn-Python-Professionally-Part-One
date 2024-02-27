# Sets methods
# Check the below site for more information about all sets’ methods
# https://docs.python.org/3/library/stdtypes.html#set
# Or any site you prefer
# There is another type of set, it's called frozenset(), which is immutable
# type, we will not talk about it in this course, you can check the frozenset()
# by yourself, if you need to use it in your code.

a = {9, "cat", 9.7, "dog"}
b = {"mouse", 9.7, "banana", 9}

# 7. intersection() returns a new set that contains items that exist in both
# sets, it can be assigned to a variable.
c = a.intersection(b)
d = b.intersection(a)
# print(c)
# print(d)

# 8. intersection_update() update the set on the left side of
# intersection_update() with items that exist in both sets, it can be assigned
# to a variable.
# a.intersection_update(b)
# print(a)

# b.intersection_update(a)
# print(b)
