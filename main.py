
# Student Performance Tracker
# Project by: Mohd Kaif
# Intern ID: CITS9935
# Duration: 4 Weeks

import json
import os
import matplotlib.pyplot as plt
# File to store student records
DATA_FILE = "students.json"

# Load saved student data
def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save student data permanently
def save_students():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

# Calculate student grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Add a new student
def add_student():
    name = input("Enter student name: ")

    try:
        marks = float(input("Enter marks out of 100: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter between 0 and 100.")
        return

    students.append({
        "name": name,
        "marks": marks
    })

    save_students()
    print("Student added and saved successfully!")

# Display all student reports
def show_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Performance Report ---")

    for student in students:
        marks = student["marks"]
        grade = calculate_grade(marks)

        print(f"Name: {student['name']}")
        print(f"Marks: {marks}/100")
        print(f"Percentage: {marks}%")
        print(f"Grade: {grade}")
        print("------------------------")

# Find the topper
def show_topper():
    if not students:
        print("No student records found.")
        return

    topper = max(students, key=lambda s: s["marks"])

    print(f"Topper: {topper['name']}")
    print(f"Marks: {topper['marks']}/100")
# Display student performance graph
def show_graph():
    if not students:
        print("No student records available for graph.")
        return

    names = [student["name"] for student in students]
    marks = [student["marks"] for student in students]

    plt.figure(figsize=(8, 5))
    plt.bar(names, marks)
    plt.title("Student Performance Tracker")
    plt.xlabel("Student Names")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()
# Main menu
while True:
    print("\n===== STUDENT PERFORMANCE TRACKER =====")
    print("1. Add Student")
    print("2. Show Student Reports")
    print("3. Show Topper")
    print("4. Show Performance Graph")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        show_topper()
    elif choice == "4":
        show_graph()
    elif choice == "5":
        print("Thank you for using Student Performance Tracker!")
        break
    else:
        print("Invalid choice! Please try again.")
   