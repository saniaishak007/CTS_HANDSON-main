# HANDS-ON 4

## Task 2: Request Handling and JSON Responses

### 42. In the POST route, use `request.get_json()` and validate the required fields (`name`, `code`, `credits`).

Update the POST route.

```python
@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["name", "code", "credits"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    courses.append(data)

    return make_response_json(data, 201)
```



---

### 43. Add GET, PUT and DELETE routes using `<int:course_id>`.

Add the following routes.

```python
@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    ...

@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    ...

@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    ...
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 224812" src="https://github.com/user-attachments/assets/ab8c4275-3c4f-437b-8306-33fe7e352f1c" />
<img width="1920" height="1080" alt="Screenshot 2026-07-01 224842" src="https://github.com/user-attachments/assets/fa7ae931-98d9-49d2-9a3c-788454b5cce8" />
<img width="1920" height="1080" alt="Screenshot 2026-07-01 224906" src="https://github.com/user-attachments/assets/7f3683af-e0d2-4329-956e-18d9ba4ee8a0" />


---

### 44. Create a helper function `make_response_json()`.

```python
def make_response_json(data, status_code):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code
```

Use this helper function in all successful responses.



---

### 45. Add Flask error handlers for `404` and `500`.

Add the following inside `create_app()`.

```python
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
```



---

### 46. Test all endpoints using Thunder Client.

#### GET

```
GET
http://127.0.0.1:5000/api/courses/
```

Expected Status

```
200 OK
```

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

---

#### POST (Missing Field)

```json
{
    "name":"Python"
}
```

Expected Status

```
400 Bad Request
```

---

#### GET by ID

```
GET
http://127.0.0.1:5000/api/courses/0
```

Expected Status

```
200 OK
```

---

#### PUT

```
PUT
http://127.0.0.1:5000/api/courses/0
```

Body

```json
{
    "name":"Advanced Python",
    "code":"CS101",
    "credits":5
}
```

Expected Status

```
200 OK
```

---

#### DELETE

```
DELETE
http://127.0.0.1:5000/api/courses/0
```

Expected Status

```
200 OK
```

---

#### Unknown ID

```
GET
http://127.0.0.1:5000/api/courses/100
```

Expected Status

```
404 Not Found
```
<img width="1920" height="1080" alt="Screenshot 2026-07-01 224930" src="https://github.com/user-attachments/assets/8c740cc1-50a9-47dc-84c6-5f16a5d35fe2" />


---

