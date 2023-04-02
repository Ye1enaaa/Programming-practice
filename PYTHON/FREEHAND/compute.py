grades = []
convertedGrades = []
# grade = ''
floatGrade = ''
def computeGrades():
    global floatGrade
    while floatGrade != '0.2':
        floatGrade = input("Enter your grades: ")
        grades.append(float(floatGrade))
    grades.pop()

    for grade in grades:
        newValue = grade * 3
        convertedGrades.append(newValue)
    
    totalGradesBasedOnUnits = sum(convertedGrades)
    totalNumberOfGrades = len(convertedGrades) * 3
    # print(totalNumberOfGrades)
    # print(grades)
    # print(convertedGrades)
    totalGPA = totalGradesBasedOnUnits / totalNumberOfGrades
    print(totalGPA)
computeGrades()