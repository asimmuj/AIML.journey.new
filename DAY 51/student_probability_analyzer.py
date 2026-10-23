total_students = int(input("Total students: "))
python_pass = int(input("Passed Python: "))
both_pass = int(input("Passed both Python and Math: "))
if total_students <= 0:
    print("Total students must be greater than 0.")
elif python_pass < 0 or python_pass > total_students:
    print("Invalid number of students who passed Python.")
elif both_pass < 0 or both_pass > python_pass:
    print("Invalid number of students who passed both subjects.")
else:
    probability = both_pass / python_pass
    print("\n--- Student Probability Analyzer ---")
    print("Total students:", total_students)
    print("Passed Python:", python_pass)
    print("Passed both subjects:", both_pass)
    print("P(Math | Python):", round(probability, 2))
    print("Probability percentage:", round(probability * 100, 2), "%")
