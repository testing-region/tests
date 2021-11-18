class Student:
    def __init__(self, name, student_id, gender, major, yeargroup):
        self.name = name
        self.student_id = student_id
        self.gender = gender
        self.major = major
        self.yeargroup = yeargroup

    def change_major(self, new_major):
        self.major = new_major
    
    def __str__(self):
        return f'{self.name}, a {self.gender}, with student ID {self.student_id} is in year group {self.yeargroup}. Majoring in {self.major}'
    
    # get all variables from init separately
    def get_name(self):
        return self.name
    
    def get_student_id(self):
        return self.student_id
    
    def get_gender(self):
        return self.gender
    
    def get_major(self):
        return self.major
    
    def get_yeargroup(self):
        return self.yeargroup

  

class Course:
    def __init__(self, course_code, course_name, name_of_instructor, name_of_fi):
        self.course_code = course_code
        self.course_name = course_name
        self.name_of_instructor = name_of_instructor
        self.name_of_fi = name_of_fi
        self.list_of_students = {}
    
    def __str__(self):
        return f'{self.course_code} is taught by {self.name_of_instructor} and assisted by {self.name_of_fi}. The number of students in the course are {len(self.list_of_students)}'

    def enrol_student(self, student):
        if student.get_student_id() not in self.list_of_students.keys():
            self.list_of_students[student.get_student_id] = student.get_name(), student.get_gender(), student.get_major(), student.get_yeargroup()
            return True
        else:
            return False
        
    def display_enrolled_students(self):
        print('Student ID', 'Name', 'Gender', 'Major', 'Year Group')
        print('-'*50)
        for stu in self.list_of_students.keys():
            print(f'{stu}, {self}')