# ===========================================================
# Task 1 - Django Framework Fundamentals
# ===========================================================

# 1. Request-Response Cycle
#
# Browser sends GET request to /api/courses/
#        |
#        V
# URL Router (urls.py)
#        |
#        V
# View (views.py)
#        |
#        V
# Model (models.py) performs database query
#        |
#        V
# Data returned from database
#        |
#        V
# View prepares response
#        |
#        V
# HttpResponse returned to browser


# -----------------------------------------------------------
# 2. Middleware
# -----------------------------------------------------------

# Middleware is software that processes requests before they
# reach the view and processes responses before they are sent
# back to the browser.

# Example 1:
# SecurityMiddleware
# Adds security headers and protects against attacks.

# Example 2:
# SessionMiddleware
# Enables user session management.


# -----------------------------------------------------------
# 3. WSGI vs ASGI
# -----------------------------------------------------------

# WSGI (Web Server Gateway Interface)
# Supports synchronous applications.

# ASGI (Asynchronous Server Gateway Interface)
# Supports asynchronous programming, WebSockets and long-lived
# connections.

# Django uses WSGI by default.

# Use ASGI when building:
# - Chat applications
# - Live notifications
# - Real-time dashboards
# - WebSocket applications


# -----------------------------------------------------------
# 4. MVC vs Django MVT
# -----------------------------------------------------------

# MVC
# Model -> Database
# View -> User Interface
# Controller -> Business Logic

# Django MVT
# Model -> Model
# View -> Controller
# Template -> View

# Django's View performs the work of the Controller in MVC.
# Django's Template corresponds to the View in MVC.


# -----------------------------------------------------------
# 5. Django Project Files
# -----------------------------------------------------------

# settings.py
# Stores project configuration and installed applications.

# urls.py
# Maps URLs to views.

# wsgi.py
# Entry point for WSGI-compatible web servers.

# asgi.py
# Entry point for ASGI-compatible web servers.