#!/usr/bin/python3
for firstnumber in range(0, 10):
    for secondnumber in range(firstnumber + 1, 10):
        if firstnumber == 8 and secondnumber == 9:
            print("{}{}".format(firstnumber, secondnumber))
        else:
            print("{}{}, ".format(firstnumber, secondnumber), end='')
