#!/usr/bin/python3
import sys


def main():
    if len(sys.argv[1:]) == 1:
        first = sys.argv[1]
        print("1 argument:")
        print("{0}: {1}".format(sys.argv.index(first), first))
    elif not sys.argv[1:]:
        print("{0} arguments.".format(len(sys.argv[1:]) ))
    else:
        print("{0} arguments:".format(len(sys.argv[1:])))
        for i in sys.argv[1:]:
            length = sys.argv.index(i)
            print("{0}: {1}".format(length, i))


if __name__ == "__main__":
    main()
