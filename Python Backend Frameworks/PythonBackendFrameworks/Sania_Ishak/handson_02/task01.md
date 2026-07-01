## Hands-On 2 – Task 1: Define Models and Run Migrations
# courses/models.py

```
from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    enrollment_year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    enrollment_date = models.DateField()
    grade = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = [['student', 'course']]

    def __str__(self):
        return f"{self.student} - {self.course}"
```


## OUTPUT :
11.<img width="1920" height="1080" alt="Screenshot 2026-07-01 110801" src="https://github.com/user-attachments/assets/25621e61-1216-4836-a5e1-267e858a4949" />
12.<img width="1920" height="1080" alt="Screenshot 2026-07-01 110833" src="https://github.com/user-attachments/assets/628522d7-448b-454a-9fff-785f2fcd6313" />
13.<img width="1211" height="643" alt="Screenshot 2026-07-01 110910" src="https://github.com/user-attachments/assets/3a012aa8-03e6-4883-b5d2-4b4f16fc5fb6" />
14.<img width="1182" height="177" alt="Screenshot 2026-07-01 113529" src="https://github.com/user-attachments/assets/198f5bec-5b3f-4c8d-8253-c4154b443131" />




