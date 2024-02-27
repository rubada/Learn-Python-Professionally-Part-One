# Functions
# Arguments Types:
# 1. Default argument
# 2. Keyword arguments (named arguments)
# 3. Positional arguments
# 4. Arbitrary arguments (*args and **kwargs)

# 4. Arbitrary arguments (*args and **kwargs) if number of arguments is unknown
# arbitrary arguments can be used because when using this type of arguments
# any number of arguments can be passed when the function is called.


# There are two types of arbitrary arguments
# 1. *args (Positional Arguments), the args name can be changed with any other
# name, single * (asterisk) should be used before this name to define it as
# positional argument.

def create_sentence(*args):
    sentence = ""
    for word in args:
        sentence = sentence + word + " "
    return args, sentence


# Calling the function it will return a tuple when using *args
sent_tuple, sentence = create_sentence("Hello", "this", "is", "a", "string")
# print(sent_tuple)
# print(sentence)


# 2. **kwargs (Keyword Arguments) the kwargs name can be changed with any other
# name, double ** (asterisk) should be used before this name to define it as
# keyword argument.
def create_sentence1(**kwargs):
    sentence = ""
    for value in kwargs.values():
        sentence = sentence + value + " "
    return kwargs, sentence


# Calling the function it will return a dictionary when using **kwargs
sent_dict, sentence1 = create_sentence1(word1="Hello", word2="this",
                                        word3="is", word4="a",
                                        word5="string1")
# print(sent_dict)
# print(sentence1)


# Arbitrary arguments can be used with other arguments, such as positional,
# default and keyword arguments.

def create_sentence2(word1, word2, *args, **kwargs):
    sentence = word1 + " " + word2 + " "
    for value in args:
        sentence = sentence + value + " "
    for value in kwargs.values():
        sentence = sentence + value + " "
    return sentence


sentence2 = create_sentence2("Hello",
                             "this",
                             "is",
                             word4="a",
                             word5="string2")
# print(sentence2)


# Note: when defining a function with parameters, the keyword arguments should
# be assigned after the positioned arguments.
def create_sentence3(word1, word2, word3, word4, word5):
    sentence = ""
    sentence = f"{word1} {word2} {word3} {word4} {word5}"
    return sentence


# sentence3 = create_sentence3("Hello", "this", "is",
#                              word4="a",
#                              word5="string3")

# Calling or invoking the function as shown below will raise an error:
# sentence3 = create_sentence3(word1="Hello",
#                             "this", "is",
#                             word4="a",
#                             word=5,
#                             word5="string")
# print(sentence2)
