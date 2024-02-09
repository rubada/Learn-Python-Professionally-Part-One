# Dictionay Accessing, changing and modifying:
# Dictinary methods will be cover in this video and the upcomming videos
# To check all the methods, check the following site:
# https://docs.python.org/3/library/stdtypes.html#dict
# or any other site you prefer
# Using the dictionary keys, as mentioned in the previous video to access
# or change the value.
my_dict = {"color": "red", "fruit": "banana", "year": 1988,
           "age": 20}

value1 = my_dict["color"]
# print(value1)

# Using get() method, give the same result
value2 = my_dict.get("fruit")
# print(value2)

# Keys can be accessed using the keys() method, and return a list of keys
# as viewied object.
keys_dict = my_dict.keys()
my_list = list(keys_dict)
# print(keys_dict)
# print(my_list)

# Adding new item to dictionary
my_dict["animal"] = "cat"

# or changing the key value
my_dict["year"] = 2004

# Note viewed object means any change in the dictionary, will modify the keys
# list that is returned when keys() method is used.
# print(my_dict)
# print(keys_dict)

# Note that when the dictionary is changed the list that is created by list()
# will not be modified or changed.
# print(my_list)

# Redefine the list again using the list() to get the modified values.
my_list = list(keys_dict)
# print(my_list)

# Using memebership operators to check if a key in a dictionary
# if "fruit" in my_dict:
#     print(True)
# if "Hello" not in my_dict:
#     print("Hello not in my_dict")
