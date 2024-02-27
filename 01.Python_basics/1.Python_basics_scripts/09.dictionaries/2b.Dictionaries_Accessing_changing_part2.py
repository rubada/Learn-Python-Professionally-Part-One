# Dictionary Accessing
# Accessing the values in the dictionary, by using the values method,
# Same as keys the value list is a viewed object, any change in the
# dictionary will change or modify the view list.
my_dict = {"color": "red", "fruit": "banana", "year": 1988,
           "age": 20}
values_dict = my_dict.values()
# print(values_dict)

my_dict["year"] = 2000
my_dict["animal"] = "cat"
# print(my_dict)
# print(values_dict)

my_dict1 = {"color": "red", "fruit": "banana", "year": 1988,
            "age": 20}
# The items() method return the dictionary as tuples inside a list:
my_list = my_dict1.items()
# print(my_list)

my_dict1["year"] = 2015
my_dict1["animal"] = "dog"
# print(my_dict1)
# print(my_list)

# Another way to change or modify a dictionary, use the update() method.
my_dict2 = {"color": "red", "fruit": "banana", "year": 1988,
            "age": 20}
my_dict2.update({"year": 2008, "animal": "cat"})
# print(my_dict2)

# To merge two dictionary, there are two ways which are introduced in
# Python version 3.9, and all the versions after 3.9 have this method.
my_dict3 = {"color": "red", "fruit": "banana", "year": 1988,
            "age": 20}
my_dict4 = {'name': ['John', 'Henry', 'Luca'], 'age': [22, 30, 15],
            'country': ['USA', 'UK', 'Italy']}

new_dict = my_dict3 | my_dict4
# print(new_dict)

# Or updating a dictionary
my_dict3 |= my_dict4
print(my_dict3)
