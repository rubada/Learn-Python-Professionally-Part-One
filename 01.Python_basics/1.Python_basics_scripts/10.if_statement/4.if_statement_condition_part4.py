# Nested if statement, if statement can be used inside another
# if statement
x2 = 500
y2 = 699
z2 = 533
my_list2 = [3, 99]

if x2 < y2:
    if x2 <= z2:
        my_list2.append(z2)
    else:
        my_list2.append(x2)
else:
    if x2 <= z2:
        my_list2.append(z2)
    else:
        my_list2.append(y2)

# print(my_list2)

# pass can be used in if statement in order not to leave the if
# statement empty, and then one can come back later and fill it.
x3 = 500
y3 = 699

if y3 >= x3:
    pass
