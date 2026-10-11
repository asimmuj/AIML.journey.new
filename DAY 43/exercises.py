import numpy as np
marks = [30, 40, 50, 60, 70]
average = np.mean(marks)
median = np.median(marks)
print("Marks:", marks)
print("Mean:", average)
print("Median:", median)

import matplotlib.pyplot as plt
marks = [
    35, 40, 45, 48, 50,
    52, 55, 58, 60, 62,
    65, 67, 70, 72, 75,
    78, 80, 85, 90, 95
]
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(marks, bins=4, edgecolor="black")
plt.title("Histogram - 4 Bins")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.subplot(1, 2, 2)
plt.hist(marks, bins=8, edgecolor="black")
plt.title("Histogram - 8 Bins")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
marks = [10, 12, 13, 14, 15, 16, 100]
print("Median:", np.median(marks))
print("Mean:", np.mean(marks))
plt.boxplot(marks)
plt.title("Box Plot - Detecting Outliers")
plt.ylabel("Values")
plt.show()

import matplotlib.pyplot as plt
advertising = [100, 150, 200, 250, 300, 350, 400, 450]
sales = [20, 25, 30, 35, 42, 45, 55, 60]
plt.scatter(advertising, sales)
plt.title("Advertising Spend vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales (units)")
plt.show()