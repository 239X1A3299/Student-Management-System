"""
Simple Student Management System
Beginner-friendly, menu-driven console app using file storage (students.txt).

Features:
1. Add student
2. View all students
3. Search student by name
4. Delete student

Data storage format (students.txt): one student per line, fields separated by | (pipe):
name|age|student_id

Run: python main.py
"""

import os

DATA_FILE = "students.txt"


def load_students():
    """Read students from DATA_FILE and return a list of student dicts."""
    students = []
    if not os.path.exists(DATA_FILE):
        return students

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                # skip malformed lines
                continue
            name, age, sid = parts
            students.append({"name": name, "age": age, "id": sid})
    return students


def save_students(students):
    """Write list of student dicts to DATA_FILE."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for s in students:
            line = f"{s['name']}|{s['age']}|{s['id']}\n"
            f.write(line)


def add_student():
    """Prompt user for student details and save to file."""
    print("\nAdd New Student")
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    age = input("Enter age: ").strip()
    sid = input("Enter student ID: ").strip()
    if not sid:
        print("Student ID cannot be empty.")
        return

    students = load_students()
    # check for duplicate ID
    for s in students:
        if s["id"] == sid:
            print("A student with this ID already exists.")
            return

    students.append({"name": name, "age": age, "id": sid})
    save_students(students)
    print("Student added successfully.")


def view_students():
    """Display all students in a readable table."""
    students = load_students()
    if not students:
        print("\nNo students found.")
        return

    print("\nAll Students:")
    print("{:<25} {:<6} {:<10}".format("Name", "Age", "ID"))
    print("-" * 45)
    for s in students:
        print("{:<25} {:<6} {:<10}".format(s["name"], s["age"], s["id"]))


def search_student():
    """Search students by name (case-insensitive, partial match)."""
    term = input("\nEnter name to search: ").strip().lower()
    if not term:
        print("Search term cannot be empty.")
        return

    students = load_students()
    matches = [s for s in students if term in s["name"].lower()]
    if not matches:
        print("No matching students found.")
        return

    print(f"\nFound {len(matches)} match(es):")
    for s in matches:
        print("- {} (Age: {}, ID: {})".format(s["name"], s["age"], s["id"]))


def delete_student():
    """Delete a student by student ID."""
    sid = input("\nEnter student ID to delete: ").strip()
    if not sid:
        print("Student ID cannot be empty.")
        return

    students = load_students()
    remaining = [s for s in students if s["id"] != sid]
    if len(remaining) == len(students):
        print("No student found with that ID.")
        return

    save_students(remaining)
    print("Student deleted successfully.")


def main_menu():
    """Show menu and handle user choices."""
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by name")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()
