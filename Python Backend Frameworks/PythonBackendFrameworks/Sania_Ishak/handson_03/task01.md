# HANDS-ON 3

## Task 1: Serializers and Basic API Views

### 26. In `courses/serializers.py`, create a `ModelSerializer` for each model: `DepartmentSerializer`, `CourseSerializer`, `StudentSerializer`, `EnrollmentSerializer`. Include all fields.

Create `courses/serializers.py`.

```python
from rest_framework import serializers
from .models import Department, Course, Student, Enrollment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 142214" src="https://github.com/user-attachments/assets/23e801a0-2d77-4fba-94cb-280cbc781907" />


---

### 27. In `courses/views.py`, create a `CourseListView` using DRF's `APIView`: handle GET and POST.

Replace `views.py` with:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer


class CourseListView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
```
<img width="1062" height="463" alt="Screenshot 2026-07-01 203638" src="https://github.com/user-attachments/assets/16ae06ce-a365-43c9-b236-29c682810bf1" />


---

### 28. Create a `CourseDetailView` for GET, PUT and DELETE operations.

Add the following below `CourseListView`.

```python
class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

<img width="1072" height="793" alt="Screenshot 2026-07-01 203832" src="https://github.com/user-attachments/assets/236a859c-987c-4599-8ef8-172afcaa79c4" />


---

### 29. Wire both views in `courses/urls.py`. Include `courses/urls.py` in the main `urls.py`.

**courses/urls.py**

```python
from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
```

**coursemanager/urls.py**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
]
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1581c828-f24b-481e-aae0-795e588d5aaa" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a47c16a2-8791-424e-881b-0082c392a8c0" />


---

### 30. Test all endpoints using Thunder Client or Postman.

#### GET

```
GET
http://127.0.0.1:8000/api/courses/
```

Expected Status:

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 145846" src="https://github.com/user-attachments/assets/7ba957b5-94b9-4fed-8618-69597ead4ae4" />

---

#### POST

```
POST
http://127.0.0.1:8000/api/courses/
```

Body (JSON)

```json
{
    "name":"Data Science",
    "code":"CS201",
    "credits":3,
    "department":1
}
```

Expected Status:

```
201 Created
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 201410" src="https://github.com/user-attachments/assets/e34fb76a-d41e-41b5-9738-1ff3ccde7152" />

---

#### GET by ID

```
GET
http://127.0.0.1:8000/api/courses/9/
```

Expected Status:

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 201447" src="https://github.com/user-attachments/assets/320132d1-e731-4079-9a33-19c59e25ca0b" />

---

#### PUT

```
PUT
http://127.0.0.1:8000/api/courses/9/
```

Body

```json
{
    "name":"Advanced Data Science",
    "code":"CS201",
    "credits":4,
    "department":1
}
```

Expected Status:

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 201524" src="https://github.com/user-attachments/assets/91a8c5f8-9e92-44c8-a802-c6b26610bd06" />

---

#### DELETE

```
DELETE
http://127.0.0.1:8000/api/courses/9/
```

Expected Status:

```
204 No Content
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 201831" src="https://github.com/user-attachments/assets/25b42289-eaa3-4bfe-a980-19e994abc845" />

---


