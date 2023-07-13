#!/usr/bin/python3
# Owned By MoOka

from sys import argv
if __name__ == "__main__":
    res = 0
    for ar in range(1, len(argv)):
        res = res + int(argv[ar])
    print("{}".format(res))
