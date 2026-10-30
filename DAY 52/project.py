import statistics
marks = [75, 80, 65, 90, 85, 70, 80, 95, 60, 80]
mean=statistics.mean(marks)
median=statistics.median(marks)
mode=statistics.mode(marks)
maximum=max(marks)
minimum=min(marks)
range=maximum-minimum
variance=statistics.pvariance(marks)
stddev=statistics.pstdev(marks)
print("mean: ",mean)
print("median: ",median)
print("mode: ",mode)
print("maximum marks: ",maximum)
print("minimum marks: ",minimum)
print("range: ",range)
print("variance: ",variance)
print("standard deviation: ",stddev)