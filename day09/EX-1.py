student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Crying about 2 more marks"
    elif score > 80:
        student_grades[student] = "Bruh shut up"
    elif score > 70:
        student_grades[student] = "Ok ok"
    else:
        student_grades[student] = "fuck u too"

print(student_grades)
