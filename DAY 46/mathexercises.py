def f(x):
    return 3 * x + 2
print("f(1) =", f(1))
print("f(4) =", f(4))
print("f(10) =", f(10))

#exercise 2
def calculate_total(price, quantity):
    total = price * quantity
    return total
price = 50
quantity = 4
total = calculate_total(price, quantity)
print("Price per item:", price)
print("Quantity:", quantity)
print("Total cost:", total)

#exercise 3
def predict(x):
    return 4 * x + 5
x = 6
prediction = predict(x)
print("Input:", x)
print("Predicted output:", prediction)

#exrcise 4
def predict_marks(study_hours, practice_tests):
    marks = (2 * study_hours) + (3 * practice_tests) + 10
    return marks
study_hours = 5
practice_tests = 4
predicted_marks = predict_marks(study_hours, practice_tests)
print("Study hours:", study_hours)
print("Practice tests:", practice_tests)
print("Predicted marks:", predicted_marks)