def predicted_marks(hours):
    marks=8*hours+20
    return marks
hours=float(input("enter study hours"))
if hours<0:
    print("hours cannot be negative")
else:
    predicted_marks=predicted_marks(hours)
    if predicted_marks>100:
        predicted_marks=100
print("study hours: ",hours)
print("predicted marks: ",predicted_marks)