"""Report classes: show a ClassRecord as text or as a chart.

Report is the parent class. TextReport and ChartReport inherit from it,
and each one changes generate() in its own way (polymorphism).
"""

import matplotlib.pyplot as plt


class Report:
    """The parent class for all reports."""

    def __init__(self, record):
        """Create a report for a class record.

        Args:
            record (ClassRecord): The class record to report on.
        """
        self._record = record

    def generate(self):
        """Make the report. Each child class writes its own version."""
        print("This is a general report. Use TextReport or ChartReport.")


class TextReport(Report):
    """A report printed as text."""

    def generate(self):
        """Print a summary of the class."""
        record = self._record
        print("Class report:", record.get_course_name())
        print("Students:", len(record))
        print("Class average:", record.class_average())

        print()
        print("Top students:")
        rank = 1
        for student in record.top_students():
            print(f"  {rank}. {student.get_name()} - {student.average()} ({student.letter_grade()})")
            rank = rank + 1

        print()
        failing = record.failing_students()
        print(f"Below passing ({record.PASSING_SCORE}):", len(failing))
        for student in failing:
            print(f"  - {student.get_name()} - {student.average()}")


class ChartReport(Report):
    """A report shown as a bar chart."""

    def generate(self):
        """Draw a bar chart of each student's average."""
        names = []
        averages = []
        for student in self._record.get_students():
            names.append(student.get_name())
            averages.append(student.average())

        plt.bar(names, averages)
        plt.axhline(self._record.PASSING_SCORE, color="red", linestyle="--", label="Passing")
        plt.title("Student averages")
        plt.ylabel("Average score")
        plt.ylim(0, 100)
        plt.legend()
        plt.show()
