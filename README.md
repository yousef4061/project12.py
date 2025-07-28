# project12.py
# README - Mini Projects and Tests
## Overview
***This repository contains 5 mini Python projects and test files demonstrating object-oriented programming (OOP) concepts such as classes, inheritance, and methods. Below is a detailed description of each project/test.***

### 1. Mini Project
```

Description: A collection of OOP examples including:
Student Class: Manages student details (name, ID, courses) with methods:
study(): Displays enrolled courses.
exam(): Lists courses for exams.
remove_course(course_name): Removes a course if exists.
set_teacher(teacher_name): Sets teacher statically for all students.
BankAccount Class: Handles banking operations with:
deposit(amount): Adds money if amount > 0.
withdraw(amount): Subtracts money if sufficient funds and amount > 0.
get_balance(): Returns current balance.
Car Class: Tracks vehicle details with:
drive(distance): Increases mileage if distance > 0.
get_info(): Returns car details (year, make, model, mileage).
Inheritance Example: Eagle and Fish classes inherit from Animal base class, showcasing polymorphism.
Purpose: Demonstrates encapsulation, inheritance, and method usage in Python.
Usage: Run each class file (e.g., python student.py) to test 
functionalities.
```

### 2. Test 1
```

Description: Likely a variation of BankAccount, testing financial transactions. Includes methods for deposit, withdraw, and balance check with typo fixes (e.g., balance instead of balace).
Purpose: Validates error handling and attribute management.
Usage: Execute the file to perform sample transactions.
```

### 3. Test 2
```

Description: Possibly an extension of Student, with enhanced course management. Includes fixes for issues like TypeError: 'str' object is not callable (e.g., using join safely).
Purpose: Tests class behavior under various inputs.
Usage: Run to check student operations and debug errors.
```

### 4. Test 3
```

Description: Likely related to Car, focusing on mileage updates and info display. Includes attribute error fixes (e.g., mileage instead of mielage).
Purpose: Ensures proper attribute and method execution.
Usage: Test driving and info retrieval functions.
```

### 5. Test 4
```

Description: A continuation or variation of previous classes, possibly with additional features or bug fixes.
Purpose: Validates codebase with new test cases.
Usage: Run to explore functionalities or confirm fixes.
Requirements
Language: Python 3.x
Dependencies: No external libraries (uses standard library only).
How to Run
Save each file (e.g., student.py, bankaccount.py, etc.).
Open a terminal in the project directory.
Run with python filename.py (replace filename with the actual file name).
Notes
Some files may have initial bugs (e.g., typos) addressed in provided corrections.
Restart the Python environment if TypeError: 'str' object is not callable occurs to avoid variable shadowing.
Customize code (e.g., add methods) as needed.
Future Improvements
Add input validation for all methods.
Include unit tests using unittest framework.
Enhance documentation with docstrings for each class and method.
```

#### Author
Created by:**[yousef damqani]**
Date: 28 July 2025
