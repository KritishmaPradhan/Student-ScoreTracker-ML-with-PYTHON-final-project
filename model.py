from student import *
class StudentController:
    def __init__(self):
        self.students = []
    def add_student(self, students):
        self.students.append(students)
    def show_student(self, name):
        for s in self.students:
            if s == name:
                print("Student found", s)

if __name__ == "__main__":
    # name = input("Enter you name :")                             # by taking user input for class object
    # id = input("Enter your id: ") 
    sub_marks = {}
    # for individual_mks in range(3):
    #     marks = int(input("Enter your marks : "))
    #     sub_marks[individual_mks] = marks
    # print(sub_marks)
    Stu1 = Student('kriti', 23, {1: 20, 2: 30, 3: 40})             # by directly assigning values to class object
    Stu2 = Student('rachel', 20, {1: 40, 2: 20, 3: 80})
    Stu3 = Student('ben', 27, {1: 50, 2: 30, 3: 20})
    print(Stu1)
    print(Stu2)
    print(Stu3)
    Stu1.calculate_avg_marks()
    SC = StudentController()
    SC.add_student(Stu1.name)
    SC.add_student(Stu2.name)
    SC.add_student(Stu3.name)
    print(SC.students)
    SC.show_student('rachel')

    Stu1.calculate_percentage()
    

    # ................. PRACTICE CODE ...............