import pandas as pd
data = {
    "Name": ["Ali", "Sara", "John", "Mujtaba", "Zara", "Ahmed"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Marks": [85, 90, 78, 88, 95, 75],
    "Salary": [50000, 45000, 55000, 48000, 60000, 42000]
}
df = pd.DataFrame(data)
print("Average marks by department:")
print(df.groupby("Department")["Marks"].mean())
print("\nMaximum marks:")
print(df.groupby("Department")["Marks"].max())
print("\nMinimum marks:")
print(df.groupby("Department")["Marks"].min())
print("\nTotal salary:")
print(df.groupby("Department")["Salary"].sum())

#exercise 2
import pandas as pd
data = {
    "Name": ["Ali", "Sara", "John", "Mujtaba", "Zara", "Ahmed"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Marks": [85, 90, 78, 88, 95, 75]
}
df = pd.DataFrame(data)
result = df.groupby("Department").agg({
    "Marks": ["mean", "max", "min", "count"]
})
print(result)

#exercise 3
import pandas as pd
data = {
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Tablet", "Laptop"],
    "Region": ["North", "South", "North", "East", "South", "East"],
    "Sales": [50000, 30000, 60000, 25000, 20000, 45000]
}
df = pd.DataFrame(data)
# Total sales by product
print("Total sales by product:")
print(df.groupby("Product")["Sales"].sum())
# Average sales by region
print("\nAverage sales by region:")
print(df.groupby("Region")["Sales"].mean())
# Sales by product and region
print("\nSales by product and region:")
print(df.groupby(["Product", "Region"])["Sales"].sum())
# Product with highest total sales
total_sales = df.groupby("Product")["Sales"].sum()
best_product = total_sales.idxmax()
print("\nProduct with highest sales:", best_product)
print("Total sales:", total_sales.max())

#exercise 4
import pandas as pd
data = {
    "Name": ["Ali", "Sara", "John", "Mujtaba", "Zara",
             "Ahmed", "Ayesha", "Rahul", "Fatima", "David"],

    "Department": ["IT", "HR", "IT", "Finance", "HR",
                   "Finance", "IT", "HR", "Finance", "IT"],

    "Age": [22, 25, 24, 28, 26, 30, 23, 27, 29, 25],

    "Salary": [35000, 30000, 40000, 45000, 32000,
               50000, 38000, 33000, 48000, 42000],

    "Experience": [1, 3, 2, 5, 4, 6, 1, 4, 5, 3]
}
df = pd.DataFrame(data)
print("Average salary by department:")
print(df.groupby("Department")["Salary"].mean())
print("\nMaximum experience:")
print(df.groupby("Department")["Experience"].max())
print("\nNumber of employees:")
print(df.groupby("Department")["Name"].count())
print("\nAverage age:")
print(df.groupby("Department")["Age"].mean())
print("\nTotal salary expenditure:")
print(df.groupby("Department")["Salary"].sum())