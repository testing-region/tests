# json will be used to load/save dictionary data to/from a file
import json


def load_data():
    """
    Loads previously saved data

    Returns
    -------
    dict
        a dictionary of students' data (having names and assignment data)
    """
    with open("./student_data.txt", "r") as f:
        return json.load(f)  # reads a dictionary in a file


class_list = load_data()


def register():
    """
    Allows a user to register new students
    """
    print("Enter an empty space when done!!!")

    # enter students' name until the user enters an empty space
    while True:
        name = input("Enter student name: ")
        if name != "":
            class_list[name] = {}
        else:
            break


def enter_grades():
    """
    Allows a user to enter the grades for students
    for a particular assignment
    """
    assignment_name = input("Enter the assignment name: ")
    total = int(input("Enter the total points: "))

    # create a query for every student
    for key in class_list.keys():
        score = int(input(f"Enter the score for {key}: "))

        # check if score exceeds total mark
        # return error and prompt for another input
        # P.S. Multiple input errors are not handled
        if score > total:
            print("Error: Exceeds total grade.")
            print(f"Try again: Score should be less than or equal to {total}")
            score = int(input(f"Enter the score for {key}: "))

        # store the score for the particular assignment
        class_list[key][assignment_name] = score


def list():
    """
    List the student names and their scores for each
    corresponding assignment
    """
    # key1 -> student name
    # val1 -> dictionary (assignment_name, grade)
    for key1, val1 in class_list.items():
        print("Student name:", key1)

        # key2 -> assignment_name
        # val2 -> grade
        for key2, val2 in val1.items():
            print("Assignment name:", key2)
            print("Score:", val2)

        print()


def save_data(data):
    """
    Saves students' data when the program exits

    Parameters
    -----------
    data
        a dictionary of students' data (having names and assignment data)
    """
    with open("./student_data.txt", "w") as f:
        json.dump(data, f)  # writes a dictionary to a file


# our menu
while True:
    print()
    print("1. Register students")
    print("2. Enter grades")
    print("3. List students and their grades")
    print("4. Exit")
    print()

    option = input("Select an option: ")
    print()

    if option == "1":
        register()
    elif option == "2":
        enter_grades()
    elif option == "3":
        list()
    elif option == "4":
        save_data(class_list)
        break
    else:
        print("Invalid option, try again")
        print()
        continue
