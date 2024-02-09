# Change Items in Tuples
# As mentioned before tuples are immutable, once they are created,
# then they can't be changed, then how tuples can be changed?
# 1. Change the tuple to list,
# 2. Do the changes, by applying lists methods or using indexing
# and slicing.
# 3. Then change the list back to a tuple
# Example

my_tuple = (9, "cat", 9.7, "dog", [False, True, None], 9, (4, 1, "orange"))
my_list = list(my_tuple)
my_list[5] = "green"
my_list.append("carrot")
my_tuple = tuple(my_list)
# print(my_tuple)

# Tuples can be added to other tuples by using +, concatenating
new_tuple = ("red", "blue", "yellow")
add_tuple = ("black",)
new_tuple += add_tuple  # a = a + 1 same as a+=1
print(new_tuple)

# Note that when changing a tuple using the above methods,
# we create a new objects, because tuples are immutable.
# Each object has different memory address.
