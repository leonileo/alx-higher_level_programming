#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i][:2] != "__":
            print("{0}".format(names[i]))


if __name__ == "__main__":
    main()
