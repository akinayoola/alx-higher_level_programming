#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 113 and chr(letter) != 103:
        print("{}".format(chr(letter)), end="")
