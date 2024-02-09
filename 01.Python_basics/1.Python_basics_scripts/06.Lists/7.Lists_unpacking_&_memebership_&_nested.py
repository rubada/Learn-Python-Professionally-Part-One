# Using memebership operators with lists
my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]

# if "cat" in my_list:
#     print("True, cat is in my list")
# if "mouse" not in my_list:
#     print("False, mouse is not in my list")


# Lists unpacking
# There are two ways to assign objects in a list to variables.
# 1. Using Index
my_list1 = [1, 3, 9, 8, 4, 0, 2]
a = my_list1[0]
b = my_list1[1]
c = my_list1[2:6]
d = my_list1[6]

# print(a, b, c, d, sep="\n")

# A better way sequence unpacking
a1, b1, *c1, d1 = my_list1
# print(a1, b1, c1, d1, sep="\n")

# Nested Lists
new_list = [[2, 4, 6, [5, 7]],
            [55, 6, 8, 8],
            ["red", "green", "yelllow", "black", "blue"]
            ]

e = new_list[2][-1]
# print(e)

# Use the index() methods to get the index of an item inside the list
ind = new_list[2].index("black")
# print(ind)

ind1 = my_list.index("dog")
# print(ind1)
