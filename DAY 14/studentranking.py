students=[
     ["ali",72],
     ["sara",92],
     ["zeeshan",85],
     ["mujtaba",96]
]
def selection_sort(students):
        comparisions=0
        for i in range(len(students)):
            min_index = i
            for j in range(i + 1, len(students)):
                comparisions+=1
                if students[j][1] < students[min_index][1]:
                    min_index = j
                    students[i],students[min_index]=students[min_index],students[i]
        return students
selection_sort(students)
print(students)