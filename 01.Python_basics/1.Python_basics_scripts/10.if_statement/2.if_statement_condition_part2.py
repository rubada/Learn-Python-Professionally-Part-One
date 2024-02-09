# Using if, elif and else together
my_list = [9, "cat", 9.7, "dog", [False, True, None], 9]

if 9 not in my_list:
    my_list.append(10)
elif "banana" in my_list:
    print("banana is in my_list")
else:
    my_list.append(88)

# print(my_list)


# If ... else expression can be shortened on one simple line
x = 500
y = 699
z = 633
my_list = [3, 99]

my_list.append(x) if z % 3 == 0 else my_list.append(y)

print(my_list)
