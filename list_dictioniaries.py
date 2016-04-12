# List initialisation
weekdays = list(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

'''
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
works too
'''

# There is something missing ...
weekdays.append("Sunday")
print(weekdays)

# Count list elements
print("The week consists of %d days" % len(weekdays))

# Existence and index
weekday = raw_input("Enter a weekday: ")
if weekday in weekdays:
    print("%s is the %d. weekday" % (weekday, weekdays.index(weekday) + 1))
else:
    print(weekday + "is not a valid weekday.")

# Dictionaries
vampire_cake = {
    "Sugar": "1 cup",
    "Flour": "2 cups",
    "Salt": "1 pinch",
    "Milk": "1 litre",
    "Garlic": "10 cloves"
}
print("For Vampire Cake you need: ")
print(" & ".join(vampire_cake.keys()))
ing = raw_input("Enter the name of the ingredient and I tell you how much you need: ")
if ing in vampire_cake.keys():
    print(vampire_cake[ing])
else:
    print("You don't need %s for Vampire Cake." % ing)


