# Day 9 - Linear Search

## 📌 Overview

Today I learned **Linear Search**, one of the simplest searching algorithms in DSA.

Linear Search checks elements one by one until the target element is found or the entire list has been checked.

## 🎯 What I Learned

* What searching means
* Linear Search algorithm
* Lists and indexing
* Using loops for searching
* Comparing elements with a target
* Boolean flags
* `break`
* `return`
* Handling "not found" cases with `-1`
* Best and worst-case performance
* Introduction to Big-O notation

## 🔎 How Linear Search Works

Given a list and a target:

1. Start from the first element.
2. Compare the current element with the target.
3. If they are equal, the target is found.
4. Otherwise, move to the next element.
5. Continue until the target is found or the list ends.
6. If the target does not exist, return `-1`.

## 💻 Example

```python
def linearsearch(numbers, target):

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1
```

## 🧠 Example

For:

```python
numbers = [10, 25, 7, 42, 18]
target = 42
```

The algorithm checks:

```text
10 → ❌
25 → ❌
7  → ❌
42 → ✅
```

Therefore, the result is:

```text
Index: 3
```

## 🚀 Mini Project - Student Search System

I built a simple student search program using Linear Search.

The program:

* Stores student names in a list
* Takes a student name from the user
* Searches through the list using Linear Search
* Displays whether the student was found
* Displays the student's index when found

Example:

```text
Enter student name: Sara

Student found!
Index: 3
```

If the student doesn't exist:

```text
Enter student name: John

Student not found!
```

## ⏱️ Time Complexity

### Best Case

The target is the first element.

```text
O(1)
```

### Worst Case

The target is the last element or doesn't exist.

```text
O(n)
```

### Space Complexity

```text
O(1)
```

## 🔗 Key Concept

Linear Search connects several Python concepts I learned previously:

```text
Lists
  ↓
Indexing
  ↓
Loops
  ↓
Conditions
  ↓
Functions
  ↓
Searching Algorithm
```

## 💡 Key Takeaway

Linear Search is simple but can become inefficient for large datasets because it may need to check every element.

It is useful when the dataset is small, unsorted, or when searches are not performed frequently.

## 📚 Next Step

Next, I will continue solving searching problems and improve my problem-solving ability before moving deeper into DSA.
