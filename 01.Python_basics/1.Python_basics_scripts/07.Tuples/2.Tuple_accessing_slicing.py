# How to access tuple items?
# Of course by using indexing, the same indexing rules used
# in strings and lists applied on tuples

# Examples
my_tuple = (9, "cat", 9.7, "dog", [False, True, None], 9, (4, 1, "orange"))

# print(my_tuple[6])
# print(my_tuple[-3])

# To access the sub-list or sub-tuple inside the main tuple, we use
# double indexing:
# print(my_tuple[6][0])
# print(my_tuple[6][1])
# print(my_tuple[6][2])

# Tuples are iterables, we can use loops with them
# for i in range(len(my_tuple)):
#     print(my_tuple[i])

# for i in my_tuple:
#     print(i)

# we can loop over the sub-tuple
# for i in range(len(my_tuple[6])):
#     print(my_tuple[6][i])

# for i in my_tuple[6]:
#     print(i)

my_tuple = (9, "cat", 9.7, "dog", [False, True, None], 9, (4, 1, "orange"))

# Tuples Slicing
# The same strings and lists slicing rules are applied on tuples
# a. a[start:stop]
# Indexing will begin from "start" through "stop-1".

# print(my_tuple[3:6])
# print(my_tuple[-4:-1])

# b. a[start:]
# Indexing will begin from "start" to the end of the tuple.

# print(my_tuple[4:])
# print(my_tuple[-3:])

# c. a[:stop]
# Indexing starts from the beginning through "stop-1".

# print(my_tuple[:4])
# print(my_tuple[:-3])

# d. a[:]
# Create a copy of the tuple.

# print(my_tuple[:])
# print(my_tuple[::])

my_tuple = (9, "cat", 9.7, "dog", [False, True, None], 9, (4, 1, "orange"))

# e. a[start:stop:step]
# Indexing will begin from "start" through "stop-1", taking in account
# the step.

# print(my_tuple[1:6:2])
# print(my_tuple[-6:-1:2])

# f. reverse order
# f. reverse order
# a[start:stop:-step]
# "start" index > "stop" index, begin from "start" through "stop+1" in
# descending order.
# As shown above step is a negative number, indicating that the list output
# will be reversed.

# print(my_tuple[::-1])
# print(my_tuple[5:3:-2])
# print(my_tuple[-2:-6:-2])
# print(my_tuple[3::-1])
