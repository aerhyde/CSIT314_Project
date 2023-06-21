class Student:
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

students = []

students.append(Student("John Doe", "Math", 90))
students.append(Student("Jane Smith", "Science", 85))
students.append(Student("Tom Johnson", "English", 95))
students.append(Student("Max William", "Chemistry", 85))
students.append(Student("Islam Khaled", "Arabic", 90))
students.append(Student("Emma Alex", "Biology", 97))

search_name = input("Enter the student's name for those who ONLY subscribed: ")

found = False
for student in students:
    if student.name == search_name:
        found = True
        print("Student Name:", student.name)
        print("Subject:", student.subject)
        print("Grade:", student.grade)
        break

if not found:
    print("Student not found.")
    print("Subscribe so that you can see your child's work.")


