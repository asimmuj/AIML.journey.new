# Day 14 - Selection Sort

## What I Learned

Today I learned about sorting and how Selection Sort works.

Sorting is the process of arranging data in a particular order, such as ascending or descending.

I learned how Selection Sort repeatedly finds the smallest or largest element from the unsorted part of a list and places it in its correct position.

### Topics Covered

* Sorting fundamentals
* Ascending and descending order
* Selection Sort algorithm
* Nested loops
* Finding minimum and maximum elements
* Swapping elements in a list
* Time and space complexity

## How Selection Sort Works

1. Start from the first element.
2. Assume it is the smallest (or largest) element.
3. Compare it with the remaining elements.
4. Update the index whenever a smaller (or larger) element is found.
5. Swap the selected element with the current position.
6. Repeat until the list is sorted.

## Example

**Before sorting:**

```python
[5, 3, 8, 1, 2]
```

**After sorting:**

```python
[1, 2, 3, 5, 8]
```

## Programs

| File                 | Description                                 |
| -------------------- | ------------------------------------------- |
| `selection_sort.py`  | Basic Selection Sort implementation         |
| `exercises.py`       | Practice problems on sorting                |
| `student_ranking.py` | Student ranking system using Selection Sort |
| `challenge.py`       | Top-K student ranking challenge             |

## Mini Project - Student Ranking System

Built a simple program that ranks students based on their marks using Selection Sort.

### Features

* Stores student names and marks
* Sorts students from highest to lowest marks
* Displays student rankings
* Shows the highest and lowest scorers
* Counts the number of comparisons made during sorting

## Time and Space Complexity

| Complexity       | Value |
| ---------------- | ----- |
| Best Case        | O(n²) |
| Average Case     | O(n²) |
| Worst Case       | O(n²) |
| Space Complexity | O(1)  |

Selection Sort uses constant extra space because it sorts the list in place.

## What I Understood

* Sorting helps organize data and makes certain operations easier.
* Selection Sort works by repeatedly selecting the minimum or maximum element.
* The algorithm uses nested loops to find the correct element.
* It is simple to understand but inefficient for large datasets.
* Sorting is useful in ranking systems, searching, and data processing.

## Next Step

Move on to **Day 15 - Insertion Sort** and understand how it differs from Selection Sort.

---

**Day 14 Completed: Selection Sort**