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