#!/usr/bin/python3
import sys


def main():
    num = len(sys.argv)
    print("{0} arguments".format(num))
    for i, ar in enumerate(sys.argv[1:], 1):
        if num == 1:
            print("1 argument")
            print("{0}: {1}".format(i, ar))
        else:
            print("{0}: {1}".format(i, ar))


if __name__ == "__main__":
    main()
