subjects = ("Math","DSA","Economics","Digital Logic","Computer Graphics")
selected_subjects = {}

def display_menu():
    print("Welcome to subject selector application!")
    
    print("1. View Available Subjects")
    print("2. Select Subjects for a Student")
    print("3. Show Subjects of a Student")
    print("4. Find Common Subjects Between Two Students")
    print("5. Show All Unique Selected Subjects")
    print("6. Show Subjects Chosen by One Student but Not Another")
    print("7. Exit")

def display_subjects():
    if subjects:
        for subject in subjects:
            print(f"{subject}")

def store_selected_subject(student):
    subject = input("Choose a subject:")
    if subject not in subjects:
        print("Subject not available. Please try again!")
        return
    selected_subjects[student] = subject
    print("subject choice save successfully!")

def student_subjects(student):
    if student in selected_subjects:
        print(f"subjects selected by {student} are:\n")

        for idx,subject in enumerate(selected_subjects,1):
            print(f"{idx}."+ selected_subjects[student])
                        

def menu():
    display_menu()
    while True:
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            display_subjects()

        elif(choice == 2):
            student = input("Enter student's name: ")
            store_selected_subject(student);

        elif(choice == 3):
            student = input("Enter the name of the student: ")
            student_subjects(student)

        else:
            print("Invalid choice")


menu()
