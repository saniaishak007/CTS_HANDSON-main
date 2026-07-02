from fastapi import FastAPI
from typing import Optional
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


@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):
    return {
        "course_id": course_id,
        "message": "Course fetched successfully"
    }


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
