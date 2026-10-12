# Day 16 - Bubble Sort in Python

## About
Today I learned **Bubble Sort**, a simple sorting algorithm that sorts elements by comparing two adjacent elements and swapping them if they are in the wrong order.

I also practiced using nested loops, swapping values, counting comparisons and swaps, and optimizing the algorithm.

## What I Learned
- Understanding how Bubble Sort works
- Comparing adjacent elements
- Swapping elements in Python
- Using nested loops for sorting
- Counting comparisons and swaps
- Optimizing Bubble Sort using a `swapped` variable
- Understanding time and space complexity

## How Bubble Sort Works

Bubble Sort repeatedly compares neighboring elements.

If the left element is greater than the right element, they are swapped. After each pass, the largest unsorted element moves to its correct position.

### Example

**Before sorting:**
```python
[5, 3, 8, 4, 2]
```

**After sorting:**
```python
[2, 3, 4, 5, 8]
```

## Mini Project: Student Marks Sorter

I created a Student Marks Sorter using Bubble Sort.

### Features
- Displays the original marks
- Sorts marks in ascending order
- Displays the highest and lowest marks
- Counts comparisons and swaps
- Detects whether the list was already sorted

## Time and Space Complexity

| Case | Time Complexity |
|---|---|
| Best case (optimized) | O(n) |
| Average case | O(n²) |
| Worst case | O(n²) |

**Space Complexity:** O(1), excluding the input list, because Bubble Sort sorts the list in place.

## Technologies Used
- Python 3
- VS Code

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Run the Python file:

```bash
python bubble_sort.py
```

## Key Takeaway

I learned how Bubble Sort works, why adjacent elements are compared, and how an optimization can stop unnecessary passes when the list is already sorted.

This helped me improve my understanding of loops, swapping, algorithm optimization, and sorting algorithms.

---

**Day 16 of my 180-Day AI/ML Learning Roadmap**

*Learn → Understand → Implement → Build → Review → Improve*
