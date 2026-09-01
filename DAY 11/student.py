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
target=int(input("enter a id to search: "))
low = 0
high = len(student_ids)-1
comparisions=0
while low<=high:
        comparisions+=1
        mid= (low+high)//2
        if student_ids[mid]==target:
            print("student found!")
            print("index: ",mid)
            break
        elif target>student_ids[mid]:
            low = mid+1
        else:
            high=mid-1
print("comparisions: ",comparisions)
    
