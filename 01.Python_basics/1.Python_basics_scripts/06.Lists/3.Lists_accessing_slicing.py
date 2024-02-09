# How to access list items?
# Of course by using indexing, the same indexing rules used
# in strings are applied on lists

# Examples
my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]

# print(my_list[0])
# print(my_list[5])
# print(my_list[4])
# print(my_list[-1])
# print(my_list[-4])

# To access the sub list inside the main list, double indexing is used:
# print(my_list[4][0])
# print(my_list[4][1])
# print(my_list[4][2])

# Lists are iterables, loops can be used to iterate on lists objects.
# for i in range(len(my_list)):
#     print(my_list[i])

# for item in my_list:
#     print(item)

# Loop over the sub list, as shown below:
# for i in range(len(my_list[4])):
#     print(my_list[4][i])

# for item in my_list[4]:
#     print(item)

my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]

# Lists Slicing
# The same string rules are applied on lists
# a. a[start:stop]
# Indexing will begin from "start" through "stop-1".

# print(my_list[3:5])
# print(my_list[-4:-1])

# b. a[start:]
# Indexing will begin from "start" to the end of the list.

# print(my_list[3:])
# print(my_list[-5:])

# c. a[:stop]
# Indexing starts from the beginning through "stop-1".

# print(my_list[:4])
# print(my_list[:-2])

# d. a[:]
# Create a copy of the list.

# print(my_list[:])
# print(my_list[::])

my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]

# e. a[start:stop:step]
# Indexing will begin from "start" through "stop-1", taking in account
# the step.

# print(my_list[1:6:2])
# print(my_list[-6:-1:2])

# f. reverse order
# a[start:stop:-step]
# "start" index > "stop" index, begin from "start" through "stop+1" in
# descending order.
# As shown above step is a negative number, indicating that the list output
# will be reversed.

# print(my_list[::-1])
# print(my_list[5:3:-1])
# print(my_list[5:3:-2])
# print(my_list[-2:-6:-2])
# print(my_list[3::-1])
# print(my_list[:3:-1])
