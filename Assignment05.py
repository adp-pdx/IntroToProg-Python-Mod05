# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Adam Packer, 3/18/2025, Started with Starter Code, updated code to reflect assignment requirements
# ------------------------------------------------------------------------------------------ #

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
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)  # parse the JSON into a Python list of dictionaries
    file.close()
except FileNotFoundError:
    print("File not found. Starting with an empty 'students' list.")
    students = []
except json.JSONDecodeError:
    print("JSON file was empty or invalid. Starting with an empty 'students' list.")
    students = []

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.strip():
                raise ValueError("First name cannot be empty!")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.strip():
                raise ValueError("Last name cannot be empty!")

            course_name = input("Please enter the name of the course: ")
            if not course_name.strip():
                raise ValueError("Course name cannot be empty!")

            student_data = {
                "student_first_name": student_first_name,
                "student_last_name": student_last_name,
                "course_name": course_name
            }
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(f"Error: {e}")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(
                f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)  # writes the entire list of dictionaries to the JSON file
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(
                    f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']}")
        except Exception as e:
            print("An error occurred while writing to the file:", e)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
