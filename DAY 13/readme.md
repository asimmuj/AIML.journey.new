# Day 13 - Selection Sort

## Overview

Today I started learning sorting algorithms. I learned how Selection Sort works and implemented it in Python.

The main idea is to find the smallest element in the unsorted part of a list and place it in its correct position.

## What I Learned

* What sorting algorithms are and why they are used.
* How Selection Sort works step by step.
* How to find the minimum element in a list.
* How to swap elements using Python.
* How to sort a list in ascending order.
* Understanding the time complexity of Selection Sort.

## How Selection Sort Works

1. Start from the first element.
2. Assume it is the smallest element.
3. Compare it with the remaining elements.
4. Find the actual smallest element.
5. Swap it with the current element.
6. Repeat the process until the list is sorted.

## Example

**Before sorting:**

```python
[64, 25, 12, 22, 11]
```

**After sorting:**

```python
[11, 12, 22, 25, 64]
```

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n²)      |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

**Space Complexity:** O(1)

Selection Sort is an in-place sorting algorithm because it sorts the original list without requiring another list.

## Files

* `selection_sort.py` - Implementation of Selection Sort.
* `exercises.py` - Practice problems.
* `mini_project.py` - Application of sorting concepts.

## Key Takeaway

Selection Sort helped me understand how sorting works internally instead of relying on Python's built-in `sort()` method.

This is my first step toward understanding more efficient sorting algorithms and their role in problem-solving.

---

**Day 13 completed. Moving forward to the next DSA concept.**