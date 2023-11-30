#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    arg_num = len(arguments)
    if arg_num != 1:
        print("{} arguments".format(arg_num), end='')
    else:
        print('' "{}".format(arg_num), end=' ')
    if arg_num > 0:
        print(': ')
    else:
        print('.\n')
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
    if arg_num == 0:
        print('.')
