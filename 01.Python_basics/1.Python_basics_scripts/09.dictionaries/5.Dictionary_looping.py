# Dictionay Looping
# for looping can be used to access dictionary items:
my_dict = {"color": "red", "list": [1, 32, 76], "tuple": (5, 7),
           "set": {5, "yellow"}, "dict": {"a": "banana", "b": 8}
           }
# for item in my_dict:
#     print(item, ":",  my_dict[item])

# keys() method can be used to print keys
# for key in my_dict.keys():
#     print(key)

# values() method can be used to print values
# for value in my_dict.values():
#     print(value)

# To get the keys and values use items() method
# for key, value in my_dict.items():
#     print(key, ":", value)

# for loop can be used to create a dictinary
keys = ["name", "age", "country"]
values = [["John", "Henry", "Luca"],
          [22, 30, 15],
          ["USA", "UK", "Italy"]]

person_data = {}

for i in range(len(keys)):
    person_data[keys[i]] = values[i]

# print(person_data)
