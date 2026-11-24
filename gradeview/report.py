"""Report classes: show a ClassRecord as text or as a chart.

Report is the parent class. TextReport and ChartReport inherit from it
and each override generate() in their own way (polymorphism).
"""


class Report:
    """Base class for all reports. Child classes must override generate()."""

    def __init__(self, record):
        """Create a report for a class record.

        Args:
            record (ClassRecord): The class record to report on.
        """
        self._record = record

    def generate(self):
        """Build the report. Child classes must override this method."""
        raise NotImplementedError("Child classes must override generate()")


class TextReport(Report):
    """A report printed as plain text."""

    def generate(self):
        """Print a text summary of the class and return it as a string."""
        record = self._record
        lines = [
            f"Class report: {record.get_course_name()}",
            f"Students: {len(record)}",
            f"Class average: {record.class_average()}",
            "",
            "Top students:",
        ]
        for rank, student in enumerate(record.top_students(), start=1):
            lines.append(f"  {rank}. {student.get_name()} - {student.average()} ({student.letter_grade()})")

        failing = record.failing_students()
        lines.append("")
        lines.append(f"Below passing ({record.PASSING_SCORE}): {len(failing)}")
        for student in failing:
            lines.append(f"  - {student.get_name()} - {student.average()}")

        text = "\n".join(lines)
        print(text)
        return text


class ChartReport(Report):
    """A report drawn as a bar chart of each student's average."""

    def generate(self, show=True):
        """Draw a bar chart of student averages with a passing line.

        Args:
            show (bool, optional): Open the chart window. Defaults to True.

        Returns:
            matplotlib.figure.Figure: The chart, so it can be saved.
        """
        import matplotlib.pyplot as plt

        students = self._record.get_students()
        names = [student.get_name() for student in students]
        averages = [student.average() for student in students]

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(names, averages, color="#4C72B0")
        ax.axhline(self._record.PASSING_SCORE, color="#C44E52", linestyle="--", label="Passing")
        ax.set_title(f"Student averages: {self._record.get_course_name()}")
        ax.set_ylabel("Average score")
        ax.set_ylim(0, 100)
        ax.legend()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        fig.tight_layout()

        if show:
            plt.show()
        return fig
