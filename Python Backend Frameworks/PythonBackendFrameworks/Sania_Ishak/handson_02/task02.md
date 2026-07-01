"""
Hands-On 2 - Task 2 Django ORM Queries

Run inside shell:
python manage.py shell
exec(open("handson2_task2.py").read())
"""

# -----------------------------
# Imports
# -----------------------------
from courses.models import Department, Course, Student, Enrollment
from django.db.models import Count, F
from datetime import date

# -----------------------------
# Create Departments
# -----------------------------
cs = Department.objects.create(
    name="Computer Science",
    head_of_dept="Dr. Ravi",
    budget=500000
)

it = Department.objects.create(
    name="Information Technology",
    head_of_dept="Dr. Priya",
    budget=400000
)

# -----------------------------
# Create Courses
# -----------------------------
c1 = Course.objects.create(
    name="Python Programming",
    code="CS101",
    credits=4,
    department=cs
)

c2 = Course.objects.create(
    name="Data Structures",
    code="CS102",
    credits=4,
    department=cs
)

c3 = Course.objects.create(
    name="Web Development",
    code="IT101",
    credits=3,
    department=it
)

c4 = Course.objects.create(
    name="Cloud Computing",
    code="IT102",
    credits=4,
    department=it
)

# -----------------------------
# Create Students
# -----------------------------
s1 = Student.objects.create(
    first_name="Rahul",
    last_name="Sharma",
    email="rahul@example.com",
    department=cs,
    enrollment_year=2024
)

s2 = Student.objects.create(
    first_name="Anjali",
    last_name="Singh",
    email="anjali@example.com",
    department=cs,
    enrollment_year=2024
)

s3 = Student.objects.create(
    first_name="Arun",
    last_name="Kumar",
    email="arun@example.com",
    department=it,
    enrollment_year=2023
)

s4 = Student.objects.create(
    first_name="Priya",
    last_name="Ravi",
    email="priya@example.com",
    department=it,
    enrollment_year=2024
)

s5 = Student.objects.create(
    first_name="Karthik",
    last_name="Raj",
    email="karthik@example.com",
    department=it,
    enrollment_year=2025
)

print("\nDepartments, Courses and Students created successfully.\n")

# -----------------------------
# Create Enrollments
# -----------------------------
Enrollment.objects.create(student=s1, course=c1, enrollment_date=date.today(), grade="A")
Enrollment.objects.create(student=s1, course=c2, enrollment_date=date.today(), grade="B")
Enrollment.objects.create(student=s2, course=c1, enrollment_date=date.today(), grade="A")
Enrollment.objects.create(student=s3, course=c3, enrollment_date=date.today(), grade="B")
Enrollment.objects.create(student=s4, course=c4, enrollment_date=date.today(), grade="A")

print("Enrollments created successfully.\n")

# -----------------------------
# Query Courses (ForeignKey lookup)
# -----------------------------
print("Courses in Computer Science:")

courses = Course.objects.filter(department__name="Computer Science")

for course in courses:
    print("-", course.name)

# -----------------------------
# Count Courses per Department
# -----------------------------
print("\nCourse Count by Department:")

counts = Department.objects.annotate(course_count=Count("course"))

for dept in counts:
    print(dept.name, "-", dept.course_count)

# -----------------------------
# select_related() optimization
# -----------------------------
print("\nStudents with Departments:")

students = Student.objects.select_related("department")

for student in students:
    print(student.first_name, "-", student.department.name)

# -----------------------------
# Update Budget (F expression)
# -----------------------------
Department.objects.update(
    budget=F("budget") * 1.10
)

print("\nDepartment budgets increased by 10%.")

print("\nHands-On 2 Task 2 Completed Successfully.")

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2a62e348-d293-4305-a728-c632c8ee0b74" />
