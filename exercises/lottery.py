import random


def lotto_numbers(quant):
    numbers = []
    for x in xrange(0, quant):

        rand = random.randint(0, 46)
        while rand in numbers:
            rand = random.randint(0, 46)
        numbers.append(rand)

    return numbers

count = raw_input("How many lottery numbers do you want to generate?")
# TODO: plausibility check -> max 46 !!
print(lotto_numbers(int(count)))