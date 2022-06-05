student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

student_grades.update(student_scores)
for key in student_scores:
    if student_scores[key] in range(91,101):
        student_grades[key] = "Outstanding"
    elif student_scores[key] in range(81,91):
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] in range(71,81):
        student_grades[key] = "Acceptable"
    elif student_scores[key] in range(0,71):
        student_grades[key] = "Fail"
    else:
        print('Please enter a valid score.')

print(student_grades)
