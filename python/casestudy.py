class_list = {}


def register():
    print("Enter an empty space when done!!!")

    while True:
        name = input("Enter student name: ")
        if name != "":
            class_list[name] = {}
        else:
            break


def enter_grades():
    assignment_name = input("Enter the assignment name: ")
    total = int(input("Enter the total points: "))

    for key in class_list.keys():
        score = int(input(f"Enter the score for {key}: "))

        if score > total:
            print("Error: Exceeds total grade.")
            print(f"Try again: Score should be less than or equal to {total}")
            score = int(input(f"Enter the score for {key}: "))

        class_list[key][assignment_name] = score


def list():
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


# our menu
while True:
    print("1. Register students")
    print("2. Enter grades")
    print("3. List students and their grades")
    print("4. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        register()
    elif option == 2:
        enter_grades()
    elif option == 3:
        list()
    elif option == 4:
        break
    else:
        print("Invalid option, try again")
        continue
