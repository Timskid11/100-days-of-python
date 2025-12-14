student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for eachkey in student_scores:
    key_score = student_scores[eachkey]
    if 100 >=key_score >= 91 :
        student_grades[eachkey] = "Outstanding"
    elif 90 >=key_score >= 81:
        student_grades[eachkey] = "Exceeds Expectations"
    elif 80 >= key_score >=71:
        student_grades[eachkey] = "Acceptable"
    elif key_score <= 70:
        student_grades[eachkey] = "Fail"

print(student_grades)