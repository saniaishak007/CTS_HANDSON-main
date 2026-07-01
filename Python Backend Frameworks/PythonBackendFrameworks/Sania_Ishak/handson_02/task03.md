"""
Hands-On 2 - Task 3 Django Admin Interface

Before running:
1. Create a superuser:
   python manage.py createsuperuser

   Username : admin
   Email    : admin@college.edu
   Password : Admin@123

2. Start the development server:
   python manage.py runserver

3. Open the Django Admin:
   http://127.0.0.1:8000/admin/

4. Login using the superuser credentials.

5. Through the Admin interface:
   - Create 3 Courses
   - Create 5 Students
   - Create 4 Enrollments
   - Try creating the same Student-Course enrollment twice to verify
     the unique_together constraint.

Admin Configuration (courses/admin.py)
--------------------------------------
"""

from django.contrib import admin
from .models import Department, Course, Student, Enrollment

```
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "credits", "department"]
    search_fields = ["name", "code"]
    list_filter = ["department"]


admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)


print("=" * 60)
print("Hands-On 2 - Task 3")
print("=" * 60)

print("\n✓ Superuser should be created using:")
print("  Username : admin")
print("  Email    : admin@college.edu")
print("  Password : Admin@123")

print("\n✓ Registered Models:")
print("  - Department")
print("  - Course")
print("  - Student")
print("  - Enrollment")

print("\n✓ CourseAdmin Customization:")
print("  list_display = ['name', 'code', 'credits', 'department']")
print("  search_fields = ['name', 'code']")
print("  list_filter = ['department']")

print("\n✓ Start the server:")
print("  python manage.py runserver")

print("\n✓ Open:")
print("  http://127.0.0.1:8000/admin/")

print("\n✓ Login with the superuser credentials.")

print("\n✓ Using the Admin interface:")
print("  • Create 3 Courses")
print("  • Create 5 Students")
print("  • Create 4 Enrollments")

print("\n✓ Validation Test:")
print("  Try enrolling the same student in the same course twice.")
print("  Expected Result:")
print("  'Enrollment with this Student and Course already exists.'")

print("\nHands-On 2 Task 3 Completed Successfully.")
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 133757" src="https://github.com/user-attachments/assets/34ee4ccb-006e-4501-a432-b0e63ec0f71c" />
<img width="1920" height="1080" alt="Screenshot 2026-07-01 133831" src="https://github.com/user-attachments/assets/48a39353-9edd-4d59-9ed6-f6d6d52069a3" />
<img width="1920" height="1080" alt="Screenshot 2026-07-01 133912" src="https://github.com/user-attachments/assets/4c9bda8a-44ef-48cd-b46d-eeb4c2bc0d6d" />
<img width="1920" height="1080" alt="Screenshot 2026-07-01 134100" src="https://github.com/user-attachments/assets/02de4fe2-b322-4240-b6ad-c9085ecec0cd" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9476a45e-a894-4a9b-b9c2-2e6ed0184dd0" />




