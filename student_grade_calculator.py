

def get_marks(subject):
    while True:
        user_input = input(f"Enter marks for {subject} (0-100): ")

        if not user_input.isdigit():
            print("Invalid input! Please enter a whole number.")
            continue

        marks = int(user_input)

        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid marks! Please enter between 0 and 100.")

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    student_name = input("Enter student name: ")

    subjects = ["Python", "Maths", "Science", "English", "Computer Science"]
    marks_list = []

    for subject in subjects:
        marks = get_marks(subject)
        marks_list.append(marks)

    total = sum(marks_list)
    average = total / len(subjects)

    passed = True

    for marks in marks_list:
        if marks < 35:
            passed = False

    grade = calculate_grade(average)

    print("\n            STUDENT REPORT             ")
    print("Student Name:", student_name)

    for i in range(len(subjects)):
        print(subjects[i], ":", marks_list[i])

    
    print("Total Marks:", total, "/", len(subjects) * 100)
    print("Average:", round(average, 2))
    print("Grade:", grade)

    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    


main()