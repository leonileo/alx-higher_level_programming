#!/usr/bin/python3
import sys


def main():
    length = 0
    num = len(sys.argv) - 1
    if num != 1:
        print("{0} arguments:".format(num))
    for i in sys.argv[1:]:
        length += 1
        if num == 1:
            print("1 argument:")
            print("{0}: {1}".format(length, i))
        else:
            print("{0}: {1}".format(length, i))


if __name__ == "__main__":
    main()
