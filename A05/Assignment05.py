# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Xinyuan Zheng,5/21/2025,Updated script with dictionaries and exception handling
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
file = None
menu_choice: str = ''

# Load data from file (if exists)
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print("No existing file found. Starting with an empty student list.")
except json.JSONDecodeError:
    print("File is empty or corrupted. Starting fresh.")
except Exception as e:
    print(f"An error occurred while loading data: {e}")

# Menu Loop
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ").strip()

    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
            course_name = input("Enter the course name: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 50)

    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file)
            print("The following data was saved to file:")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except Exception as e:
            print(f"Error writing to file: {e}")

    elif menu_choice == "4":
        print("Program Ended")
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")
