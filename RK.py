class Student:
    def __init__(self, student_id, last_name, grade, group_id):
        self.student_id = student_id
        self.last_name = last_name
        self.grade = grade
        self.group_id = group_id

class StudentGroup:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

students = [
    Student(1, "Иванов", 85, 101),
    Student(2, "Петров", 90, 101),
    Student(3, "Сидоров", 78, 102),
    Student(4, "Смирнов", 88, 102),
    Student(5, "Козлов", 92, 103),
]

groups = [
    StudentGroup(101, "Группа А"),
    StudentGroup(102, "Группа Б"),
    StudentGroup(103, "Группа В"),
]

courses = [
    Course(201, "Математика"),
    Course(202, "Информатика"),
    Course(203, "Физика"),
]

enrollments = [
    Enrollment(1, 201),
    Enrollment(1, 202),
    Enrollment(2, 202),
    Enrollment(3, 203),
    Enrollment(4, 201),
    Enrollment(5, 203),
]

groups_with_a_students = [
    (group.group_name, [student.last_name for student in students if student.group_id == group.group_id])
    for group in groups if group.group_name.startswith("Группа А")
]

groups_max_grade = sorted(
    [(group.group_name, max(student.grade for student in students if student.group_id == group.group_id))
     for group in groups],
    key=lambda x: x[1], reverse=True
)

sorted_enrollments = sorted(
    [(next(student.last_name for student in students if student.student_id == enrollment.student_id),
      next(course.course_name for course in courses if course.course_id == enrollment.course_id))
     for enrollment in enrollments],
    key=lambda x: x[1]
)

print("Группы на 'А' и их студенты:", groups_with_a_students)
print("Группы с максимальной оценкой студентов:", groups_max_grade)
print("Связанные студенты и курсы:", sorted_enrollments)
