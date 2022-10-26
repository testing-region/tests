def grade_info(score):
    """Find the grade letter & grade point based on score

    Args:
        score (float): score earned in a course

    Returns:
        tuple: grade_letter :str, grade_point :float
    """
    if 85 <= score <= 100:
        return "A+", 4.0
    elif 80 <= score <= 84:
        return "A", 4.0
    elif 75 <= score <= 79:
        return "B+", 3.5
    elif 70 <= score <= 74:
        return "B", 3.0
    elif 65 <= score <= 69:
        return "C+", 2.5
    elif 60 <= score <= 64:
        return "C", 2.0
    elif 55 <= score <= 59:
        return "D+", 1.5
    elif 50 <= score <= 54:
        return "D", 1.0
    elif score < 50:
        return "E", 0.0
    else:
        return "I", None



# CGPA: Cummulative Grade Point Average

def honours_info(CGPA):
    """Returns honours based on CGPA

    Args:
        CGPA (float): Cummulative Grade Point Average

    Returns:
        str: description of honours
    """
    if 3.85 <= CGPA <= 4.0:
        return "Summa Cum Laude"
    elif 3.7 <= CGPA <= 3.84:
        return "Magna Cum Laude"
    elif 3.5 <= CGPA <= 3.69:
        return "Cum Laude"
    else:
        return None


num_courses = int(input("How many courses did you take?: "))

# add new line for readable output
print("")

# variables to count the number of letter grade
num_A_plus = 0
num_A = 0
num_B_plus = 0
num_B = 0
num_C_plus = 0
num_C = 0
num_D_plus = 0
num_D = 0
num_E = 0

# variables to calculate total
total_grade_point = 0
total_weight = 0

# ask for score based on the number of courses
for course in range(num_courses):
    score = float(input(f"Enter score for course {course + 1}: "))
    weight = float(input(f"Enter credit weight for course {course + 1}: "))
    grade_letter, grade_point = grade_info(score)
    
    # Display grade info
    print("Course", course + 1, ":", grade_letter, "with", grade_point, "grade point")

    # add new line for readable output
    print("")

    # count the number of letter grade
    if grade_letter == "A+":
        num_A_plus += 1
    elif grade_letter == "A":
        num_A += 1
    elif grade_letter == "B+":
        num_B_plus += 1
    elif grade_letter == "B":
        num_B += 1
    elif grade_letter == "C+":
        num_C_plus += 1
    elif grade_letter == "C":
        num_C += 1
    elif grade_letter == "D+":
        num_D_plus += 1
    elif grade_letter == "D":
        num_D += 1
    elif grade_letter == "E":
        num_E += 1
    
    # # add grade point to total grade
    ## total_grade_point += grade_point

    # compute total weighted grade points
    total_grade_point += grade_point * weight

    # add weight to total weight
    total_weight += weight
    

# Blank spaces for readable output
print("\n\n")

# letter grade report
print("{0:^15}{1:^40}".format("Grade letter", "Number of letter grade"))
print("-"*50)
print("{0:<15}{1:^40}".format("A+", num_A_plus))
print("{0:<15}{1:^40}".format("A", num_A))
print("{0:<15}{1:^40}".format("B+", num_B_plus))
print("{0:<15}{1:^40}".format("B", num_B))
print("{0:<15}{1:^40}".format("C+", num_C_plus))
print("{0:<15}{1:^40}".format("C", num_C))
print("{0:<15}{1:^40}".format("D+", num_D_plus))
print("{0:<15}{1:^40}".format("D", num_D))
print("{0:<15}{1:^40}".format("E", num_E))

# Blank spaces for readable output
print("\n\n")

## CGPA = total_grade_point / num_courses

CGPA = total_grade_point / total_weight
print("Your cummualative grade point average (GPA) is", round(CGPA, 2))

# Display honours if applicable
honours = honours_info(CGPA)
if honours != None:
    print("Congratulations, You had", honours)