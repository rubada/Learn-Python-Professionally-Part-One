my_set = {2, "Hello", (3, 7, 88)}

# 1st question
# create a copy of the above set, we use the copy() method to create
# a copy of a set, don't use the equal sign
new_set = my_set.copy()
# or using the set function
# new_set = set(my_set)

# 2nd question
# Access the tuple inside new_set
# There are many ways to access the tuple in a set, but they will be
# clear in the future, but the simplest is to use the built-in function
# isinstance to check if an item is tuple or any other type of data.
for i in new_set:
    if isinstance(i, tuple):
        output = i
# print(output)


# 3rd question
# add items in a set
# add cat and add [6, 9, "dog"] to new_set1
# and add below list to new_set1
my_list = ["mouse", "cat"]
new_set1 = {2, "Hello", False, (3, 7, 88)}

new_set1.add("dog")
new_set1.update([6, 9, "dog"])
new_set1.update(my_list)
# print(new_set1)


# 4th question
# Given the following sets:
a = {3, 4, 88, 9, 8, 200, 50}
b = {3, 4, 88, 9}

# Check if b is a subset of a:
# issubset Check if all items in a set are contained in other set.
print(b.issubset(a))

# Check if the two sets has intersection or not
# isdisjoint return True if there is no common items in both sets
# and False otherwise
print(a.isdisjoint(b))

# Check if a has all the items in b
# issuperset return True if the set contains the orher set
print(a.issuperset(b))
