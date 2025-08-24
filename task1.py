students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88,
    "Vikram": 95
}
name = input("Enter the student's name: ")
if name in students:
    print("{}'s marks: {}".format (name, students[name]))
else:
    print("Sorry, '{}' is not found in the student records.".format(name))

