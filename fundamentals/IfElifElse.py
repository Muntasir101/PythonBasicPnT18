pass_mark = 40

student_mark = int(input('Enter your marks: '))

if student_mark >= pass_mark:
    if 40 <= student_mark < 50:
        print("Grade D")
    elif 50 <= student_mark < 60:
        print("Grade C")
    elif 60 <= student_mark < 70:
        print("Grade B")
    elif 70 <= student_mark < 80:
        print("Grade A-")
    elif 80 <= student_mark < 90:
        print("Grade A")
    elif 90 <= student_mark <= 100:
        print("Grade A+")
    else:
        print("Invalid marks for Grade")
else:
    print("Fail")