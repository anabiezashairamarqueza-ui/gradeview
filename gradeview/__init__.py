"""gradeview: a simple library for analyzing student grades.

Example:
    >>> from gradeview import ClassRecord, TextReport
    >>> record = ClassRecord.from_csv("scores.csv", "DS212")
    >>> TextReport(record).generate()
"""

from .student import Student
from .class_record import ClassRecord
from .report import Report, TextReport, ChartReport

__version__ = "0.1.0"
__all__ = ["Student", "ClassRecord", "Report", "TextReport", "ChartReport"]
