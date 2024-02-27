# Tuples methods
# Tuples has only two methods, count() and index()

my_tuple = ("cat", 9.7, 9, "dog", [False, True, None], 9, (1, 2))

# 1. count(), returns the number of the items in a tuple.
a = my_tuple.count(9)
# print(a)

b = my_tuple.count("cat")
# print(b)

# 2. index(), returns the index number of an item in a tuple.
c = my_tuple.index([False, True, None])
# print(c)

# If there are duplicate items, then the index of the first duplicates
# is returned.
d = my_tuple.index(9)
# print(d)
