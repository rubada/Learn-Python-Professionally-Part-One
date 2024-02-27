# 1st Question:
# Change the item 3 in the list, inside the tuple, from 45 to 785:
# my_tuple = (44, 55, [66, 96, 45, 60], 89, 32)
# The output should be:
# (44, 55, [66, 96, 785, 60], 89, 32)
my_tuple = (44, 55, [66, 96, 45, 60], 89, 32)

my_list = list(my_tuple)
my_list[2][2] = 785

my_tuple = tuple(my_list)
# print(my_tuple)

# 2nd Question:
# Unpack the following Tuple
# my_tuple = (65, 78, 84, ["red", "yellow", "green"])
# output should be:
# 65
# 78
# 84
# red
# green
# yellow

my_tuple = (65, 78, 84, ["red", "yellow", "green"])
*a, b = my_tuple
c, d, e = b
# print(a, c, d, e, sep="\n")

# 3rd Question:
# Add new_tuple = (2, 4, 8) to my_tuple
# Add new_list = [3, 8, "red"] to my_tuple
# what is the output?

new_tuple = (2, 4, 8)
my_tuple = my_tuple + new_tuple
print(my_tuple)

new_list = [3, 8, "red"]
# my_tuple = my_tuple + new_list
# print(my_tuple)             # return an error

my_list = my_list + my_tuple
print(my_list)                # return an error
