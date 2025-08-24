# Task-1 Create a Dictionary of Student Marks

## Description
This is a simple Python program that stores student names and their marks in a dictionary.  
The user can enter a student's name, and the program will display their marks if the name exists in the records.  
If the student’s name is not found, an appropriate message is shown.

---
# Task-2 Demonstrate List Slicing 

##  Description
This Python program demonstrates:
1. Creating a list of numbers from **1 to 10**.  
2. Extracting the **first five numbers** from the list.  
3. Reversing the list using the `.reverse()` method.  

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


# ---Task-2 Demonstrate List Slicing ---
numbers = list(range(1, 11))

print("origianal numbers: ", numbers)

first_five = numbers[:5]

print("Extracted five numbers list:", first_five)

numbers.reverse()

print("Reversed list:", numbers)
