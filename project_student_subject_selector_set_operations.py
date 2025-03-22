# Student Subject Selector

# Tuple of available subjects (fixed and immutable)
available_subjects = ("Math", "Science", "History", "English", "Computer Science", "Physics", "Chemistry")

# Dictionary to store each student's selected subjects as sets
student_choices = {}

def display_menu():
    print("\nStudent Subject Selector")
    print("1. View Available Subjects")
    print("2. Select Subjects for a Student")
    print("3. Show Subjects of a Student")
    print("4. Find Common Subjects Between Two Students")
    print("5. Show All Unique Selected Subjects")
    print("6. Show Subjects Chosen by One Student but Not Another")
    print("7. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("\nAvailable Subjects:")
        for subject in available_subjects:
            print("-", subject)

    elif choice == "2":
        student = input("Enter student name: ")
        subjects = input("Enter subjects (comma-separated): ").split(",")
      
        subjects = {s.strip() for s in subjects}  # set comprehension! Convert to set and remove extra spaces

        # traditional way of doing the same thing
        # cleaned_subjects = set()  # Initialize an empty set

        # for s in subjects:
            # cleaned_subjects.add(s.strip())  # Remove spaces and add to the set

        # subjects = cleaned_subjects  # Assign back to the original variable

        
        # Validate subjects
        if subjects.issubset(available_subjects):
            student_choices[student] = subjects
            print(f"Subjects selected for {student}.")
        else:
            print("Invalid subjects entered! Please select only from available subjects.")

    elif choice == "3":
        student = input("Enter student name: ")
        if student in student_choices:
            print(f"\n{student}'s Subjects:")
            for subject in student_choices[student]:
                print("-", subject)
        else:
            print(f"{student} has not selected any subjects yet!")

    elif choice == "4":
        student1 = input("Enter first student name: ")
        student2 = input("Enter second student name: ")
        
        if student1 in student_choices and student2 in student_choices:
            common_subjects = student_choices[student1] & student_choices[student2]  # Intersection
            if common_subjects:
                print(f"\nCommon Subjects between {student1} and {student2}:")
                for subject in common_subjects:
                    print("-", subject)
            else:
                print("No common subjects found.")
        else:
            print("One or both students have not selected subjects.")

    elif choice == "5":
        unique_subjects = set().union(*student_choices.values())  # Union of all selected subjects
        if unique_subjects:
            print("\nAll Unique Selected Subjects:")
            for subject in unique_subjects:
                print("-", subject)
        else:
            print("No subjects have been selected yet!")

    elif choice == "6":
        student1 = input("Enter first student name: ")
        student2 = input("Enter second student name: ")

        if student1 in student_choices and student2 in student_choices:
            difference = student_choices[student1] - student_choices[student2]  # Difference
            if difference:
                print(f"\nSubjects chosen by {student1} but not {student2}:")
                for subject in difference:
                    print("-", subject)
            else:
                print(f"{student1} has no unique subjects compared to {student2}.")
        else:
            print("One or both students have not selected subjects.")

    elif choice == "7":
        print("Exiting Student Subject Selector. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
