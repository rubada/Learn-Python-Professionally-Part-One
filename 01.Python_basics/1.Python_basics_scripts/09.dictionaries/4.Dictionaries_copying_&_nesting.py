# Dictionay Copying
# To copy a dictionary, use the copy method, don't use dict1 = dict2, the
# result will be the same object, where any change in dict1 will change dict2
my_dict = {"color": "red", "fruit": "banana", "year": 1988,
           "age": 20}
my_dict1 = my_dict.copy()
# print(my_dict1)

# or dict() function can be used to copy a dictionary
my_dict2 = dict(my_dict)
# print(my_dict2)

# Nested dictionaries
# Nesting is adding many dictionaries inside one main dictionary
person1 = {"name": "John",
           "age:": 22,
           "country": "USA"}

person2 = {"name": "Henry",
           "age:": 30,
           "country": "UK"}

person3 = {"name": "Luca",
           "age:": 15,
           "country": "Italy"}

person_data = {"Person1": person1,
               "Person2": person2,
               "Person3": person3}

print(person_data)

# Accessing a nested dictionay:
name1 = person_data["Person1"]["name"]
# print(name1)
