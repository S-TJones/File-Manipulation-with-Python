

# Pop Quiz

import math
import os
import random
import sys

#################################################################################
# Question 1
#################################################################################


def checkLength():
    # Asks user for file location
    file_path = input(
        "\n*  PLease enter the file path to the file that you want to check the length of.\n")

    # Asks user for line number
    line_number = input(
        "*  Please enter the line number that you want the length for - ")
    line_number = int(line_number)

    length = 0

    with open(os.path.join(file_path), "r") as file:

        all_lines = file.readlines()

        num_lines = len(all_lines)
        if num_lines < line_number:
            print(f"This file doesn't have {line_number} lines.")
        else:
            specific_line = all_lines[line_number-1]
            length = len(specific_line)

    if length == 0:
        print("There was an error.")
    else:
        print(f"The length of line {line_number} is --> {length}\n")

#################################################################################
# Helper Section
#################################################################################

# This function displays the menu


def displayMenu():
    print()
    print("1. Check the length of a line from a text file.")
    print("2. Check the word count of a line from a text file.")
    print("3. Squeeze repition spaces in a text file.")
    print("4. Calculate total size of files in a dir and sort them in a file.")
    print("5. Calculate the size percentage of \'.java\' files in a dir.")
    print("Q. To exit.")

#################################################################################
# Driver Section
#################################################################################


if __name__ == "__main__":

    print("Welcome to Pop Quiz.")

    displayMenu()

    while (True):
        option = input("\nEnter an option - ")

        if (option == "1"):
            checkLength()
        elif (option == "2"):
            pass
        elif (option == "3"):
            pass
        elif (option == "4"):
            pass
        elif (option == "5"):
            pass
        elif (option == "Q" or option == "q"):
            break
        else:
            print(f"\n \'{option}\' is not a valid option.")
            print("Please try again.")

        displayMenu()

    print("Exiting.")
    sys.exit(0)
