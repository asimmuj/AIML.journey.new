required_skills = {
    "Python",
    "SQL",
    "Git",
    "Machine Learning",
    "Statistics"
}

student_skills = {
    "Python",
    "Git",
    "HTML"
}
print("Skills student already have:",student_skills)
print("Skills missing: ",required_skills-student_skills)
print("total required skills: ",len(required_skills))
print("total skills currently possesed: ",len(student_skills))
percentage=len(required_skills-student_skills)*100/len(required_skills)
print("skill match: ",percentage,"%")