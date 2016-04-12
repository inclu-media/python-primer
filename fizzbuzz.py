inval = -1
while inval > 100 or inval < 0:
    inval = int(raw_input("1-100: "))

for counter in xrange(1, inval+1):

    div3 = (counter % 3 == 0)
    div5 = (counter % 5 == 0)

    if div3 and div5:
        print("fizzbuzz")
    elif div3:
        print("fizz")
    elif div5:
        print("buzz")
    else:
        print(counter)
