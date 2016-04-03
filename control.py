# coding: utf-8

# Control structures
####################
is_sunny = True  # or False
print("Hi there!")
if is_sunny:
    print("What a lovely day!")

# Control structures: 2 alternatives
####################################
is_sunny = False
print("Hi there!")
if is_sunny:
    print("What a lovely day!")
else:
    print("WTF ... !")

# Control structures: n alternatives
#######################################
name = raw_input("Enter your name: ")
if name == "Martin":
    print("Welcome in!")
elif name == "Matej":
    print("You are welcome too!")
else:
    print("I'm not going to let you in!")
'''
Things to note:
- the condition must evaluate to True or False
- the condition does not need to be a boolean variable
- the condition can be a comparison operation
!! '=' assigns, '==' compares
'''