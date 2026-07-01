# HANDS-ON 3

## Task 2: ViewSets and Routers

### 31. Replace `CourseListView` and `CourseDetailView` with a single `CourseViewSet` that extends `viewsets.ModelViewSet`.

Replace the contents of `courses/views.py` with the following.

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        course = self.get_object()
        enrollments = Enrollment.objects.filter(course=course)
        students = [enrollment.student for enrollment in enrollments]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
```

<img width="1920" height="1080" alt="Screenshot 2026-07-01 204605" src="https://github.com/user-attachments/assets/55d81219-db6f-4f89-a7a0-02cd12ebb103" />


---

### 32. Create a `DefaultRouter` in `courses/urls.py` and register the viewset.

Replace `courses/urls.py` with:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, StudentViewSet, EnrollmentViewSet

router = DefaultRouter()

router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 204634" src="https://github.com/user-attachments/assets/d1ef523a-6faf-403b-8ca6-751799e3b78a" />


---

### 33. Register `StudentViewSet` and `EnrollmentViewSet`.

The following ViewSets are registered using `DefaultRouter`.

```python
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 204634" src="https://github.com/user-attachments/assets/11fdb0d6-3583-4beb-ab2d-8570db1dbb89" />


---

### 34. Add a custom action to `CourseViewSet` using the `@action` decorator.

The following custom action returns all students enrolled in a particular course.

```python
@action(detail=True, methods=['get'])
def students(self, request, pk=None):
    course = self.get_object()
    enrollments = Enrollment.objects.filter(course=course)
    students = [enrollment.student for enrollment in enrollments]
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
```

API Endpoint

```
GET
http://127.0.0.1:8000/api/courses/<id>/students/
```


---

### 35. Test the custom action endpoint using Thunder Client or Postman.

#### GET All Courses

```
GET
http://127.0.0.1:8000/api/courses/
```

Expected Status:

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 204816" src="https://github.com/user-attachments/assets/8e76d26e-a728-444c-9321-9dfaf54cdb90" />

---

#### GET All Students

```
GET
http://127.0.0.1:8000/api/students/
```

Expected Status:

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 204844" src="https://github.com/user-attachments/assets/98412fac-5592-4d0f-93dc-68434844794c" />

---

#### GET All Enrollments

```
GET
http://127.0.0.1:8000/api/enrollments/
```

Expected Status:

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 204910" src="https://github.com/user-attachments/assets/c5d1b9b5-2d03-44e2-b9a2-6eb4619f17ac" />

---

#### GET Students Enrolled in a Course

```
GET
http://127.0.0.1:8000/api/courses/2/students/
```

> Replace **2** with any existing Course ID.

Expected Status:

```
200 OK
```

If no students are enrolled in the selected course, the response will be:

```json
[]
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 205021" src="https://github.com/user-attachments/assets/5ce0372d-5a79-43a1-84ca-a50217bb25c2" />


---

