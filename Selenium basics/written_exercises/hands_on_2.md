# V-Model Analysis

## Task 1: V-Model Mapping

### 1. V-Model Diagram

```text
                  SDLC (Development)

           Requirements
                |
        System Design
                |
      Architecture Design
                |
         Module Design
                |
              Coding
                |
          Unit Testing
                |
      Integration Testing
                |
         System Testing
                |
      Acceptance Testing

             TDLC (Testing)
```

### 2. SDLC to TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan and Acceptance Test Cases |
| System Design | System Testing | System Test Plan and System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan and Integration Test Cases |
| Module Design | Unit Testing | Unit Test Plan and Unit Test Cases |
| Coding | Test Execution | Source Code and Executable Build |

---

### 3. Entry and Exit Criteria

#### Unit Testing

**Entry Criteria**
- Module development completed.
- Code compiles successfully.
- Unit test cases are prepared.

**Exit Criteria**
- All unit test cases executed.
- Critical defects fixed.
- Code coverage meets project standards.

---

#### Integration Testing

**Entry Criteria**
- Unit testing completed successfully.
- Modules integrated.
- Integration test cases prepared.

**Exit Criteria**
- All integration test cases executed.
- Interfaces work correctly.
- No critical integration defects remain.

---

#### System Testing

**Entry Criteria**
- Complete application deployed in the test environment.
- Integration testing completed.
- System test cases prepared.

**Exit Criteria**
- All planned system test cases executed.
- No Critical or High severity defects remain.
- System meets all functional and non-functional requirements.

---

#### Acceptance Testing

**Entry Criteria**
- System testing completed successfully.
- Product is stable.
- Acceptance test cases approved by stakeholders.

**Exit Criteria**
- Customer validates the application.
- All acceptance criteria satisfied.
- Product approved for release.

---

### 4. QA Engagement During Development

QA should participate before testing begins at the following stages:

1. **Requirements Review**
   - Review business requirements.
   - Identify ambiguities and missing requirements.
   - Ensure requirements are testable.

2. **Design Review**
   - Review API design and database design.
   - Identify possible risks and edge cases.
   - Prepare test scenarios early.

---

## Task 2: Agile QA and Shift-Left Testing

### 1. Problems with Waterfall Testing

1. Defects are discovered very late, making them expensive to fix.
2. Requirement misunderstandings remain unnoticed until testing begins.
3. Delays in development also delay testing, increasing the overall project timeline.

---

### 2. QA Role in Agile Ceremonies

#### Sprint Planning
- Review user stories.
- Define acceptance criteria.
- Estimate testing effort.

#### Daily Stand-up
- Report testing progress.
- Discuss blockers and defects.
- Coordinate with developers.

#### Sprint Review
- Validate completed features.
- Demonstrate tested functionality.
- Confirm acceptance criteria are satisfied.

#### Retrospective
- Discuss testing challenges.
- Suggest process improvements.
- Improve collaboration for future sprints.

---

### 3. Shift-Left Practices

#### a) Review Requirements for Testability
QA reviews requirements early to remove ambiguities and ensure every requirement can be tested.

#### b) Write Test Cases Before Coding (TDD/BDD)
Prepare test scenarios before development starts so developers clearly understand the expected behavior.

#### c) Static Code Analysis
Use automated tools to identify coding issues, security vulnerabilities, and coding standard violations before execution.

#### d) API Contract Testing Before Integration
Validate API request and response formats before integrating modules to prevent interface issues.

---

### 4. Acceptance Criteria (Given-When-Then)

#### Scenario 1: Happy Path

**Given** the college admin is logged into the Course Management System

**When** the admin enters a unique course code, valid course name, credits, and submits the form

**Then** the course is created successfully and a confirmation message is displayed.

---

#### Scenario 2: Duplicate Course Code

**Given** a course with the same course code already exists

**When** the admin attempts to create another course using that course code

**Then** the system displays an error message indicating that the course code already exists and the course is not created.

---

#### Scenario 3: Missing Required Fields

**Given** the admin opens the Create Course page

**When** the admin submits the form without entering the required fields

**Then** the system displays validation messages for the missing fields and prevents course creation.