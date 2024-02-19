#!/usr/bin/python3
"""prints a function"""


def say_my_name(first_name, last_name=""):
    """ function that prints first and last name.

    ARGS
        @first name: first name from input
        @last mane: last name of user
    
    Error
        TypeError: first_name must be a string or last_name must be a string.

        prints the first and last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))

