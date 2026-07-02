# HANDS-ON 6

## Task 2: Path/Query Parameters and Async Database Access

### 62. Add GET `/api/courses/{course_id}` Endpoint.

Open `main.py`.

Add the following endpoint.

```python
@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):
    return {
        "course_id": course_id,
        "message": "Course fetched successfully"
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

Test

```
GET
/api/courses/1
```

Expected Output

```json
{
    "course_id": 1,
    "message": "Course fetched successfully"
}
```

Test invalid input.

```
GET
/api/courses/abc
```

Expected Status

```
422 Unprocessable Entity
```

<img width="1920" height="1080" alt="Screenshot 2026-07-02 090234" src="https://github.com/user-attachments/assets/f4701fd2-db72-4184-8404-0b659066a9bc" />
<img width="1920" height="1080" alt="Screenshot 2026-07-02 090444" src="https://github.com/user-attachments/assets/560cfb94-3322-4303-be54-349caf556d9e" />

---

### 63. Add Query Parameters.

Update `main.py`.

```python
from typing import Optional

@app.get("/api/courses/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None
):
    return {
        "skip": skip,
        "limit": limit,
        "department_id": department_id
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

Test 1

```
GET
/api/courses/?skip=0&limit=2
```

Expected Output

```json
{
    "skip": 0,
    "limit": 2,
    "department_id": null
}
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8202f596-ee3b-4e7a-9730-cc1337dc6cd0" />

Test 2

```
GET
/api/courses/?skip=2&limit=2
```

Expected Output

```json
{
    "skip": 2,
    "limit": 2,
    "department_id": null
}
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/848c447a-4aab-4a7b-bc3f-8d8e9911fcfa" />

Test 3

```
GET
/api/courses/?department_id=1
```

Expected Output

```json
{
    "skip": 0,
    "limit": 10,
    "department_id": 1
}
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c024f74c-413a-4357-b769-aa4e52126c95" />


---

### 64. Configure Async SQLAlchemy.

Install the async SQLite driver.

```bash
pip install aiosqlite
```

Create `database.py`.

```python
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///course.db"

engine = create_async_engine(DATABASE_URL)
```

Run the application.

```bash
uvicorn main:app --reload --port 8001
```

Expected Outcome

- Async SQLAlchemy engine created successfully.


---

### 65. Create `get_db()` Dependency.

Update `database.py`.

```python
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db():
    async with AsyncSession(engine) as session:
        yield session
```

Import dependency.

```python
from fastapi import Depends
```

Run the application.

```bash
uvicorn main:app --reload --port 8001
```

Expected Outcome

- Database dependency created successfully.


---

### 66. Implement Async CRUD Operations.

Use asynchronous SQLAlchemy methods.

```python
await db.execute(select(Course))
await db.commit()
```

Example dependency injection.

```python
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

@app.get("/api/courses/")
async def get_courses(db: AsyncSession = Depends(get_db)):
    pass
```

Run the application.

```bash
uvicorn main:app --reload --port 8001
```

Test all CRUD endpoints using Swagger.

Expected Status

```
200 OK
```


---

### 67. Test Pagination and Filtering.

Open Swagger.

```
http://127.0.0.1:8001/docs
```

Test

```
GET
/api/courses/?skip=0&limit=2
```

Expected Output

```json
[
    {
        "id": 1
    },
    {
        "id": 2
    }
]
```

Test

```
GET
/api/courses/?skip=2&limit=2
```

Expected Output

```json
[
    {
        "id": 3
    },
    {
        "id": 4
    }
]
```

Test

```
GET
/api/courses/?department_id=1
```

Expected Status

```
200 OK
```

Expected Outcome

- Pagination works successfully.
- Filtering by `department_id` works successfully.
- Async endpoints return the expected data.


---

