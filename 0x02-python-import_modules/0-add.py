#!/usr/bin/python3
from add_0 import add
a = 1
b = 2
c = add(a, b)


def main():
    """ main function """
    print("{0} + {1} = {2}".format(a, b, c))


if __name__ == "__main__":
    main()
