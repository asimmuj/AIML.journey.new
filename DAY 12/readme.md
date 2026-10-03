# Day 12 - Binary Search Variations

## What I Learned

Today I continued learning Binary Search and focused on understanding how it works instead of just memorizing the code.

I practiced:

* Finding an element in a sorted list.
* Understanding `low`, `high`, and `mid`.
* Counting comparisons during a search.
* Finding the first occurrence of a duplicate element.
* Finding the last occurrence of a duplicate element.
* Understanding why Binary Search requires sorted data.
* Tracing the algorithm step by step.

## How Binary Search Works

Binary Search reduces the search space by half in every iteration.

1. Set `low` to the first index.
2. Set `high` to the last index.
3. Calculate the middle index.
4. Compare the middle element with the target.
5. If the target is smaller, search the left half.
6. If the target is larger, search the right half.
7. Repeat until the element is found or the search space becomes empty.

## Time Complexity

| Algorithm     | Time Complexity |
| ------------- | --------------- |
| Linear Search | O(n)            |
| Binary Search | O(log n)        |

Binary Search is faster for large sorted lists because it eliminates half of the remaining elements in each step.

## Problems Practiced

* Basic Binary Search
* Binary Search with comparison counter
* First occurrence of an element
* Last occurrence of an element
* Searching student IDs
* Handling elements that are not present in the list

## Mini Project - Student ID Search

I created a program that searches for a student using their ID.

The program:

* Takes a student ID as input.
* Uses Binary Search to find the ID.
* Displays the student's name if found.
* Shows the index and number of comparisons.
* Displays a message if the student does not exist.

## What I Understood

* Why `low` is updated using `mid + 1`.
* Why `high` is updated using `mid - 1`.
* Why sorted data is necessary for Binary Search.
* How duplicate elements change the search logic.
* How reducing the search space makes an algorithm more efficient.

## Challenges

The main challenge was understanding how to modify Binary Search to find the first and last occurrences of duplicate elements instead of stopping at the first match.

## Conclusion

Day 12 helped me understand Binary Search more deeply. I also learned that knowing an algorithm's code is not enough. Understanding how and why its logic works is important for solving new problems.

**Next:** Moving towards more DSA problem-solving and sorting algorithms.