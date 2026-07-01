# Task 1: Understand the Request-Response Cycle

## 1. Request-Response Cycle

### Flow

```
Browser
   │
   ▼
URL Router (urls.py)
   │
   ▼
View (views.py)
   │
   ▼
Model (models.py)
   │
   ▼
Database
   │
   ▼
Model
   │
   ▼
View
   │
   ▼
HttpResponse
   │
   ▼
Browser
```

### Description

When a user sends a **GET /api/courses/** request, Django first receives the request through the URL Router (`urls.py`). The URL router matches the URL with the appropriate view function.

The **View (`views.py`)** processes the request and contains the application logic. If data is required, it communicates with the **Model (`models.py`)**.

The **Model** interacts with the database, performs the required query, and returns the data to the View.

The **View** prepares an **HttpResponse** (or renders a template) and sends the response back to the browser.

---

# 2. Middleware

Middleware is software that processes every HTTP request before it reaches the View and processes every HTTP response before it is sent back to the browser.

It acts as a bridge between the browser and the Django application.

### Two Built-in Middleware Classes

### SecurityMiddleware
- Adds security-related HTTP headers.
- Protects the application against common security attacks.

### SessionMiddleware
- Enables session management.
- Stores and retrieves user session information.

---

# 3. WSGI vs ASGI

## WSGI (Web Server Gateway Interface)

- Supports synchronous applications.
- Handles one request at a time.
- Suitable for traditional web applications.

## ASGI (Asynchronous Server Gateway Interface)

- Supports asynchronous programming.
- Can handle multiple requests simultaneously.
- Supports WebSockets, chat applications, live notifications, and real-time dashboards.

### Which one does Django use?

Django uses **WSGI by default**.

### When should ASGI be used?

Use ASGI when building:

- Chat applications
- WebSocket applications
- Live notifications
- Real-time dashboards
- Other asynchronous applications

---

# 4. MVC Pattern and Django MVT

## MVC Pattern

### Model
- Handles data and database operations.

### View
- Displays information to the user.

### Controller
- Handles user requests and application logic.

---

## Django MVT Pattern

### Model
- Manages database operations.

### View
- Contains the application logic.
- Performs the role of the Controller in MVC.

### Template
- Displays data to the user.
- Performs the role of the View in MVC.

---

## MVC to Django MVT Mapping

| MVC | Django MVT |
|------|------------|
| Model | Model |
| View | Template |
| Controller | View |

---

# Summary

- The request first reaches the URL Router.
- The View processes the request.
- The Model communicates with the database.
- Middleware processes requests before and responses after the View.
- Django uses WSGI by default and ASGI for asynchronous applications.
- Django follows the MVT architecture, where the Django View acts like the MVC Controller.
