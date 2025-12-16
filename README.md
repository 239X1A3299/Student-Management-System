# Student Management System (Python)

Simple, beginner-friendly Student Management System implemented in Python. Suitable for school or college projects and demonstrations of basic file handling, lists, loops, and functions.

Features
- Add student (name, age, ID)
- View all students
- Search student by name (partial, case-insensitive)
- Delete student by ID

Project structure
- main.py
- students.txt (data file - created automatically)
- README.md

How data is stored
- Each student is stored on one line in `students.txt` in the format: `name|age|student_id`.

How to run
1. Make sure you have Python 3 installed.
2. Open a terminal in this project folder.
3. Run:

```bash
python main.py
```

Short explanation
- The program uses simple functions to load and save students from `students.txt`.
- `load_students()` reads the file and returns a list of student dictionaries.
- `save_students()` writes the list back to the file.
- The `main_menu()` function shows a menu and calls small functions for add/view/search/delete.

Notes for submission
- The code is commented and keeps logic simple for learning and grading.
- You can open `students.txt` in a text editor to see stored students.

Enjoy! Modify fields or add validation as an exercise.
