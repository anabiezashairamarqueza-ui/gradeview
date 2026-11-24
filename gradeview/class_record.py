"""The ClassRecord class: a group of students (composition)."""

import csv

from .student import Student


class ClassRecord:
    """A class record that contains many Student objects.

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
        """Build a ClassRecord from a CSV file.

        The CSV needs a "name" column and a "student_id" column.
        Every other column is treated as a score.

        Args:
            path (str): Path to the CSV file.
            course_name (str, optional): The name of the course.

        Returns:
            ClassRecord: A record filled with the students from the file.
        """
        record = cls(course_name)
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                name = row.pop("name")
                student_id = row.pop("student_id")
                scores = [value for value in row.values() if value not in ("", None)]
                record.add_student(Student(name, student_id, scores))
        return record

    def get_course_name(self):
        """Return the course name."""
        return self._course_name

    def get_students(self):
        """Return a copy of the list of students."""
        return list(self._students)

    def add_student(self, student):
        """Add a student to the record.

        Args:
            student (Student): The student to add.

        Raises:
            TypeError: If the object is not a Student.
            ValueError: If a student with the same ID is already in the record.
        """
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added")
        if student in self._students:
            raise ValueError(f"Student {student.get_student_id()} is already in the record")
        self._students.append(student)

    def class_average(self):
        """Return the average of all students' averages, or 0.0 if empty."""
        if not self._students:
            return 0.0
        total = sum(student.average() for student in self._students)
        return round(total / len(self._students), 2)

    def top_students(self, n=3):
        """Return the n students with the highest averages.

        Args:
            n (int, optional): How many students to return. Defaults to 3.
        """
        return sorted(self._students, reverse=True)[:n]

    def failing_students(self):
        """Return the students whose average is below the passing score."""
        return [s for s in self._students if s.average() < self.PASSING_SCORE]

    def __len__(self):
        """Return the number of students, so len(record) works."""
        return len(self._students)

    def __repr__(self):
        """Return a readable description of the record."""
        return f"ClassRecord({self._course_name!r}, students={len(self)})"
