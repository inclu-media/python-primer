# Defining a string variable
name = "Ninja Sensei Martin-san"

# Some useful string operations
################################

# String length
print("The string is %d characters long." % len(name))

# Case vonversion
print("All Uppercase: %s" % name.upper())
print("All Lowercase: %s" % name.lower())
'''
Note that these functions are called in an object-oriented and not
a procedural manner - they are calles as "methods of a string object".
'''

# Finding substrings
substring = "Martin"
pos = name.find(substring)
if pos < 0:
    print("%s was not found in %s." % (substring, name))
else:
    print("%s was found at position %d." % (substring, pos))

# String replacement
new_name = name.replace("Martin", "Matej")
print(new_name)

# Counting substring occurances
letter = "a"
print("\"%s\" occurs %d times in \"%s\"" % (letter, name.count(letter), name))

# Reading a string from a file
filename = "string.txt"
another_name = open(filename).read()
print("Content of %s: \"%s\"" % (filename, another_name))
'''
Check
https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
for the full picture
'''