covariance = 25
if covariance > 0:
    print("Positive covariance")
    print("X and Y tend to move in the same direction.")
elif covariance < 0:
    print("Negative covariance")
    print("X and Y tend to move in opposite directions.")
else:
    print("Zero covariance")
    print("No linear tendency to move together.")

#exercise 2
correlation = -0.92
if correlation < 0:
    print("Strong negative correlation")
    print("As one variable increases, the other tends to decrease.")
elif correlation > 0:
    print("Positive correlation")
else:
    print("No linear correlation")

#exercise 3
import numpy as np

x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]

correlation = np.corrcoef(x, y)[0][1]

print("Correlation:", correlation)

if abs(correlation) < 0.01:
    print("No linear correlation")
    print("But a nonlinear relationship exists.")

#exercise 4
import numpy as np
x = [10, 20, 30, 40, 50]
y = [5, 15, 25, 35, 45]
mean_x = np.mean(x)
mean_y = np.mean(y)
covariance = np.cov(x, y)[0][1]
correlation = np.corrcoef(x, y)[0][1]
print("Mean of X:", mean_x)
print("Mean of Y:", mean_y)
print("Covariance:", covariance)
print("Correlation:", correlation)
if correlation > 0:
    print("Positive relationship")
elif correlation < 0:
    print("Negative relationship")
else:
    print("No linear relationship")