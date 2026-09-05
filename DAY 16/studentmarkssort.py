def bubble_sort(marks):
    comparisons = 0
    swaps = 0
    n = len(marks)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                swaps += 1
                swapped = True
        if swapped == False:
            break
    return comparisons, swaps

marks = [78, 92, 65, 88, 55, 73, 95]

print("\nOriginal marks:")
print(marks)
comparisons, swaps = bubble_sort(marks)
print("\nSorted marks:")
print(marks)
print("\nHighest mark:", marks[-1])
print("Lowest mark:", marks[0])
print("Comparisons:", comparisons)
print("Swaps:", swaps)
