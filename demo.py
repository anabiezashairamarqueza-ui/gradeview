
"""Demo and testing of the gradeview library."""

from gradeview import ClassRecord, TextReport, ChartReport


def main():
    # 1. Load the sample student records
    print("=" * 45)
    print("       GRADEVIEW - STUDENT GRADE ANALYSIS")
    print("=" * 45)

    record = ClassRecord.from_csv("sample_scores.csv", "DS212")

    # 2. Display all student records
    print("\n[1] STUDENT RECORDS")
    print(record)

    # 3. Display the class average
    print("\n[2] CLASS AVERAGE")
    print(f"Class Average: {record.class_average():.2f}")

    # 4. Display the top 3 students
    print("\n[3] TOP 3 STUDENTS")
    top = record.top_students(3)

    for student in top:
        print(student)

    # 5. Display students below the passing grade
    print("\n[4] STUDENTS BELOW PASSING")
    failing = record.failing_students()

    if failing:
        for student in failing:
            print(student)
    else:
        print("No students below passing.")

    # 6. Display the highest-ranked student's grades
    print("\n[5] TOP STUDENT GRADE DETAILS")

    if top:
        best_student = top[0]
        print("Student:", best_student.get_name())
        print("Letter Grade:", best_student.letter_grade())
        print("Philippine Grade:", best_student.ph_grade())

    # 7. Generate the text report
    print("\n[6] TEXT REPORT")
    TextReport(record).generate()

    # 8. Generate the bar chart
    print("\n[7] CHART REPORT")
    ChartReport(record).generate()

    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()
