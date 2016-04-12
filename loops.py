'''
while loops are being used if we don't know in advance,
how often the loop needs to run.
If the loop needs to run is determined by a boolean run condition.
'''
in_val = ""
while in_val != "exit":
    in_val = raw_input("Stop the loop by entering \"exit\"")


'''
for loops are useful if we know in advance, how often the
loop is going to run.
'''
tune = ["na", "na", "na", "na", "na", "na", "na", "na", "na", "na", "na","na", "na", "na", "Batman!"]
for word in tune:
    print(word)

'''
for loops are often used in order to move a variable through a range of values
'''
for x in xrange(0,10):
    print(x)
