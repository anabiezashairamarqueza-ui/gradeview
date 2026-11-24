"""The Student class: one student and their scores."""


class Student:
    """A single student with a name, an ID number and a list of scores.

    The attributes are private (encapsulation). Read them through the
    getter methods instead of touching them directly.
    """

    def __init__(self, name, student_id, scores=None):
        """Create a student.

        Args:
            name (str): The student's full name.
            student_id (str): The student's ID number.
            scores (list, optional): Starting scores from 0 to 100.
        """
        self._name = name
        self._student_id = str(student_id)
        self._scores = []
        for score in scores or []:
            self.add_score(score)

    def get_name(self):
        """Return the student's name."""
        return self._name

    def get_student_id(self):
        """Return the student's ID number."""
        return self._student_id

    def get_scores(self):
        """Return a copy of the student's scores, so the original stays safe."""
        return list(self._scores)

    def add_score(self, score):
        """Add one score from 0 to 100.

        Args:
            score (float): The score to add.

        Raises:
            ValueError: If the score is below 0 or above 100.
        """
        score = float(score)
        if not 0 <= score <= 100:
            raise ValueError(f"Score must be from 0 to 100, got {score}")
        self._scores.append(score)

    def average(self):
        """Return the student's average score, or 0.0 if there are no scores."""
        if not self._scores:
            return 0.0
        return round(sum(self._scores) / len(self._scores), 2)

    def letter_grade(self):
        """Return a letter grade from A to F based on the average."""
        avg = self.average()
        if avg >= 90:
            return "A"
        if avg >= 85:
            return "B"
        if avg >= 80:
            return "C"
        if avg >= 75:
            return "D"
        return "F"

    def __repr__(self):
        """Return a readable description, e.g. Student('Ana', avg=91.5)."""
        return f"Student({self._name!r}, avg={self.average()})"

    def __eq__(self, other):
        """Two students are equal if they have the same ID number."""
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id

    def __hash__(self):
        """Hash by ID number so students can be used in sets and dicts."""
        return hash(self._student_id)

    def __lt__(self, other):
        """Compare students by average, so sorted() ranks them."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average() < other.average()
