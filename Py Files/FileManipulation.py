

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

    length = -1  # Initialize variable to prevent errors

    try:
        with open(os.path.join(file_path), "r") as file:  # Opens the file for reading

            all_lines = file.readlines()  # Gets all lines as a list of strings

            num_lines = len(all_lines)  # Total of all lines in the file

            if num_lines < line_number:
                print(f"This file doesn't have {line_number} lines.")
            else:
                specific_line = all_lines[line_number-1]
                # Calculates the length of the specific line
                length = len(specific_line)

    except FileNotFoundError:
        print("\nWrong file or file path.")
        print("Remember to add an extension to file you entered.")
    except IOError as e:
        print("\nThere is an Error\n", e)
    else:
        print("No exceptions.\nUnknown Error found.")

    # Checks to see if the calculation of the length was successful
    if length == -1:
        print("\nThere was an error.")
    else:
        print(f"The length of line {line_number} is --> {length}\n")


#################################################################################
# Question 2
#################################################################################


def checkWordCount():
    # Asks user for file location
    file_path = input(
        "*  PLease enter the absolute file path to the file that you want to check the length.\n")
    # Asks user for line number
    line_number = input(
        "*  Please enter the line number that you want the length for - ")
    line_number = int(line_number)

    word_count = -1  # Initialize variable to prevent errors

    try:
        file = open(file_path, "r")  # Opens the file for reading

        all_lines = file.readlines()  # Gets all lines as a list of strings

        num_lines = len(all_lines)  # Total of all lines in the file

        if num_lines < line_number:
            print(f"This file doesn't have {line_number} lines.")
        else:
            specific_line = all_lines[line_number-1]
            all_words = specific_line.split()
            word_count = len(all_words)

    except FileNotFoundError:
        print("\nWrong file or file path.")
        print("Remember to add an extension to file you entered.")
    except IOError as e:
        print("\nThere is an IO Error\n", e)
    else:
        print("No exceptions.\nUnknown Error found.")
    finally:
        file.close()

    # Checks to see if the counting of the words were successful
    if word_count == -1:
        print("There was an error.")
    else:
        print(f"The length of line {line_number} is --> {word_count}")


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
            print(f"\n\'{option}\' is not a valid option.")
            print("Please try again.")

        displayMenu()

    print("Exiting.")
    sys.exit(0)
