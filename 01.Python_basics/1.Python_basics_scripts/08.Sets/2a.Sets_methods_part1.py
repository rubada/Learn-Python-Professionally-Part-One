# Sets methods
# Check below site for more information about all sets methods
# https://docs.python.org/3/library/stdtypes.html#set
# Or any site you prefer
# There is another type of sets, its called frozenset(), it is immutable type,
# we will not talk about it in this course, you can check the frozenset() by
# yourself, if you need to use it in your code.

my_set = {9, "cat", 9.7, "dog"}

# 1. add() method used to add items or objects any location inside the set.
# my_set.add("yellow")
# my_set.add(4)
# print(my_set)

# 2. update() method add another set or other iterable at any location inside
# the set
new_list = [4, 5, 7]
# my_set.update(new_list)
# print(my_set)

# 3. remove(), pop(), discard() remove items from a set

# remove() method removes item from a set and raise an error if the item
# doesn't exist inside the set.
my_set = {9, "cat", 9.7, "dog"}
# my_set.remove("cat")
# my_set.remove("mouse")
# print(my_set)

# pop() mehtod removes a random item from a set.
# my_set.pop()
# print(my_set)

# discard() method removes item from a set and doesn't raise and error if item
# doesn't exist
# my_set.discard("cat")
# my_set.discard("mouse")
# print(my_set)

# 4. union() will combine more than one set or more than one iterable into one
# set and create a new set or new object, even if the same variable name is
# used.
my_set = {9, "cat", 9.7, "dog"}
set1 = {3, "red", "banana"}
list1 = [66, "apple", "bird"]
new_set = my_set.union(set1, list1)
# print(new_set)
# print(id(my_set))

my_set = my_set.union(set1, list1)
# print(my_set)
# print(id(my_set))

# If the an object is needed to be updated, Use the update() method, don't
# use the union() method.
