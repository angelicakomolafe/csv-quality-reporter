# CSV Quality Reporter

## Product Proposal
CSV Quality Reporter is a small Python data product designed to validate CSV files and generate a structured data quality report. It helps users quickly identify common data issues such as missing required columns, missing values, and duplicate rows, which are frequent problems when working with exported datasets.

The product was developed as a side project to demonstrate core software engineering principles including modular design, testing, version control, and continuous integration.

---

## Problem Statement
CSV files are widely used for data exchange but often suffer from inconsistent structure and poor data quality. Manually checking files is time-consuming and error-prone, particularly when datasets grow in size or are shared between teams.

---

## Proposed Solution
The CSV Quality Reporter provides:
- Automated validation of required columns
- Detection of missing values per column
- Duplicate row detection
- Generation of a JSON summary report
- A command-line interface for local execution

---

## Design & Prototype
A simple prototype was designed to illustrate the user flow:
1. Upload CSV file
2. Run validation
3. View validation results and summary report

(This prototype was created using a low-fidelity wireframe approach.)

---

## Project Management Approach
The project followed a lightweight agile approach focused on delivering a minimal viable product (MVP).

- Requirements were captured as features and tasks
- Development was completed incrementally
- Each feature was committed separately to GitHub
- Testing and CI were added once core functionality was implemented

GitHub was used for version control, commit history, and CI/CD automation.

---

## Requirements
### Functional Requirements
- Validate presence of required columns
- Count missing values per required column
- Detect duplicate rows
- Generate a JSON quality report
- Provide automated tests

### Non-Functional Requirements
- Reproducible execution using requirements.txt
- Automated test execution
- CI pipeline for verification

---

## MVP Development Process
1. Project structure and dependencies were defined
2. Validation logic was implemented in a dedicated module
3. Report generation logic was added
4. Automated tests were written using pytest
5. Continuous Integration was configured using GitHub Actions

---

## Test Driven Development & CI/CD
Tests were written to validate core behaviour such as missing columns, duplicate detection, and report structure.  
A GitHub Actions workflow automatically runs tests on every push and pull request to ensure code quality and correctness.

---

## Evaluation

### What Worked Well
The modular design of the CSV Quality Reporter proved effective, as separating validation and reporting logic into distinct modules improved readability, maintainability, and testability. This structure allowed individual components to be developed and verified independently. The use of automated testing with pytest significantly increased confidence in the correctness of the solution, particularly when handling edge cases such as missing columns and duplicate rows. Additionally, integrating GitHub Actions for Continuous Integration ensured that all tests were executed automatically on each push, reducing the risk of regressions and reinforcing good software engineering practice.

### Challenges and Trade-offs
One of the key challenges encountered was configuring Python imports correctly across different operating systems, particularly on Windows. This required explicit configuration of the Python path for pytest, which highlighted the importance of understanding Python’s module resolution behaviour. Due to time constraints and the scope of the MVP, design decisions were made to prioritise backend correctness and testability over user-facing features such as a graphical interface or advanced configuration options. While this limited usability for non-technical users, it ensured that the core functionality was robust and verifiable.

### Limitations
The current implementation uses hard-coded validation rules, meaning required columns must be specified manually. The tool also outputs reports exclusively in JSON format, which may not be ideal for all users. Furthermore, the application operates as a local script rather than a packaged command-line tool or web application, which limits accessibility for less technical users.

### Future Improvements
Future development could include configurable validation rules via a configuration file, support for additional output formats such as HTML or CSV summaries, and the introduction of a simple user interface or command-line wrapper. Performance optimisations could also be explored for handling very large datasets, alongside enhanced logging and error reporting.

Overall, the project successfully meets its objectives as a minimum viable product, demonstrating sound software engineering principles, effective testing practices, and the use of modern development workflows.

---

## User Documentation
### How to Run
```bash
pip install -r requirements.txt
pytest -q
# csv-quality-reporter
