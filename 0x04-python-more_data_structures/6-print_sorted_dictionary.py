#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_keys = list(a_dictionary.key())
    order_keys.sort()
    for i in order_keys:
        print ("{}: {}".format(i, a_dictionary.get(i))
