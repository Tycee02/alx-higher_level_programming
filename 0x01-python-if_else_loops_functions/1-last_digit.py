#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
Thestring = "Last digit of {} is {}".format(number, lastdigit)
if number < 0:
    lastdigit = -(lastdigit)
if lastdigit > 5:
    print(f"{Thestring} and is greater than 5")
elif lastdigit == 0:
    print(f"{Thestring} and is 0")
else:
    print(f"{Thestring} and is less than 6 and not 0")
