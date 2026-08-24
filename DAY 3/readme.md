# Day 3 — Python Functions

## 📌 Overview

Day 3 of my 180-Day AI/ML journey focused on **Python Functions**.

The main goal was to understand how functions make programs reusable, organized, and easier to maintain.

I also built a **Student Performance Analyzer** using functions, loops, conditions, and Python's built-in functions.

---

## 🎯 Objectives

* Understand what functions are and why they are useful
* Create and call functions using `def`
* Understand parameters and arguments
* Understand `return`
* Understand the difference between `print()` and `return`
* Use functions with lists
* Use loops and conditions inside functions
* Break a program into smaller reusable components
* Practice basic function design

---

## 📚 Concepts Learned

### 1. Defining a Function

```python
def greet():
    print("Hello")
```

### 2. Calling a Function

```python
greet()
```

### 3. Parameters and Arguments

```python
def greet(name):
    print("Hello", name)

greet("Mujtaba")
```

* `name` → parameter
* `"Mujtaba"` → argument

### 4. Return Statement

```python
def add(a, b):
    return a + b
```

`return` sends a value back to the caller so that the result can be stored or used elsewhere.

### 5. `print()` vs `return`

`print()` displays a value.

`return` sends a value back to the caller.

This distinction was one of the most important concepts learned on Day 3.

### 6. Functions with Lists

Functions can receive lists as parameters and process their elements using loops and conditions.

---

## 🛠️ Mini Project — Student Performance Analyzer

The project analyzes a list of student marks:

```python
marks = [35, 78, 91, 42, 67, 29, 88]
```

The program calculates:

* Total number of students
* Number of passed students
* Number of failed students
* Highest mark
* Lowest mark
* Average mark

### Example Output

```text
Total students: 7
Passed students: 5
Failed students: 2
Highest marks: 91
Lowest marks: 29
Average marks: 61.42857142857143
```

---

## 🧠 Key Learning

The biggest lesson from Day 3 was that functions should be designed to perform a specific task and, when appropriate, **return their result instead of directly printing it**.

For example:

```python
def average(marks):
    return sum(marks) / len(marks)
```

The returned value can then be reused:

```python
avg = average(marks)

print(avg)
```

This makes functions more reusable and easier to combine with other parts of a program.

---

## 💡 What I Improved

My first implementation used `print()` directly inside most functions.

After reviewing the project, I understood that returning values is generally better when the result needs to be reused elsewhere.

I also learned the importance of meaningful and consistent function names such as:

```python
count_passed()
count_failed()
highest_mark()
lowest_mark()
calculate_average()
```

---

## 🧪 Practice

During Day 3, I practiced:

* Creating simple functions
* Passing arguments
* Returning values
* Working with lists inside functions
* Using loops inside functions
* Using conditions inside functions
* Building reusable calculations

---

## 🚀 Next Step

Day 3 established the foundation for writing reusable Python code.

The next stages will build on these fundamentals and gradually introduce more advanced Python concepts, problem solving, data structures, and eventually AI/ML programming.

---

## 📅 180-Day AI/ML Journey

**Day 3 / 180 — Python Functions**

