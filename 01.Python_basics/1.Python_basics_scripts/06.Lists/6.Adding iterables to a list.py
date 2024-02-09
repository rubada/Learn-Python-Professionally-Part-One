# How to add iterables to a list?
# Lists concatentating by using + sign, will join two lists together.

my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]
list_num = [10, "red", False]

my_list = list_num + my_list + list_num
# print(my_list)

my_tuple = (2, 4, 6)
# my_list = my_list + my_tuple
# print(my_list)

# Using extend() method will extend the same list by adding the items from
# the new list.
# extend method used to add iterable at the end of a list, such as:
# lists, sets, tuples and dictionary keys.

# my_list.extend(list_num)
# print(my_list)

# my_list.extend(my_tuple)
# print(my_list)
