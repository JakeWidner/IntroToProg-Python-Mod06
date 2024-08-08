# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
#       with structured error handling
# Change Log: (Who, When, What)
#   JWidner,8/5/2024,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #

# import JSON module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Processing --------------------------------------- #
class FileProcessor:
    """
    Functions for JSON file processing.

    ChangeLog: (Who, When, What)
    JWidner,8/5/2024,created class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function read the data from a JSON file and return it as a list.

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: list of student data read from the JSON file
        """
        try:
            file = open(file_name, "r")   # Extract the data from the file
            student_data = json.load(file)  # Read from the Json file
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes the data to the JSON file.

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=1)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    IO Functions section

    ChangeLog: (Who, When, What)
    JWidner,8/5/2024,created class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the list of student registered for each course

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: None
        """
        global FILE_NAME  # Use filename constant
        # Process the data to create and display a custom message
        try:
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
        except KeyError as e:  # Key mismatch error handling
            print(f"Key mismatch. Please ensure keys in {FILE_NAME} are correct.")
            print(f"Key {e} not found in {student_data}")
            print(f"Correct the keys in {FILE_NAME} and restart the program.")
        except Exception as e:
            IO.output_error_messages("There was an error displaying data!", e)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        JWidner,8/5/2024,created function

        :return: None
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


#  End of function definitions

# Beginning of the main body of this script
# When the program starts, read the file data into table
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:

    IO.output_menu(menu=MENU)  # Output the menu to the user
    menu_choice = IO.input_menu_choice()  # receive menu choice from user

    if menu_choice == "1":  # Get new data and print out new student data
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # Display current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a JSON file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":  # Exit the program
        break  # out of the loop

print("Program Ended")
