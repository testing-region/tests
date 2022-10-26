num_students_init = 62
registered_students = 133

# increase = final value - initial value
num_student_increase = registered_students - num_students_init

percent_increase = (num_student_increase / num_students_init) * 100
print("The percentage increase in the number of students is", round(percent_increase, 2), "%")
