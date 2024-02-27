dict_keys = ["name", "country", "birth_year"]
dict_values = [["Jon Wade", "Sam Python", "Ahmad Yassin"],
               ["UK", "Australia", "Jordan"],
               [2000, 1998, 2004],
               ]
# 1st Question
# Create a new dictionary using the above lists.
personal_data = {}
for i in range(len(dict_keys)):
    personal_data[dict_keys[i]] = dict_values[i]

# print(personal_data)

# 2nd Question
# Update the above dictionary with the following values:
new_data = ["Mohammad Hossni", "Eygpt", 1997]
for i in range(len(personal_data)):
    key = dict_keys[i]
    personal_data[key].append(new_data[i])

# print(personal_data)


# 3rd Question
# Add the following dictionary by updating the above dictionary:
new_dict = {"gender": ["F", "M", "F", "M"]}
new_dict1 = {"id_number": [233747575, 345744576, 678924687, 788954524]}

# personal_data |= new_dict
# personal_data |= new_dict1
# print(personal_data)

# or
# personal_data.update(new_dict)
# personal_data.update(new_dict1)
# print(personal_data)


# 4rth Question
# Create a dictionary where the keys are the numbers from 1 to 10,
# both 1 and 10 should be included and the values are the square of
# of the key.
keys_dict = [*range(1, 11)]

square_number = {}
for i in range(len(keys_dict)):
    square_number[i+1] = (i+1)**2
# print(square_number)
