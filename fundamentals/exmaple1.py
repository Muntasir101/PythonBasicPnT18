"""
Suppose we need to assign different grades to students based on their scores.

If a student scores above 90, assign grade A
If a student scores above 75, assign grade B
If a student scores above 65, assign grade C
"""

student_mark = int(input('Enter your marks: '))

if student_mark > 90:
    print("Grade A")
elif student_mark > 75:
    print("Grade B")
elif student_mark > 65:
    print("Grade C")
