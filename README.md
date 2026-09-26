# Student Result Analyzer

This project is a simple Python-based command-line application for tracking and analyzing a student's academic performance. It allows a user to enter course codes, scores, and credit units, then calculates important academic results such as the semester average, GPA, strongest course, and weakest course.

## What the app does

The program lets you:

- Add multiple courses for a student
- Validate each score and unit before saving
- Calculate grade equivalents for each course
- Compute the semester average using weighted scores
- Calculate GPA using the standard grade-point scale:
  - A = 5
  - B = 4
  - C = 3
  - D = 2
  - E = 1
  - F = 0
- Identify the strongest and weakest courses
- Display the results in the terminal
- Export the student's results as a CSV file
- Change the student profile while using the app

## Grade system

The application uses this grading rule:

- 70 and above = A
- 60 to 69 = B
- 50 to 59 = C
- 45 to 49 = D
- 40 to 44 = E
- Below 40 = F

## How to run

Make sure Python is installed, then run:

```bash
python script.py
```

## Menu options

When the program starts, it shows a menu with these options:

1. Add course
2. Show result
3. Export result to CSV
4. Change student
5. Exit

## Example use case

A student can enter courses such as:

- MAT101 - 78 - 3 units
- ENG102 - 65 - 2 units
- PHY201 - 52 - 4 units

The app then calculates the weighted semester average, GPA, and highlights the best and weakest results.

## Project purpose

This project is useful for managing student academic records in a lightweight, easy-to-use interface without needing a database or web app. It is ideal for learning basic Python logic, input validation, calculations, and CSV export.
