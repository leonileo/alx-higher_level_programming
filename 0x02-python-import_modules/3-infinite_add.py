#!/usr/bin/python3
import sys


def main():
    sum = 0
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            sum += int(i)
    print(sum)


if __name__ == "__main__":
    main()
