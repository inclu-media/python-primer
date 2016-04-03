import random

guess_me = random.randint(0, 10)

my_guess = -1

while guess_me != my_guess:
    my_guess = int(raw_input("What number between 0 and 10 am I thinking of? "))
    if guess_me == my_guess:
        print("Great, you got it! The number is %d." % guess_me)
    elif my_guess < guess_me:
        print("Your number is too small. Try again.")
    else:
        print("Your number is too big. Try again")
