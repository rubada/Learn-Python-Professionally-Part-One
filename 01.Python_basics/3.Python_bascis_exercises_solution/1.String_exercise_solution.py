# String Exercise Solution
"""If there any question please ask you question in github discussion
https://github.com/rubada/Learn_Python_in_Arabic/discussions"""

sent1 = "Hello, I like to watch movies, my favorite genres are action,\
    fantasy, drama, sci-fi. Do you agree with me?"
sent2 = "Hi, some of the movies I watch, has a great soundtracks right! that's\
    right I like listening to music also!"

# 1st question:
# what is the use of the backslash in both string?
"""When using the backslash, Python will recoginze it as the line
continuation either in string or code line as shown below"""
a = 3 + 2 \
    + 8
# print(a)

"""If the code has (), [], {}, there is node need to use the backslash
for line continuation.
() used in function there is no need to use backslash for line continuation.
The same rule applies in lists [], sets and dictionary {} and tupples()"""
b = (3 + 6 + 8 + 10
     + 6)
# print(b)

# 2nd question:
# how many characters are in sent1, charaters include letters, whitespace,
# commas, etc.
len_sent1 = len(sent1)
# print(len_sent1)

# 3rd quesrion:
# In sent1 print the letter "m" in "my" using indexing.
find_m = sent1.find("my")
# print(sent1[find_m])

# 4th question:
# In sent2 slice the part "has a great soundtracks" and create a new
# variable for this new text, use both negative and standard Indexing.

# standard Indexing
first_ind = sent2.index('has a')
last_ind = sent2.index('right!')
# print(sent2[first_ind:last_ind-1])  # -1 to remove the whitespace

# negative Indexing
len_sent2 = len(sent2)
first_neg_index = first_ind - len_sent2
last_neg_index = last_ind - len_sent2
# print(sent2[last_neg_index:first_neg_index:-1])

# 5th question:
# Get the rerverse for "I like to watch movies,"in sent1 using both negative
# and standard indexing.

# standard Indexing
first_ind_sent1 = sent1.index('I like')-1       # -1 to add "I"
last_ind_sent1 = sent1.index('my favorite')-2   # -2 to remove m and whitespace
# print(sent1[last_ind_sent1:first_ind_sent1:-1])

# negative Indexing
first_neg_ind = first_ind_sent1 - len_sent1
last_neg_ind = last_ind_sent1 - len_sent1
# print(sent1[last_neg_ind:first_neg_ind:-1])

# 6th question:
# Count the number of "right" in sent2.
# print(sent2.count("right"))

# 7th question:
# Create a list of words from sent1, and remove all characters like commas,
# dots, etc.
sent1_list = sent1.replace(",", "").strip("?").split()
# print(sent1_list)

# 8th question:
# Below a variable "a" is defined repeat the variable 4 times.
# Then add this varibale in a sentence you choose.
a = "Python"
# print(a*4)

my_sent = (f"{a} is a programming language that is used in different"
           " application")  # () allows string continuation
# print(my_sent)
