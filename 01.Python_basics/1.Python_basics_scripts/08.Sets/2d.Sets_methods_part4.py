# Sets methods
# Check the below site for more information about all sets’ methods
# https://docs.python.org/3/library/stdtypes.html#set
# Or any site you prefer
# There is another type of set, it's called frozenset(), which is immutable
# type, we will not talk about it in this course, you can check the frozenset()
# by yourself, if you need to use it in your code.

a = {9, "cat", 9.7, "dog"}
b = {"mouse", 9.7, "banana", 9}

# 7. symmetric_difference() returns a new set that contains items that don't
# exist in both sets, it can be assigned to a variable.
c = a.symmetric_difference(b)
d = b.symmetric_difference(a)
# print(c)
# print(d)

# 8. symmetric_difference_update update the set on the left side of
# symmetric_difference_update() with items that don't exist in both sets, it
# can be assigned to a variable.
# a.symmetric_difference_update(b)
# print(a)

# b.symmetric_difference_update(a)
# print(b)
