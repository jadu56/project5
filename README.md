# Task-1 Create a Dictionary of Student Marks

## Description
This is a simple Python program that stores student names and their marks in a dictionary.  
The user can enter a student's name, and the program will display their marks if the name exists in the records.  
If the student’s name is not found, an appropriate message is shown.

---

## Code
```python
# ---Create a Dictionary of Student Marks---
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88,
    "Vikram": 95
}

name = input("Enter the student's name: ")
if name in students:
    print("{}'s marks: {}".format(name, students[name]))
else:
    print("Sorry, '{}' is not found in the student records.".format(name))
