from flask import Blueprint, request, jsonify
from courses.models import Course, db

courses_bp = Blueprint("courses_bp", __name__)

# GET all courses
@courses_bp.route("/api/courses/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses])


# POST course
@courses_bp.route("/api/courses/", methods=["POST"])
def create_course():
    data = request.json

    course = Course(
        title=data["title"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201