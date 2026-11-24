"""The Student class: one student and their scores."""


class Student:
    """A student with a name, an ID number and a list of scores.

    The attributes start with an underscore, which means they are private
    (encapsulation). Use the get methods to read them.
    """

    def __init__(self, name, student_id, scores=None):
        """Create a student.

        Args:
            name (str): The student's full name.
            student_id (str): The student's ID number.
            scores (list, optional): Starting scores from 0 to 100.
        """
        self._name = name
        self._student_id = student_id
        self._scores = []
        if scores is not None:
            for score in scores:
                self.add_score(score)

    def get_name(self):
        """Return the student's name."""
        return self._name

    def get_student_id(self):
        """Return the student's ID number."""
        return self._student_id

    def get_scores(self):
        """Return the student's scores."""
        return self._scores

    def add_score(self, score):
        """Add one score from 0 to 100.

        Args:
            score (float): The score to add.

        Raises:
            ValueError: If the score is below 0 or above 100.
        """
        score = float(score)
        if score < 0 or score > 100:
            raise ValueError("Score must be from 0 to 100")
        self._scores.append(score)

    def average(self):
        """Return the student's average score, or 0 if there are no scores."""
        if len(self._scores) == 0:
            return 0
        total = sum(self._scores)
        return round(total / len(self._scores), 2)

    def letter_grade(self):
        """Return a letter grade from A to F based on the average."""
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 85:
            return "B"
        elif avg >= 80:
            return "C"
        elif avg >= 75:
            return "D"
        else:
            return "F"

    def __repr__(self):
        """Return how the student looks when printed."""
        return f"Student('{self._name}', average={self.average()})"

    def __eq__(self, other):
        """Two students are equal if they have the same ID number."""
        return self._student_id == other._student_id

    def __lt__(self, other):
        """A student is 'less than' another if their average is lower."""
        return self.average() < other.average()
