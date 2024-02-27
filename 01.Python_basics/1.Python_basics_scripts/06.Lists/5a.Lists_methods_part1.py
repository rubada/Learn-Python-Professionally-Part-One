# Lists methods
# Check the below site for more information about all list methods
# https://docs.python.org/3/tutorial/datastructures.html
# Or any site you prefer

my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]

# 1. append(), is used to add an item at the end of the list
my_list.append("mouse")
# print(my_list)

# An important note, append() can't be assigned to a variables,
# it will return None, why?
# Because append() is used to modify a list, which means there
# is nothing to return
add = my_list.append(7)
# print(add)

# List is modified even if it is assigned to a variable.
# Thus, no need to assign append() to a variable.
# print(my_list)


# 2. insert(), add an item to a specific location in a list
my_list1 = [9, "cat", 9.7, "dog", [False, True, None], 9]
my_list1.insert(3, "red")
# print(my_list1)


# 3. pop() removes an item with a specific index from a list,
# if no index is specified, it will remove the last item.

my_list2 = [9, "cat", 9.7, "dog", [False, True, None], 9]

# my_list2.pop(2)
# print(my_list2)
# my_list2.pop()
# print(my_list2)

# pop() can be assigned to a variable and return the item
# that is removed
my_list3 = [9, "cat", 9.7, "dog", [False, True, None], 9]
pop_item = my_list3.pop()
print(pop_item)
