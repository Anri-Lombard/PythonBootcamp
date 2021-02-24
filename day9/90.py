student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for person in student_scores:
    if student_scores[person] > 90:
        student_grades[person] = "Outstanding"
    elif student_scores[person] > 80:
        student_grades[person] = "Exceeds Expectations"
    elif student_scores[person] > 70:
        student_grades[person] = "Acceptable"
    else:
        student_grades[person] = "Fail"

print(student_grades)