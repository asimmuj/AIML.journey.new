#enhanced version
def binary_search(student_ids, target):
    low = 0
    high = len(student_ids) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        print(
            "Checking index:",
            mid,
            "ID:",
            student_ids[mid]
        )
        if student_ids[mid] == target:
            return mid, comparisons
        elif target > student_ids[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons
student_ids = [
    102,
    115,
    128,
    143,
    156,
    172,
    189,
    205,
    221,
    240
]
target = int(input("Enter student ID: "))
index, comparisons = binary_search(student_ids, target)
if index != -1:
    print("\nStudent found!")
    print("Student ID:", target)
    print("Index:", index)
    print("Comparisons:", comparisons)
else:
    print("\nStudent not found!")
    print("Comparisons:", comparisons)...