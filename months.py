#!/usr/bin/env python
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program shows you what month it is

import math


def main():
    # This function checks what month it is based off a number

    # Input

    chosen_number = int(input("Enter a number between 1-12: "))
    print("")

    # process
    if chosen_number == 1:
        # Output
        print("The month is January")
    elif chosen_number == 2:
        # Output
        print("The month is February")
    elif chosen_number == 3:
        # Output
        print("The month is March")
    elif chosen_number == 4:
        # Output
        print("The month is April")
    elif chosen_number == 5:
        # Output
        print("The month is May")
    elif chosen_number == 6:
        # Output
        print("The month is June")
    elif chosen_number == 7:
        # Output
        print("The month is July")
    elif chosen_number == 8:
        # Output
        print("The month is August")
    elif chosen_number == 9:
        # Output
        print("The month is September")
    elif chosen_number == 10:
        # Output
        print("The month is October")
    elif chosen_number == 11:
        # Output
        print("The month is November")
    elif chosen_number == 12:
        # Output
        print("The month is December")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
