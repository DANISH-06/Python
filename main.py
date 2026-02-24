from functools import reduce
import pandas as pd


class Student:
    def __init__(self, name, student_id, courses, grades):
        self.name = name
        self.id = student_id
        self.courses = courses
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def predict_performance(self):
        avg = self.average_grade()
        if avg >= 70:
            return "High"
        elif avg >= 50:
            return "Medium"
        else:
            return "Low"


students = [
    Student("Alice", "S001", ["Math", "CS", "Physics"], [75, 82, 68]),
    Student("Bob", "S002", ["Math", "History"], [45, 55]),
    Student("Charlie", "S003", ["CS", "Physics"], [90, 88])
]

averages = list(map(lambda s: (s.name, s.average_grade()), students))
high_performers = list(filter(lambda s: s.average_grade() >= 70, students))
overall_avg = reduce(lambda acc, s: acc + s.average_grade(), students, 0) / len(students)

data = {
    "Name": [s.name for s in students],
    "Average Grade": [s.average_grade() for s in students],
    "Performance": [s.predict_performance() for s in students]
}

df = pd.DataFrame(data)

print("Student Averages:")
for name, avg in averages:
    print(f"{name}: {avg:.2f}")

print("\nHigh Performers:")
for s in high_performers:
    print(s.name)

print(f"\nOverall Average Grade: {overall_avg:.2f}")

print("\nPandas DataFrame:")
print(df)