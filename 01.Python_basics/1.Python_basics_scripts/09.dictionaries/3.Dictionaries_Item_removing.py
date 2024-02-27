# Dictionary Items' removing

my_dict = {"color": "red", "fruit": "banana", "year": 1988,
           "age": 20}
# 1. pop() method removes an item from a dictionary using specified key:

my_dict.pop("color")
# print(my_dict)

# 2. popitems() removes the item at the end of the dictionary, before Python
# versions older than 3.6, the popitems() removes a random item from a
# dictionary:

my_dict1 = {"color": "red", "fruit": "banana", "year": 1988,
            "age": 20}
my_dict1.popitem()
# print(my_dict1)

# the del keyword remove an item with specified key:
my_dict2 = {"color": "red", "fruit": "banana", "year": 1988,
            "age": 20}
del my_dict2["fruit"]
# print(my_dict2)

# or it can be used to delete the dictionary
del my_dict2
# print(my_dict2)
