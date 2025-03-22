lst = ['Fundamentals','Cyber Security','Python Fundamentals','Data Structure']
borrowed_books = {}


def display_books():
    print("Available Books")
    for i,value in enumerate(lst,1):
        print(f"{i}. ",value)

def borrow_book(user):
    selected_book = input("Please Enter Book Name: ")

    if selected_book not in lst:
        print("Book Not Found")
        return
       
   
    lst.remove(selected_book)
    borrowed_books[user] = selected_book
    print(f"The book -->{selected_book} borrowed by user --> ", user)


def return_book(user):
    if user not in borrowed_books:
        print("Borrower Not Found")
        return
    returned_book = borrowed_books.pop(user)
    lst.append(returned_book)


def main():
    print("*****Welcome to Library Management System*****")
    #display_books()
    while True:
        print("\n")
        print("===========================")
        print("1. Dispaly Available Books")
        print("2. Borrow Book")
        print("3. Return Borrowed Book")
        print("4. Exit program")
        choice = int(input("Select an option: "))
        if(choice == 1):
            display_books()
        elif(choice == 2):
            user = input("Please Enter Your Name: ")
            borrow_book(user)
        elif(choice == 3):
            user = input("Please Enter Borrower's name: ")
            return_book(user)
        elif(choice == 4):
            break
        else:
            print("Invalid input")


            
   
    
    
main()






