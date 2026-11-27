# gradeviep

A Python library for analyzing student grades. Load a class record from a CSV file, then get averages, letter grades, top students, students below passing, and a bar chart.

Built for the DS212 Object-Oriented Programming final project (DS2B-G5).

## Installation

Coming soon on PyPI:

```bash
pip install gradeview
```

## Quick start

```python
from gradeview import ClassRecord, TextReport, ChartReport

record = ClassRecord.from_csv("sample_scores.csv", "DS212")

print(record.class_average())     # average of the whole class
print(record.top_students(3))     # the 3 highest averages
print(record.failing_students())  # students below 75

TextReport(record).generate()     # prints a summary
ChartReport(record).generate()    # draws a bar chart
```

The CSV needs a `name` column and a `student_id` column. Every other column is treated as a score from 0 to 100.

## Sample data

`sample_scores.csv` contains real, anonymized grades of the first 20 students in the Mathematics class of the UCI Student Performance dataset. The original grades use Portugal's 0–20 scale, so we multiplied them by 5 to get scores from 0 to 100. The columns `period1`, `period2` and `final` are the first-period, second-period and final grades (G1, G2 and G3 in the original data). The students had no names in the dataset, so they are labeled Student 01 to Student 20.

Note: in Portugal the passing grade is 10 out of 20 (50 out of 100), while gradeview uses 75 by default, so most of these students show up as below passing.

Source: Cortez, P. (2008). *Student Performance* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T (licensed under CC BY 4.0).

## Class diagram

```mermaid
classDiagram
  class Student {
    -_name : str
    -_student_id : str
    -_scores : list
    +get_name() str
    +get_scores() list
    +add_score(score)
    +average() float
    +letter_grade() str
    +__repr__() str
    +__eq__(other) bool
    +__lt__(other) bool
  }
  class ClassRecord {
    -_course_name : str
    -_students : list
    +from_csv(path)$ ClassRecord
    +add_student(student)
    +class_average() float
    +top_students(n) list
    +failing_students() list
    +__len__() int
  }
  class Report {
    #_record : ClassRecord
    +generate()
  }
  class TextReport {
    +generate()
  }
  class ChartReport {
    +generate()
  }
  ClassRecord "1" *-- "many" Student : contains
  Report o-- ClassRecord : uses
  Report <|-- TextReport
  Report <|-- ChartReport
```

## OOP concepts used

| Concept | Where |
|---|---|
| Encapsulation | `Student` and `ClassRecord` keep their data private (`_scores`, `_students`) behind getter methods |
| Inheritance | `TextReport` and `ChartReport` inherit from `Report` |
| Polymorphism | Each report overrides `generate()` in its own way |
| Dunder methods | `__repr__`, `__eq__`, `__lt__`, `__len__` |
| Composition | A `ClassRecord` contains many `Student` objects |

## Contributors

DS2B-G5:

- Abragan, Ira Marie
- Añabieza, Shaira Marqueza
- Catanus, Baby Grace
- Fiola, Hopelyn Grace
- Lauzon, Angel Janelle

## License

MIT
