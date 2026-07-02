# HANDS-ON 6

## Task 1: FastAPI Setup and Pydantic Schemas

### 57. Create a FastAPI Project.

Create the project folder.

```bash
mkdir handson_06
cd handson_06
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

```bash
venv\Scripts\activate
```

Install the required packages.

```bash
pip install fastapi uvicorn sqlalchemy aiosqlite
```

Verify the installation.

```bash
pip list
```

Save the dependencies.

```bash
pip freeze > requirements.txt
```

Create the following files.

```text
handson_06/
│
├── main.py
├── schemas.py
├── database.py
├── requirements.txt
└── venv/
```

Create `main.py`.

```python
from fastapi import FastAPI

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

@app.get("/")
async def root():
    return {"message": "API running"}
```

Run the application.

```bash
uvicorn main:app --reload
```

If port 8000 is busy.

```bash
uvicorn main:app --reload --port 8001
```

Open

```
http://127.0.0.1:8001/
```

Expected Output

```json
{
    "message": "API running"
}
```

<img width="315" height="457" alt="Screenshot 2026-07-02 084714" src="https://github.com/user-attachments/assets/d2d92e05-841d-4dcc-84ed-689547a100d1" />
<img width="1050" height="300" alt="Screenshot 2026-07-02 084846" src="https://github.com/user-attachments/assets/851d67a2-9eb5-441f-a8e8-a23c21f101c2" />


---

### 58. Create Pydantic Schemas.

Open `schemas.py`.

```python
from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: list[CourseResponse] = []
```

Run the application.

```bash
uvicorn main:app --reload --port 8001
```

<img width="1920" height="1080" alt="Screenshot 2026-07-02 085258" src="https://github.com/user-attachments/assets/381c3f84-a66a-46bc-8e35-03e0e8ca55a1" />

---

### 59. Define Nested Pydantic Models.

Verify that `DepartmentResponse` contains a list of `CourseResponse`.

```python
class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: list[CourseResponse] = []
```

Run the application.

```bash
uvicorn main:app --reload --port 8001
```

Expected Outcome

- Nested Pydantic model created successfully.


---

### 60. Add POST `/api/courses/`.

Update `main.py`.

```python
from fastapi import FastAPI
from schemas import CourseCreate

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post("/api/courses/")
async def create_course(course: CourseCreate):
    return {
        "message": "Course Created Successfully",
        "course": course
    }
```

Run the application.

```bash
uvicorn main:app --reload --port 8001
```

Open Swagger.

```
http://127.0.0.1:8001/docs
```

Click **POST /api/courses/** → **Try it out**

Enter

```json
{
    "name": "Python",
    "code": "CS101",
    "credits": 4,
    "department_id": 1
}
```

Click **Execute**.

Expected Output

```json
{
    "message": "Course Created Successfully",
    "course": {
        "name": "Python",
        "code": "CS101",
        "credits": 4,
        "department_id": 1
    }
}
```

Test invalid input.

```json
{
    "name": "Python"
}
```

Expected Status

```
422 Unprocessable Entity
```

<img width="1920" height="1080" alt="Screenshot 2026-07-02 085403" src="https://github.com/user-attachments/assets/ff5c6baa-765d-4946-b706-031bbc99b7d4" />
<img width="1920" height="1080" alt="Screenshot 2026-07-02 085509" src="https://github.com/user-attachments/assets/369397d9-cdb0-4eac-8b7b-d0c6e84d2409" />
<img width="1920" height="1080" alt="Screenshot 2026-07-02 085525" src="https://github.com/user-attachments/assets/32200b0f-518b-458c-881c-7b395278b12d" />
<img width="1920" height="1080" alt="Screenshot 2026-07-02 085633" src="https://github.com/user-attachments/assets/2df5ca04-25bb-40f1-99b8-924427df4a19" />

<img width="1920" height="1080" alt="Screenshot 2026-07-02 085654" src="https://github.com/user-attachments/assets/84a4915e-c5dd-4537-be71-2b91170aea76" />

---

### 61. View Swagger UI and ReDoc.

Open Swagger UI.

```
http://127.0.0.1:8001/docs
```

Verify the following.

- GET /
- POST /api/courses/
- CourseCreate Request Schema
- Response Schema

Open ReDoc.

```
http://127.0.0.1:8001/redoc
```

Expected Outcome

- Swagger UI generated automatically.
- ReDoc documentation available.
- Request and response schemas displayed.

<img width="1920" height="1080" alt="Screenshot 2026-07-02 090052" src="https://github.com/user-attachments/assets/e9078f10-4bcc-46fc-99d1-a8469acc2c25" />
