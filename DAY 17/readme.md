# Day 17 - Sorting Algorithm Analysis

## About
This project compares three sorting algorithms in Python:
- Selection Sort
- Insertion Sort
- Bubble Sort

The goal is to understand how sorting algorithms work, compare their execution times, and learn about time complexity and space complexity.

## Concepts Learned
- Time complexity and Big-O notation
- Best, average, and worst cases
- Space complexity
- In-place sorting
- Stable and unstable sorting
- Comparing sorting algorithms
- Measuring execution time using Python's `time` module
- Generating random numbers using the `random` module

## Algorithms and Complexity

| Algorithm | Best Case | Average Case | Worst Case | Extra Space |
|---|---|---|---|---|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Optimized Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |

*Note: The O(n) best case for Bubble Sort assumes the implementation stops early when no swaps occur.*

## How It Works
1. Generate a list of random numbers.
2. Create separate copies of the same list for each algorithm.
3. Sort each copy using a different algorithm.
4. Measure the execution time.
5. Display the sorted results and timing information.
6. Compare the results to check whether the algorithms produce the same sorted list.

## Technologies Used
- Python
- `random` module
- `time` module

## How to Run

Make sure Python is installed on your computer.

Run the program from your terminal:

```bash
python sorting_benchmark.py
```

## What I Learned
- Different sorting algorithms can produce the same result but perform different amounts of work.
- Selection Sort performs approximately O(n²) comparisons regardless of the initial order.
- Insertion Sort works efficiently with nearly sorted data.
- Optimized Bubble Sort can stop early when the list is already sorted.
- Fair benchmarking requires each algorithm to receive the same original dataset.
- Execution time can vary depending on the machine, input data, and implementation.

## Future Improvements
- Test larger datasets.
- Compare random, sorted, and reverse-sorted inputs.
- Repeat each benchmark and calculate average execution time.
- Verify that all algorithms produce the same sorted output.
- Compare the results with Python's built-in `sort()` method.

## Conclusion
This project helped me understand the differences between Selection Sort, Insertion Sort, and Bubble Sort, and how algorithm analysis helps us choose an appropriate solution for a given problem.

---

**Day:** 17/180  
**Roadmap:** Python, DSA and AI/ML Preparation
