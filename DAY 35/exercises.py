import pandas as pd
# students = pd.DataFrame({
#     "name": ["Mujtaba","Ali", "Sara", "Ahmed"],
#     "age": [20, 19, 20, 18],
#     "python": [85, 72, 91, 68],
#     "ml": [80, 75, 89, 70]
# })
# print(students)
# print(students["python"])
# print(students["ml"])
# print(students.head(2))
# print(students.shape)

# #exercise 2
# students = pd.DataFrame({
#     "name": ["Mujtaba","Ali", "Sara", "Ahmed"],
#     "age": [20, 19, 20, 18],
#     "python": [85, 72, 91, 68],
#     "ml": [80, 75, 89, 70]
# })
# print(students["python"].mean())
# print(students["python"].max())
# print(students["python"].min())
# print(students["ml"].mean())
# print(students["ml"].max())

students = pd.DataFrame({
    "name": ["Mujtaba","Ali", "Sara", "Ahmed"],
    "age": [20, 19, 20, 18],
    "python": [85, 72, 91, 68],
    "ml": [80, 75, 89, 70]
})
students["total"] = students["python"] + students["ml"]
students["average"]=students["total"]/2
print(students)