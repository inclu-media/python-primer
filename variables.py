# coding: utf-8

# Different variable types
# Point out difference to strongly typed languages

age = 43  # integer
temperature = 18.25  # float
name = "Kurt Müller"  # string
is_sunny = True  # boolean
is_rainy = False  # boolean

# Printing variables
####################

print(age)
'''
This will yield an error as the interpreter does not know about the encoding of the file
add # coding: utf-8 as first line.
'''

# Print formatting
print("My name is " + name)
# print("My name is " + name + " and I am " + age + " years old.")
'''
Here python-primer has problems: age is an integer and the plus operator could either mean adding
the number or concatenating them.
There are two possible solutions:
'''
print("My name is " + name + " and I am " + str(age) + " years old.")  # concatenation -> ok
print("My name is %s and I am %d years old" % (name, age))  # interpolation -> better

# Capturing variables
#####################







