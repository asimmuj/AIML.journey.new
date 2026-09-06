import time
import random
def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def insertionsort(numbers):
    for i in range(1,len(numbers)):
        key=numbers[i]
        j=i-1
        while j>=0 and numbers[j]>key:
            numbers[j+1]=numbers[j]
            j-=1
            numbers[j+1]=key
    return numbers

def bubblesort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] >  numbers[j + 1]:
             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers=[random.randint(1,30) for _ in range(10)]
start1=time.time()
selection_sort(numbers)
end1=time.time()
print("selection sort: ", selection_sort(numbers))
print("selection sort time: ",end1-start1)
start2=time.time()
insertionsort(numbers)
end2=time.time()
print("insertion sort: ", insertionsort(numbers))
print("insertion sort time: ",end2-start2)
start3=time.time()
bubblesort(numbers)
end3=time.time()
print("bubble sort: ", bubblesort(numbers))
print("bubble sort time: ",end3-start3)