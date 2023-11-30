#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition_result = add(a, b)
    subtract_result = sub(a, b)
    multiply_result = mul(a, b)
    division_result = div(a, b)
    print("{} + {} = {}".format(a, b, addition_result))
    print("{} - {} = {}".format(a, b, subtract_result))
    print("{} * {} = {}".format(a, b, multiply_result))
    print("{} / {} = {}".format(a, b, division_result))
