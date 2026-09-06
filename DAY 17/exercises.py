import time
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
            if numbers[j] <  numbers[j + 1]:
             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers=[9,4,5,2,3,8]
start1=time.time()
selection_sort(numbers)
end1=time.time()
print("selection sort: ",end1-start1)
start2=time.time()
insertionsort(numbers)
end2=time.time()
print("insertion sort: ",end2-start2)
start3=time.time()
bubblesort(numbers)
end3=time.time()
print("bubble sort: ",end3-start3)