def add_student(student_dict, name, marks):
    student_dict[name] = marks

def average_marks(student_dict):
    return sum(student_dict.values()) / len(student_dict)

def highest_scorer(student_dict):
    highest = max(student_dict, key=student_dict.get)
    return highest, student_dict[highest]

students = {}
while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    marks = int(input(f"Enter marks for {name}: "))
    add_student(students, name, marks)

for s, m in students.items():
    print(s, ":", m)

print("Average Marks:", average_marks(students))
top_student, top_marks = highest_scorer(students)
print("Top Scorer:", top_student, "with marks", top_marks)
