#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 07, 2022
# This program generates 10 random numbers and adds them to a list,
# then it finds the max value of those numbers and displays displays it.


# Imports random Module.
import random


# Function for finding max value.
def find_max_value(list_of_int, max_value):
    # initializes max value to -1.
    max_value = -1
    # Loop used to find max value.
    for counter in range(0, 10):
        if max_value < list_of_int[counter]:
            max_value = list_of_int[counter]
        else:
            continue
    # Returns max value.
    return max_value


def main():
    # Initializes list
    list_of_num = []
    # Initializes max value
    max_value = 0
    # Loop used to generate random numbers.
    for counter in range(0, 10):
        # Creates a variables and makes it a random number ranging from 0-100.
        random_num = random.randint(0, 100)
        # Appends the random number to the list.
        list_of_num.append(random_num)
        # Displays the random number.
        print(f"Added {random_num} at list place {counter}")
    # Calls function.
    max_value = find_max_value(list_of_num, max_value)
    # Displays max value.
    print(f"Your max value is {max_value}")


if __name__ == "__main__":
    main()
