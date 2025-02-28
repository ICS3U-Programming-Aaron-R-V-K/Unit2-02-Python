#!/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: Feb 27, 2025
# The code calculates the circumference of a Circle using Tau
import constants


def main():
    # get radius fromm the usr
    radius = float(input("Enter the radius of the circle (m):"))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display circumference
    print("")
    print("circumference = {} m".format(circumference))


if __name__ == "__main__":
    main()
