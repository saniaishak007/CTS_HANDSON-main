# HANDS-ON 4

## Task 1: Flask App Structure and Basic Routing

### 36. Create a project folder `flask_coursemanager/`. Inside, create `app.py`, `config.py`, and a `courses/` package with `__init__.py` and `routes.py`.

Create the following project structure.

```text
flask_coursemanager/
│
├── app.py
├── config.py
├── requirements.txt
└── courses/
    ├── __init__.py
    └── routes.py
```

<img width="318" height="277" alt="Screenshot 2026-07-01 223645" src="https://github.com/user-attachments/assets/dc963e90-c1df-4ae1-b59f-b0e19fc3e22e" />


---

### 37. In `app.py`, create the Flask app using the application factory pattern.

Create `app.py`.

```python
from flask import Flask, jsonify
from config import Config
from courses.routes import courses_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "status": "error",
            "message": "Resource not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```
<img width="1157" height="545" alt="Screenshot 2026-07-01 223707" src="https://github.com/user-attachments/assets/40182111-eb5c-40fc-bfb7-54716fd087e2" />


---

### 38. In `config.py`, define a `Config` class.

Create `config.py`.

```python
class Config:
    SECRET_KEY = "coursemanager"
    SQLALCHEMY_DATABASE_URI = "sqlite:///courses.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
```
<img width="1042" height="477" alt="Screenshot 2026-07-01 223723" src="https://github.com/user-attachments/assets/864e98ae-2f79-45a3-9afb-1eb0d04c62fc" />


---

### 39. In `courses/routes.py`, define a Blueprint and add GET and POST routes.

Create `courses/routes.py`.

```python
from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = []


@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)


@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    courses.append(data)

    return jsonify(data), 201
```

<img width="977" height="531" alt="Screenshot 2026-07-01 223748" src="https://github.com/user-attachments/assets/40f83ed3-99a3-47e6-9fc2-4660c814763f" />


---

### 40. Register the Blueprint in `create_app()`.

Register the blueprint.

```python
app.register_blueprint(courses_bp)
```

<img width="1037" height="348" alt="Screenshot 2026-07-01 223814" src="https://github.com/user-attachments/assets/f85d9511-b685-478b-a803-28105899b374" />

---

### 41. Run the application and test GET `/api/courses/`.

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000/api/courses/
```

Expected Response

```json
[]
```

Expected Status

```
200 OK
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 223825" src="https://github.com/user-attachments/assets/85c4211c-a674-45ed-9102-24e593eae8e3" />

---

#### POST

```
POST
http://127.0.0.1:5000/api/courses/
```

Body

```json
{
    "name":"Python",
    "code":"CS101",
    "credits":4
}
```

Expected Status

```
201 Created
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 224729" src="https://github.com/user-attachments/assets/e5998041-f460-425d-a63c-290cf888a1e2" />


---

