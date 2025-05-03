import csv
import os
def main_menu():
    print("\n Student Score Tracker  ")
    print(" 1. Add Student ")
    print(" 2. View all Students ")
    print(" 3. Search student ")
    print(" 4. Save to file ")
    print(" 5. Load from File ")
    print(" 6. Exit ")
    menu_choice = input(" Enter your choice: ")
    if menu_choice == '1':
        add_student()
    elif menu_choice == '2':
        view_student()
    elif menu_choice == '3':
        search_student()
    else:
        print('INVALID CHOICE. Try again')

def add_student():
    global sub_marks
    choice = 'y'
    data = []
    while choice == 'y':
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        sub_marks = {}
        for individual_mks in range(3):
            marks = int(input("Enter your marks : "))   
            sub_marks[individual_mks] = marks
        data.append({"id": id, "name": name, "marks": sub_marks,
                      "avg_mks" :calculate_avg_marks(sub_marks), "percentage":calculate_percentage(sub_marks) })       
        choice = input("Do you want to continue:\n y for yes or n for no: ")

    file_exists = os.path.isfile('StudentDetails.csv')

    with open('StudentDetails.csv', mode='a', newline='') as file:
        fieldnames = ['id', 'name', 'marks', 'avg_mks', 'percentage']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists or os.stat('StudentDetails.csv').st_size == 0:
            writer.writeheader()
        writer.writerows(data)

def view_student():
    with open('StudentDetails.csv', mode='r', newline='') as f:
        display_student = f.readlines()  
        for student_list in display_student:                      
            print(student_list)

def search_student():
    with open('StudentDetails.csv', mode='r', newline='') as f:
        search_student = csv.DictReader(f)
        # for specific_student in search_student:
        #     print(specific_student['name']) 
        student_id_search = input("Enter the student id you want to search: ")
        for specific_student in search_student:
            if specific_student['id'] == student_id_search:
                print(f'The details of student with id {specific_student['id']} : \n {specific_student}')

def calculate_avg_marks(sub_marks):
    total_mks = sum(sub_marks.values())
    average_mks = total_mks / len(sub_marks)
    return average_mks

def calculate_percentage(sub_marks):
    total_mks = sum(sub_marks.values())
    grand_total = len(sub_marks) * 100 
    percentage = (total_mks * 100) / grand_total
    return f'{percentage:.2f} %'

while True:   
    if __name__ == '__main__':
        main_menu()    


