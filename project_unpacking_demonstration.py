# Student records stored as dictionaries
student1 = {"name": "Alice", "math": 85, "science": 90}
student2 = {"name": "Bob", "math": 78, "english": 88}
student3 = {"name": "Charlie", "science": 95, "history": 80}

# Merge all student data into one list
students = [student1, student2, student3]

# Function to display student report using dictionary unpacking
def display_report(**student):
    print(f"\nStudent Name: {student['name']}")
    subjects = {key: value for key, value in student.items() if key != 'name'}
    
    if subjects:
        avg_score = sum(subjects.values()) / len(subjects)
        print(f"Subjects: {', '.join(subjects.keys())}")
        print(f"Average Score: {avg_score:.2f}")
    else:
        print("No subjects found!")

# Process each student using `**`
for student in students:
    display_report(**student)

# Extract all subjects using `*` unpacking
all_subjects = set().union(*(s.keys() - {'name'} for s in students))
print("\nAll Subjects Offered:", all_subjects)
