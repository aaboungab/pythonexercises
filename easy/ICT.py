print("ICT Results")
print("Total marks are out of 175")
print("")
name = input("please enter your namme: ")
print("")
print("Hello,",name)
print("")
student_homework = int(input("Homework mark out of 25: "))
student_assignment = int(input("Assignment mark out of 50: "))
student_finalexam = int(input("Final Exam mark out of 100: "))

def grade_calculator(homework, assignmnet, finalexam):
    if homework > 25 or assignmnet > 50 or finalexam > 100:
        return "invalid marl entered"
    total = homework+assignmnet+finalexam
    grade = (total/175)*100
    return grade

def grade_boundaries(grade):
    if grade >= 90:
        letter_grade = "A*"
    elif grade >= 80:
        letter_grade = "A"
    elif grade >= 70:
        letter_grade = "B"
    elif grade >= 60:
        letter_grade = "C"
    elif grade >= 40:
        letter_grade = "Pass"
    else:
        print("You have Failed")
    return letter_grade

grade = grade_calculator(student_homework,student_assignment,student_finalexam)
letter_grade = grade_boundaries(grade)
print("")
print(f"{name} you have achieved a total grade of {grade:.2f}% which is grade {letter_grade}")
