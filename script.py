"""Interactive student result analyzer.

The GPA uses a 5-point scale: A=5, B=4, C=3, D=2, E=1, F=0.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path


GRADE_POINTS = {
	"A": 5.0,
	"B": 4.0,
	"C": 3.0,
	"D": 2.0,
	"E": 1.0,
	"F": 0.0,
}


@dataclass
class CourseResult:
	code: str
	score: float
	unit: int

	@property
	def grade(self) -> str:
		if self.score >= 70:
			return "A"
		if self.score >= 60:
			return "B"
		if self.score >= 50:
			return "C"
		if self.score >= 45:
			return "D"
		if self.score >= 40:
			return "E"
		return "F"


@dataclass
class StudentResult:
	name: str
	courses: list[CourseResult] = field(default_factory=list)

	def add_course(self, code: str, score: float, unit: int) -> None:
		normalized_code = code.strip().upper()
		if not normalized_code:
			raise ValueError("Course code cannot be empty.")
		if not 0 <= score <= 100:
			raise ValueError("Score must be between 0 and 100.")
		if unit <= 0:
			raise ValueError("Unit must be greater than zero.")
		if any(course.code == normalized_code for course in self.courses):
			raise ValueError(f"{normalized_code} has already been added.")
		self.courses.append(CourseResult(normalized_code, score, unit))

	@property
	def total_units(self) -> int:
		return sum(course.unit for course in self.courses)

	@property
	def semester_average(self) -> float:
		if not self.courses:
			return 0.0
		return sum(course.score * course.unit for course in self.courses) / self.total_units

	@property
	def gpa(self) -> float:
		if not self.courses:
			return 0.0
		quality_points = sum(
			GRADE_POINTS[course.grade] * course.unit for course in self.courses
		)
		return quality_points / self.total_units

	def strongest_course(self) -> CourseResult | None:
		return max(self.courses, key=lambda course: course.score, default=None)

	def weakest_course(self) -> CourseResult | None:
		return min(self.courses, key=lambda course: course.score, default=None)

	def export_csv(self, filename: str | Path) -> Path:
		output_path = Path(filename)
		with output_path.open("w", newline="", encoding="utf-8") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(["Student", self.name])
			writer.writerow(["Course", "Score", "Grade", "Unit"])
			for course in self.courses:
				writer.writerow([course.code, f"{course.score:g}", course.grade, course.unit])
			writer.writerow([])
			writer.writerow(["Semester average", f"{self.semester_average:.2f}"])
			writer.writerow(["GPA", f"{self.gpa:.2f}"])
		return output_path

	def display(self) -> None:
		print(f"\nStudent: {self.name}")
		if not self.courses:
			print("No courses added yet.")
			return
		print(f"{'Course':<12}{'Score':>8}{'Grade':>8}{'Unit':>8}")
		print("-" * 36)
		for course in self.courses:
			print(f"{course.code:<12}{course.score:>8.2f}{course.grade:>8}{course.unit:>8}")
		strongest = self.strongest_course()
		weakest = self.weakest_course()
		print(f"\nGPA: {self.gpa:.2f}")
		print(f"Semester average: {self.semester_average:.2f}")
		print(f"Strongest course: {strongest.code} ({strongest.score:g})")
		print(f"Weakest course: {weakest.code} ({weakest.score:g})")


def read_number(prompt: str, number_type: type[int] | type[float]) -> int | float:
	while True:
		try:
			return number_type(input(prompt).strip())
		except ValueError:
			print("Please enter a valid number.")


def create_student() -> StudentResult:
	while True:
		name = input("Student name: ").strip()
		if name:
			return StudentResult(name)
		print("Student name cannot be empty.")


def run_cli() -> None:
	print("Student Result Analyzer")
	student = create_student()

	while True:
		print(
			"\n1. Add course\n"
			"2. Show result\n"
			"3. Export result to CSV\n"
			"4. Change student\n"
			"5. Exit"
		)
		choice = input("Choose an option: ").strip()

		if choice == "1":
			code = input("Course code: ")
			score = read_number("Score (0-100): ", float)
			unit = read_number("Unit: ", int)
			try:
				student.add_course(code, score, unit)
				print("Course added.")
			except ValueError as error:
				print(f"Error: {error}")
		elif choice == "2":
			student.display()
		elif choice == "3":
			filename = input("CSV filename [student_result.csv]: ").strip()
			output_path = student.export_csv(filename or "student_result.csv")
			print(f"Result exported to {output_path.resolve()}")
		elif choice == "4":
			student = create_student()
		elif choice == "5":
			print("Goodbye.")
			return
		else:
			print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
	run_cli()
