# while loop
# break statement will break the while same as for loop
my_list = [1, 3, 5, 6]
x = len(my_list)
while x > 1:
    print(my_list[x-1])
    if x == 3:
        break
    x -= 1

# Beware when using the continue statement, as shown in below example the while
# loop will continue indefinetely if x1 == 3, because after the condition is
# satisfied, the continue statement will go back to the while loop and continue
# with the loop as long x1 == 3, because the continue will not allow the
# x -=1 be executed.
my_list1 = [1, 3, 5, 6]
# x1 = len(my_list1)
# while x1 > 1:
#     print(my_list1[x1-1])
#     if x1 == 3:
#         continue
#     x1 -= 1

# To solve the above chanhge the counter position to be above the if statement
my_list2 = [1, 3, 5, 6]
x2 = len(my_list2)
# while x2 > 1:
#     print(my_list2[x2-1])
#     x2 -= 1
#     if x2 == 3:
#         continue


# Same as for loop else statement can be used
my_list3 = [1, 3, 5, 6]
x3 = len(my_list3)
while my_list3:
    print(my_list3[x3-1])
    my_list3.pop()
    x3 -= 1
else:
    print(f"list is empty: {my_list3}")
