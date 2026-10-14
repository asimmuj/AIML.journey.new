# Day 1 — Python Foundations

Part of my 180-Day AI/ML Internship Roadmap.

## 🎯 Objective

Build a strong Python foundation required for future AI/ML development.

## 📚 Concepts Learned

- Variables
- Data types
  - int
  - float
  - str
  - bool
- User input
- Type conversion
- Arithmetic operators
- Comparison operators
- Conditional statements
  - if
  - elif
  - else
- Lists
- Dictionaries
- for loops
- Functions
- Basic input validation
- Basic error/edge-case handling

## 🧪 Exercises

### Exercise 1 — Calculator
Created a basic calculator that performs:
- Addition
- Subtraction
- Multiplication
- Division

### Exercise 2 — Even or Odd
Created a program that determines whether a number is even or odd.

### Exercise 3 — Greatest of Three Numbers
Created a program to find the greatest among three numbers.

### Exercise 4 — Average of a List
Calculated the average of a list of marks using `sum()` and `len()`.

### Exercise 5 — Passing Students
Counted the number of students who scored at least 40 marks.

## 🚀 Mini Project — Student Performance Analyzer

A command-line Python program that analyzes a student's academic performance.

### Features

- Takes student's name as input
- Accepts a variable number of subjects
- Collects marks for each subject
- Calculates total marks
- Calculates average marks
- Finds highest mark
- Finds lowest mark
- Determines pass/fail status
- Assigns a performance category
- Validates subject count and marks

### Performance Categories

| Average | Performance |
|---|---|
| < 40 | Fail |
| 40–59.99 | Needs Improvement |
| 60–74.99 | Average |
| 75–89.99 | Good |
| 90+ | Excellent |

## 🧠 What I Learned

The most important thing I learned today was how different Python concepts work together to build a complete program.

I also learned that writing code is not only about making it work for normal inputs. I need to consider edge cases and validate user input.

For example:
- What happens if the user enters 0 subjects?
- What happens if marks are greater than 100?
- What happens if two numbers are equal?

## 🔍 Challenges / Mistakes

During Day 1, I initially made mistakes with:

- Using `in` instead of comparison ranges
- Printing inside a loop when I only wanted the final result
- Assigning the result of `print()` to a variable
- Not handling zero subjects
- Not considering equal values when finding the greatest number

I fixed these issues after reviewing my code.

## 🛠️ Tech Used

- Python 3
- VS Code
- Git
- GitHub

## 📁 Files

```text
day-01-python-foundations/
│
├── exercises.py
├── student_performance_analyzer.py
└── README.md