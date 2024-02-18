#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_key = list(a_dictionary.keys())

    order_key.sort()

    for i in order_key:
        print ("{}: {}".format(i, a_dictionary.get(i)))
