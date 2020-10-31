

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
    else:  # perform actions that must occur when no exception occurs
        print("All lines were successfully read.\n")

    # Checks to see if the calculation of the length was successful
    if length == -1:
        print("\nThere was an error.")
    else:
        print(f"The length of line {line_number} is --> {length}.\n")


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
    else:  # perform actions that must occur when no exception occurs
        print("All lines were successfully read.\n")
    finally:
        file.close()

    # Checks to see if the counting of the words were successful
    if word_count == -1:
        print("There was an error that caused a miscalculation.")
    else:
        print(
            f"The number of words in line {line_number} is --> {word_count}.\n")


#################################################################################
# Question 3
#################################################################################


def squeezRep():
    # Asks user for file location
    file_path = input(
        "*  PLease enter the absolute file path to the file that you want to check the length.\n")

    lines_list = list()
    new_list = list()

    try:
        # Opens the file for reading
        with open(os.path.join(file_path), "r") as reader:

            for line in reader.readlines():
                # Break up the string into a list of words
                all_words = line.strip().split()
                # Adds all the word lists to another list
                lines_list.append(all_words)

    except FileNotFoundError:
        print("\nWrong file or file path.")
        print("Remember to add an extension to file you entered.")
    except IOError as e:
        print("\nThere is an Error\n", e)
    else:  # perform actions that must occur when no exception occurs
        print("All lines were successfully read.\n")

    new_line = ""
    # Recreates the lines with 1 whitespace
    for lst in lines_list:
        for word in lst:
            new_line += (word + " ")

        new_list.append(new_line + "\n")
        new_line = ""

    # Truncates the file and opens it for writing
    try:
        file = open(os.path.join(file_path), "w")

        # for lines in new_list:
        #     # Adds every line to the list
        #     file.write(lines)

        file.writelines(new_list)  # Adds every line to the list

    except FileNotFoundError:
        print("\nWrong file or file path.")
        print("Remember to add an extension to file you entered.")
    except IOError as e:
        print("\nThere is an Error\n", e)
    else:  # perform actions that must occur when no exception occurs
        print("Successfully squeezed the white spaces in the file.")
    finally:
        reader.close()


#################################################################################
# Question 4
#################################################################################


def sizeOfFile():

    file_path = input(
        "*  PLease enter the absolute file path of the file that you want to check the size of.\n")

    lines_list = list()

    total_size = -1  # Initialize variable to prevent errors

    try:
        file = open(file_path, "r")  # Opens the file for reading

        # Moves the file cursor to end of the file
        file.seek(0, os.SEEK_END)

        # Get the current cursor position and calculates the bytes
        # based on the location (end of the file)
        total_size = file.tell()

    except FileNotFoundError:
        print("\nWrong file or file path.")
        print("Remember to add an extension to file you entered.")
    except IOError as e:
        print("\nThere is an Error\n", e)
    else:  # perform actions that must occur when no exception occurs
        print("Successfully calculated the size of the file.")

    # Checks to see if the calculations were done properly
    if total_size == -1:
        print("There was an error that caused a miscalculation.")
    else:
        print(f"The total size is {total_size} bytes.")

    return total_size

#################################################################################
# Question 5
#################################################################################


def calcPercentage():

    import fnmatch

    file_path = input(
        "*  PLease enter the absolute file path to the folder of yor choice.\n")

    total_files, file_num = -1, -1  # Initialize variable to prevent errors

    try:
        # This will calculate the total number of files
        dir_path, dir_name, dir_files = next(os.walk(file_path))
        total_files = len(dir_files)

        # This will print all file names in the current directory with the extension
        file_num = len(fnmatch.filter(os.listdir(file_path), '*.java'))
    except IOError as e:
        print("\nThere is an Error\n", e)

    # Calculates the percentage of files
    try:
        percentage = (file_num / total_files) * 100
    except ZeroDivisionError:
        print("There was a division with zero.")
        print(
            f"The variables: \'total_files\'- {total_files} and \'file_num\'- {file_num}.")
    else:
        print(f"The percentage of \'.java\' files is {percentage}%.")

#################################################################################
# Helper Section
#################################################################################


def displayMenu():
    """
        This function displays the menu.

        Args:
            None
        Returns:
            None
    """
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
            checkWordCount()
        elif (option == "3"):
            squeezRep()
        elif (option == "4"):
            sizeOfFile()
        elif (option == "5"):
            calcPercentage()
        elif (option == "Q" or option == "q"):
            break
        else:
            print(f"\n\'{option}\' is not a valid option.")
            print("Please try again.")

        displayMenu()

    print("Exiting.")
    sys.exit(0)
