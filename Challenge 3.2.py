def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Sample list of student objects
students = [
    Student("Dinesh", "A001", 6.9),
    Student("Ganesh", "B002", 10.0),
    Student("Abdul", "C003", 3.5),
  
]

# Sort the students by CGPA in descending order
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f" Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

