"""The ClassRecord class: a group of students (composition)."""

import csv

from .student import Student


class ClassRecord:
    """A class record that holds many Student objects.

    This is composition: a ClassRecord is made up of Students.
    """

    PASSING_SCORE = 75

    def __init__(self, course_name):
        """Create an empty class record.

        Args:
            course_name (str): The name of the course, e.g. "DS212".
        """
        self._course_name = course_name
        self._students = []

    @classmethod
    def from_csv(cls, path, course_name="Untitled course"):
        """Create a ClassRecord from a CSV file.

        Column 1 is the name, column 2 is the student ID,
        and every column after that is a score.

        Args:
            path (str): Path to the CSV file.
            course_name (str, optional): The name of the course.

        Returns:
            ClassRecord: A record filled with the students from the file.
        """
        record = cls(course_name)
        with open(path) as file:
            reader = csv.reader(file)
            next(reader)  # skip the header row
            for row in reader:
                name = row[0]
                student_id = row[1]
                scores = []
                for value in row[2:]:
                    if value != "":
                        scores.append(value)
                record.add_student(Student(name, student_id, scores))
        return record

    def get_course_name(self):
        """Return the course name."""
        return self._course_name

    def get_students(self):
        """Return the list of students."""
        return self._students

    def add_student(self, student):
        """Add a student to the record.

        Args:
            student (Student): The student to add.

        Raises:
            ValueError: If a student with the same ID is already in the record.
        """
        if student in self._students:
            raise ValueError("This student is already in the record")
        self._students.append(student)

    def class_average(self):
        """Return the average of all the students' averages."""
        if len(self._students) == 0:
            return 0
        total = 0
        for student in self._students:
            total = total + student.average()
        return round(total / len(self._students), 2)

    def top_students(self, n=3):
        """Return the n students with the highest averages.

        Args:
            n (int, optional): How many students to return. Defaults to 3.
        """
        ranked = sorted(self._students, reverse=True)
        return ranked[:n]

    def failing_students(self):
        """Return the students whose average is below the passing score."""
        failing = []
        for student in self._students:
            if student.average() < self.PASSING_SCORE:
                failing.append(student)
        return failing

    def __len__(self):
        """Return the number of students, so len(record) works."""
        return len(self._students)

    def __repr__(self):
        """Return how the class record looks when printed."""
        return f"ClassRecord('{self._course_name}', students={len(self)})"
