# Lists methods
# Check below site for more information about all lists methods
# https://docs.python.org/3/tutorial/datastructures.html
# Or any site you prefer

# 4. sort() method and sorted() function
# To sort a list the item in the list should be of the same type.

new_list = [20, 3, 5, 7, 9, 4, 50, 6]

# The sort() is used to sort the same list, so it can't be
# assigned to a variable
# new_list.sort()
# print(new_list)

# To assign a sorted list to a new variable the sorted() is used.
sorted_list = sorted(new_list)
print(sorted_list)

# To sort the list in reverse mode
new_list.sort(reverse=True)
# print(new_list)

sorted_list = sorted(new_list, reverse=True)
# print(sorted_list)

# 5. copy(), list1 = list2, list = [:]
# To copy a list it is better to use the copy method,
# because it will assign it to a new object.
# Let take an example


new_list = [20, 3, 5, 7, 9, 4, 50, 6]

# Copying the list as shown below, will result that both list
# have the same memory address same object, in this case modifying
# one list will modify the other.
copied_list = new_list
# copied_list.append(100)
# print(copied_list)
# print(new_list)

# Using list[:] will copy the list to different object
copied_list1 = new_list[:]
copied_list1.append(100)
# print(copied_list1)
# print(new_list)

# Finally using the copy()
copied_list2 = new_list.copy()
copied_list2.append(300)
# print(copied_list2)
# print(new_list)

# Note that when modifying a list using the lists methods, indexing,
# slicing, it is done on the same object, with the same memory address.
# Unless assigned to a new variable.
