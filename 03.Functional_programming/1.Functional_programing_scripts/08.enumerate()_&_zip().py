# Zip() is used to iterate over two or more iterables to produce an iterable
# with subtuples inside.
# Syntax
# zip(*iterables, strict=False)

colors = ["red", "green", "orange"]
fruits = ["cherry", "kiwi", "orange"]
vegetables = ["tomato", "lettuce", "pumpkin"]

veg_fru = list(zip(colors, fruits, vegetables))
# print(veg_fru)

# Using asterisk instead of using list().
# Using zip() again to unzip and return the iterators to their origin data
# structure.
zipped = [*zip(colors, fruits, vegetables)]
unzipped = zip(zipped)
# Unpack the iterable object
x, y, z = unzipped
# print(x[0], y, z, sep="\n")

new_list = list(zip(('a', 'b', 'c'), range(0, 3)))
# print(new_list)


# using strict = True will raise a ValueError, if strict is False no error
# will be raised.
# new = list(zip(('a', 'b', 'c'), (1, 4), strict=True))
# print(new)

list_of_lists = [['a', 0], ['b', 1], ['c', 2]]

# Use the zip() to seperate the lists in list_of_lists:
a, b, c = zip(list_of_lists)
# print(a[0], b, c, sep="\n")

# enumerate() takes an iterable and adds a counter on each item inside it
# Syntax
# enumerate(iterable, start)
vegetables = ["tomato", "lettuce", "pumpkin"]
# count_veg = list(enumerate(vegetables))
count_veg = [*enumerate(vegetables)]
# print(count_veg)

color_veg_fru = {
    'red': ['cherry', 'tomato'],
    'green': ['kiwi', 'lettuce'],
    'orange': ['orange', 'pumpkin']
    }

# Take the dictionary keys, and create a new dictionary with a counter
# numbers as keys:
enum_dict = dict(enumerate(color_veg_fru))
# print(enum_dict)

# Take the dictionary keys and values, and create a new dictionary with a
# counter numbers as keys, and the start parameter is equal to 1:
enum_dict_items = dict(enumerate(color_veg_fru.items(), start=1))
# print(enum_dict_items)

# enumerate can be used with "for" loop:
# for num, key_value in enumerate(color_veg_fru.items()):
#     print(f"{num} = {key_value}")

# or
# for i, (key, value) in enumerate(color_veg_fru.items()):
#     print(f"{i} - {key} = {value}")

# Using zip() and enumerate() together:
colors = ["red", "green", "orange"]
fruits = ["cherry", "kiwi", "orange"]
vegetables = ["tomato", "lettuce", "pumpkin"]

# for i, (color, fruit, veg) in enumerate(zip(colors, fruits, vegetables),
#                                         start=1):
#     print(f"{i} - {color} is for {fruit} and {veg}")

# or

# for i, item in enumerate(zip(colors, fruits, vegetables), start=1):
#     print(f"{i} - {item[0]} is for {item[1]} and {item[2]}")
