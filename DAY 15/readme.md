# Day 15 - Insertion Sort

## 📌 Topic

Insertion Sort

## 🎯 Objective

Learn how Insertion Sort works, implement it in Python, understand its time and space complexity, and compare it with Selection Sort.

---

## 🧠 What I Learned

Insertion Sort builds the sorted list one element at a time.

It takes the current element and compares it with the elements before it. If an element is bigger, it is shifted one position to the right. The current element is then placed in its correct position.

It is similar to arranging playing cards in your hand.

---

## 🔍 How Insertion Sort Works

Example:

```text
[5, 3, 4, 1, 2]
```

Take `3`:

```text
[3, 5, 4, 1, 2]
```

Take `4`:

```text
[3, 4, 5, 1, 2]
```

Take `1`:

```text
[1, 3, 4, 5, 2]
```

Take `2`:

```text
[1, 2, 3, 4, 5]
```

The list becomes sorted by inserting each element into its correct position.

---

## 💻 Basic Implementation

```python
numbers = [5, 3, 4, 1, 2]

for i in range(1, len(numbers)):

    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

## ⚔️ Selection Sort vs Insertion Sort

| Selection Sort                             | Insertion Sort                     |
| ------------------------------------------ | ---------------------------------- |
| Finds the smallest element                 | Takes the current element          |
| Mainly uses swapping                       | Mainly uses shifting               |
| Always O(n²) comparisons                   | Can be O(n) when nearly sorted     |
| Simple but not good for nearly sorted data | Works well with nearly sorted data |
| O(1) extra space                           | O(1) extra space                   |

---

## ⏱️ Time Complexity

### Best Case

**O(n)**

This happens when the list is already sorted.

### Average Case

**O(n²)**

### Worst Case

**O(n²)**

This happens when the list is sorted in reverse order.

### Space Complexity

**O(1)** extra space because the algorithm sorts the list in place.

---

## 📝 Exercises

### Exercise 1

Sort a list using Insertion Sort:

```text
[8, 4, 6, 2, 7]
```

### Exercise 2

Manually trace Insertion Sort:

```text
[7, 2, 5, 1]
```

### Exercise 3

Modify the algorithm to sort numbers in descending order.

### Exercise 4

Count the number of shifts performed during sorting.

---

## 🚀 Mini Project - Student Ranking System

I created a small student ranking program that sorts students according to their marks using Insertion Sort.

Example data:

```python
students = [
    ["Ali", 78],
    ["Sara", 92],
    ["Zeeshan", 85],
    ["Mujtaba", 95],
    ["Ahmed", 68]
]
```

Expected ranking:

```text
1. Mujtaba - 95
2. Sara - 92
3. Zeeshan - 85
4. Ali - 78
5. Ahmed - 68
```

The