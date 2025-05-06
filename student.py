class Student:
    def __init__(self, name, id, sub_marks):
        self.name = name
        self.id = id
        self.sub_marks = sub_marks
    def __str__(self):
        return f"Name {self.name} \n Id {self.id} \n marks{self.sub_marks}"
    
    def calculate_avg_marks(self):
        global length_marks, total_mks
        length_marks = len(self.sub_marks)
        total_mks = 0
        for i in self.sub_marks.values():
            total_mks += i
        average_mks = total_mks/length_marks
        print("The averge marks in all subjects is : ", average_mks)

    def calculate_percentage(self):
        grand_total = length_marks * 100
        percentage = total_mks *100 / grand_total
        print(f'{percentage} %')

# ................. PRACTICE CODE ...............