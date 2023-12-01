#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    if arg_num == 0:
        print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
    else:
        print("{} arguments:".format(arg_num))
    if arg_num >= 1:
        arg_num = 0
    for arg in sys.argv:
        if arg_num != 0:
            print("{}: {}".format(arg_num, arg))
        arg_num += 1
