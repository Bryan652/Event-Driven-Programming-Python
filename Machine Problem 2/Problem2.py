"""
Student Grade Manager 
A Student class stores the student's name and grades 
A method calculates the average grade. 
A lamda function determines the grade category (A, B, C, etc)
F strings are used for formatting output
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"Student: {self.name} | Grade: {self.grade} | Category: {self.get_grade_category()}"
    
    def get_grade_category(self):
        category = lambda g: 'A' if g >= 90 else 'B' if g >= 80 else 'C' if g >= 70 else 'D'
        return category(self.grade)

class GradeManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, grade):
        self.students.append(Student(name, grade))
    
    def display_all_students(self):
        print("\nAll Students:")
        for student in self.students:
            print(student)
    
    def calculate_average(self):
        avg = lambda grades: sum(grades) / len(grades) if grades else 0
        grades = [student.grade for student in self.students]
        average = avg(grades)
        print(f"\nClass Average: {average:.2f}")
        return average

def main():
    manager = GradeManager()
    
    student_data = [
        ("Ericz", 99),
        ("Jitz", 90),
        ("RafaeloSanAnrezo", 70),
        ("RomuloMulo", 85),
        ("BitoyCruz", 88)
    ]
    
    for name, grade in student_data:
        manager.add_student(name, grade)
    
    while True:
        print("\nStudent Grade Manager")
        print("1 - Display All Students")
        print("2 - Calculate Class Average")
        print("3 - Add Student")
        print("4 - Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            manager.display_all_students()
        elif choice == '2':
            manager.calculate_average()
        elif choice == '3':
            name = input("Enter student name: ")
            while True:
                try:
                    grade = float(input("Enter student grade: "))
                    break
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            manager.add_student(name, grade)
            print(f"Added student: {name} with grade: {grade}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()