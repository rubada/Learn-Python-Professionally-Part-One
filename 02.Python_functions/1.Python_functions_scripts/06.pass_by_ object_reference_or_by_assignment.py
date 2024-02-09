# In programing languages, the variables can be passed to a function either by:
# 1.Pass by value.
# 2.Pass by reference.
# Are functions in Python pass by value or pass by reference?
# It is neither, let's see why?

# 1.Pass by value means passing a copy of the variable or object to the
# function, then if the parameter or argument is changed or modified inside
# the function, the variable or object value outside the function will not be
# modified, because they don't share the same memory address.
# Below example may appear that python is using pass by value but it is not.
def add_item(list_arg):
    list_arg = [1, 2, 5, 6]
    list_arg.append(44)
    return list_arg


mylist = [1, 2, 5, 6]
# Calling the function doesn't affect the variables outside the function
add_item(mylist)
# print(mylist)


# 2.Passing by reference means passing the same memory address of the variable
# or object to its corresponding parameter or argument, when calling the
# function, and if the parameter value is changed inside the function, the
# variable or object value will be changed outside the function.
# That's means when  the function is called, the function parameters or
# arguments, have the same memory address as the variables used as arguments
# outside the function, that's why the variable or object value changed.
# Below example shows also that python is using pass by reference
def add_to_args(list_arg):
    list_arg.append(77)
    return list_arg


mylist1 = [1, 2, 5, 6]
# print("my_list before calling the function", mylist1)
# print("\n")
# calling the function
# add_to_args(mylist1)
# print("my_list after calling the function", mylist1)

# As shown above the examples sometimes functions behave as pass by value and
# and sometimes behave as pass by reference but this is not true, because
# functions in Python behave as pass by object reference or pass by assignment.
# To explain it let's recall what we learned before, an object has three
# charactersitics: type, value and identity, as we learned the identity and
# type will not change once the object is created, but the value or content
# can be changed or modified if the object is mutable, but it will not change
# or modified if the object is immutable.
# Also we learned that when equal sign id used to assign obj1 to obj2, this
# means that obj1 is obj1
obj1 = [1, 2, 3, 4]
obj2 = foo = mylist = obj1
# obj2, foo, mylist and obj1 are all the same id number same object, same
# memory address

# but when assigning the same list to a new variable they are not the same
# object
obj3 = [1, 2, 3, 4]
# print(obj1 is obj3)  # False
# print(id(obj1))
# print(id(obj2))
# print(id(obj3))

# Even if they have the same variable name
y = [1, 2]
# print(id(y))
y = [1, 2]
# print(id(y))

# To wrap up the above the variable name given to an object, it is just a
# label or name, sometimes there are many variables with different labels or
# names but refer to the same object, with the same memory address.
# And sometimes there are variables with the same name or labels but refer to
# a different objects with different memory addresses.
# So, when the function is called each parameter become the label that is
# assigned to an object, maybe they refer to the same objects or different
# objects.


# That why in below example when defining a variable inside the function,
# although it has the same value of the argument or variable outside the
# function, but they are different objects, and thus changing the list value
# inside the function, by using the append method will not change the values
# in my_list1 outside the function, because they are two different objects.
# (Same as obj1 and obj3 and y variables mentioned above)
def add_item1(list_arg):
    list_arg = [1, 2, 5, 6]
    list_arg.append(44)
    return list_arg


mylist1 = [1, 2, 5, 6]
add_item1(mylist1)
# print(mylist1)


# The same for imutable objects, x = 30 and x = 2 are two different objects,
# and when x is changed inside the function it will not change the x outside
# the function.
def num(x):
    x = 30
    return x


x = 2
num(x)
# print(x)

# Note if a variable is defined inside the function, it's better to give it
# a different name, not the same name as the function parameter. In this way
# both the variable (defined inside the function) and the parameter can be used
# inside the function.


# In the example below, both variables (parameters and arguments) are the same
# object with same memory address, regardless that they have different labels
# or name, (same as obj1 = obj2 mentioned above), in this case when the
# variable is changed inside the function it will be changed outside function
# list_
def add_to_args1(list_arg):
    list_arg.append(77)
    return list_arg


mylist2 = [1, 2, 5, 6]
add_to_args1(mylist2)
# print(mylist2)

# It is important when creating a function and using mutable objects, don't
# change the arguments inside the function, even if they are not returned,
# because once changed inside the function, they will be changed outside the
# function, and this will affect your code output if these variables are used
# in another part of your code.
