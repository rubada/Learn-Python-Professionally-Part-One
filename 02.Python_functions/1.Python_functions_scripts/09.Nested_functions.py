# Nested Function or Inner Function
# A function which is defined inside another function is called an inner
# function or nested function.
# Inner function is protected from everything happening outside the function
# this is called encapsulation.
def outerFunc():
    print("This is the outer function")

    def innerFunc():
        print("This is the inner function")
    innerFunc()


# outerFunc()


# Also parameters and arguments can be used as shown below
def outerFunc1(text):
    print(f"outer function {text}")

    def innerFunc1():
        print(f"inner function {text}")
    innerFunc1()


# outerFunc1("Hello World!")


# "return" keyword can be used inside the outer function to return the inner
# function, and also it can be used inside the inner function to return its
# result
def outerFunc2(text):
    x = f"outer function {text}"

    def innerFunc2():
        return f"inner function {text}"
    return innerFunc2(), x


# print(outerFunc2("Hello World!!!"))

# In nested function the outer function will return the inner function, in
# order to get the result returned from the inner function, because as
# mentioned above the inner functions are protected from everything happening
# outside.


# Scope of a variable
# As mentioned in part 8 variables scope, there is a third scope called
# nonlocal scope, which is used in a nested function, as shown below:
def outerFunc3():
    def innerFunc3():
        text = "local"
        return text
    return innerFunc3()


# print(outerFunc3())

# Accessing the nonlocal variable of the outer function from the inner function

def outerFunc4():
    text = "nonlocal"

    def innerFunc4():
        return text
    return innerFunc4()


# print(outerFunc4())


# To modify the local variable inside the inner function, nonlocal
# keyword should be used if the nonlocal keyword is not used inside the inner,
# the UnboundLocalError will be raised.
def outerFunc5():
    num = 5

    def innerFunc5():
        nonlocal num
        num = num + 4
        return num
    return innerFunc5(), num


num_inner, num_outer = outerFunc5()
# print(num_inner)
# print(num_outer)
