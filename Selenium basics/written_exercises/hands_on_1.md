# Hands-On 1: Software Testing Concepts & QA Methodologies

---

## Task 1: Map Testing Types to a Real System

### Part 1: Testing Levels in the Course Management API
To ensure comprehensive quality assurance for the Course Management API, testing is structured across four distinct levels of the software testing hierarchy:

*   **Unit Testing:** 
    *   *Test Case:* Verify the `calculateCourseDuration()` helper function in isolation.
    *   *Description:* Pass a mock start date (`2026-08-01`) and end date (`2026-12-01`) directly into the function and assert that it returns exactly `16` weeks, mocking or isolating any external database or network dependencies.
*   **Integration Testing:** 
    *   *Test Case:* Verify the interaction between the `CourseController` and the PostgreSQL/MongoDB database connection.
    *   *Description:* Send a valid course creation payload to the service layer and verify that the ORM/ODM successfully writes the record to the database and returns the generated database UUID without schema mismatches.
*   **System Testing:** 
    *   *Test Case:* Verify the end-to-end course enrollment lifecycle.
    *   *Description:* Perform a complete API call sequence: authenticate via `POST /api/auth/login` to receive a JWT, use the token to send a `POST /api/courses/` request, query `GET /api/courses/{id}` to confirm persistence, and finally execute a `DELETE /api/courses/{id}` request, ensuring the entire system functions seamlessly as a whole.
*   **User Acceptance Testing (UAT):** 
    *   *Test Case:* Verify that a College Admin can successfully publish a new semester curriculum.
    *   *Description:* From the perspective of a college administrator, log into the admin portal, input course details for a new department offering, and confirm that the system displays a "Course Published Successfully" confirmation message and lists the course in the student registration catalog.

### Part 2: Functional vs. Non-Functional Classification
Software testing is broadly categorized into checking what the system does (Functional) and how well it performs those tasks under various conditions (Non-Functional).

#### Test Case Classifications
*   **Unit Test Case:** Functional *(Verifies business logic correctness)*
*   **Integration Test Case:** Functional *(Verifies component data passing and schema compliance)*
*   **System Test Case:** Functional *(Verifies end-to-end operational requirements)*
*   **User Acceptance Test Case:** Functional *(Verifies workflow satisfaction against user requirements)*

#### Non-Functional Test Example for the API
*   **Testing Type:** Performance / Load Testing
*   **Test Case:** Verify API response latency under high concurrent traffic.
*   **Description:** Simulate 500 concurrent users sending `GET /api/courses/` requests simultaneously over a 60-second window.
*   **Expected Metric:** The API must maintain an average response time of less than 200 milliseconds with an error rate of 0% (no `500 Internal Server Error` or `504 Gateway Timeout` HTTP responses).

### Part 3: Black-Box vs. White-Box Testing

| Attribute | Black-Box Testing | White-Box Testing |
| :--- | :--- | :--- |
| **Definition** | Testing external application behavior without any knowledge of the internal code structure, architecture, or backend logic. | Testing internal structures, code pathways, branches, and algorithmic logic with full visibility into the source code. |
| **Focus Area** | Input/output validation, user interface workflows, API response codes, and business requirement compliance. | Code coverage, cyclomatic complexity, memory leaks, exception handling paths, and internal security flaws. |
| **Primary Performer** | **QA Testers / Automation Engineers** *(Focuses on user specifications and functional expectations)* | **Software Developers** *(Focuses on structural integrity and unit-level code correctness)* |

### Part 4: Formal Test Cases for `POST /api/courses/`

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_POST_001** | Verify successful creation of a new course with a valid payload. | 1. API server is running.<br>2. User is authenticated with an Admin JWT token. | 1. Send `POST /api/courses/` with header `Authorization: Bearer <token>`.<br>2. Attach valid JSON body: `{"code": "CS101", "name": "Intro to AI", "credits": 4}`.<br>3. Send request and inspect response. | HTTP Status Code **201 Created**. Response body returns the created object with a newly generated `id` and timestamp. | *(Leave blank)* | *(Leave blank)* |
| **TC_POST_002** | Verify API rejects course creation when mandatory fields are missing. | 1. API server is running.<br>2. User is authenticated with an Admin JWT token. | 1. Send `POST /api/courses/` with header `Authorization: Bearer <token>`.<br>2. Attach invalid JSON body missing the course name: `{"code": "CS102", "credits": 3}`.<br>3. Send request and inspect response. | HTTP Status Code **400 Bad Request**. Response body contains an error message specifying: `"Field 'name' is required"`. Course is not saved to DB. | *(Leave blank)* | *(Leave blank)* |
| **TC_POST_003** | Verify API denies course creation for unauthenticated requests. | 1. API server is running.<br>2. No auth token is provided in headers. | 1. Send `POST /api/courses/` with no `Authorization` header.<br>2. Attach valid JSON body: `{"code": "CS103", "name": "Data Structures", "credits": 4}`.<br>3. Send request and inspect response. | HTTP Status Code **401 Unauthorized** (or **403 Forbidden**). Response body indicates authentication failure. Course is not saved to DB. | *(Leave blank)* | *(Leave blank)* |

---

## Task 2: Defect Lifecycle & Severity Classification

### Part 1: Complete Defect Lifecycle
The defect lifecycle represents the path a bug takes from its initial detection by a QA engineer to its formal resolution and closure.

```text
[New] -> [Assigned] -> [Open] -> [Fixed] -> [Retest] -> [Verified] -> [Closed]
                          |                    |
                          |                    +--> [Reopened] (If fix fails)
                          |
                          +--> [Rejected] (Not a valid bug / working as intended)
                          +--> [Deferred] (Valid bug, but scheduled for a later release)