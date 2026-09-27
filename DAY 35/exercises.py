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

# students = pd.DataFrame({
#     "name": ["Mujtaba","Ali", "Sara", "Ahmed"],
#     "age": [20, 19, 20, 18],
#     "python": [85, 72, 91, 68],
#     "ml": [80, 75, 89, 70]
# })
# students["total"] = students["python"] + students["ml"]
# students["average"]=students["total"]/2
# print(students)

#exercise 4
import pandas as pd

students = pd.DataFrame({
    "name": ["Mujtaba", "Ali", "Sara", "Ahmed"],
    "age": [20, 19, 20, 18],
    "Python": [85, 72, 91, 68],
    "ML": [80, 75, 89, 70]
})

# 1. Select Mujtaba's row
print("Mujtaba's details:")
print(students.iloc[0])

# 2. Select Sara's row
print("\nSara's details:")
print(students.iloc[2])

# 3. Select only name and ML
print("\nName and ML marks:")
print(students[["name", "ML"]])

# 4. Select first three rows
print("\nFirst three students:")
print(students.iloc[0:3])

# 5. Select Python and ML columns
print("\nPython and ML marks:")
print(students[["Python", "ML"]])