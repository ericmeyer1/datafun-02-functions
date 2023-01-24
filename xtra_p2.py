"""
Eric Meyer

Date Completed: 1/24/2023

Northwest MS-DA couse Data Analytics Fundamentals - Module 2 - Project 2 - Task 7 (Bonus)

Testing for understanding of functions in the xtra problem for module 2 project. Also utilizing doctest to be able to instantly test if you code is working
without having to write out print functions for each function (great and handy for large projects).

>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> add_any(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keywords(a=1,b=2)
3

>>> convert_ctof(0)
32.0

>>> convert_ctof(100)
212.0
"""

import doctest

# define some existing functions


def add_two(first, second):
    """Return the sum of any two arguments."""
    sum = first + second  # fix this line -- DONE
    return sum


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    sum = 0
    for value in list_triangle:
        sum = sum + value  # fix this line to add the value instead of 0 -- DONE
    return sum


def add_any(*args):
    """Return the sum of numbers, using built-in *args."""
    sum = 0
    for x in args:
        sum += x  # fix this line to add x instead of 1 -- DONE
    return sum


def add_any_with_keywords(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += value  # Use the popular and concise version of sum = sum + x -- DONE
    return sum

# TODO: implment a new function to convert celsius to fahrenheit
# Use round as needed to make the test pass
# The name of the function is provided in the docstring above


def convert_ctof(celsius_value):
    """Return the fahrenheit value of a entered celsuis value."""
    fahrenheit_value = int(celsius_value) * (9/5) + 32
    return fahrenheit_value


if __name__ == "__main__":

    doctest.testmod()  # no messages show in terminal meaning doctest was showing that code was correct...I then added code to test convert_ctof
    print()
    # testing results visually in terminal as well! The celsuis to fahrenheit converter works!
    print(f"convert_ctof(0) = {round((convert_ctof(0)),2)}")
    # also set up round function to clean up any results to within two decimal points
    print(f"convert_ctof(100) = {round((convert_ctof(108.55)),2)}")
    print()
