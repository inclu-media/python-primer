shopping_list = []
add_more = "YES"  # needs to be initialised otherwise the while loop would not start

while add_more == "YES":
    item = raw_input("What do you want to add to the list? ")
    shopping_list.append(item)
    add_more = raw_input("Do you want to add more items? (yes|no) ")

    '''
    By converting the input string to upper case, we automatically cover
    YES, Yes, yes, etc ....
    Every input which is not a yes stops the input.
    '''
    add_more = add_more.upper()
print(shopping_list)
