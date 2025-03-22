library_books = ['Cyber Security 101','Data Structure and Algorithm','Hacking Handbook']
borrowed_books = {}  # Dictionary to store borrowed books and users

def display_books():
    """Display available books in the library."""
    if library_books:
        print("\n Available Books:")
        for idx, book in enumerate(library_books, start=1):
            print(f"{idx}. {book}")
    else:
        print("\n No books available right now.")

  

def borrow_book(user):
    """Allow a user to borrow a book."""
    display_books()

    if not library_books:
        return

    choice = input("\nEnter the book name you want to borrow: ")
    
    if choice in library_books:
        library_books.remove(choice)
        borrowed_books[user] = choice
        print(f"\n '{choice}' has been borrowed by {user}.")
    else:
        print("\n Book not available or incorrect name entered.")


def return_book(user):
    """Allow a user to return a borrowed book."""
    if user in borrowed_books:
        book = borrowed_books.pop(user)
        library_books.append(book)
        print(f"\n '{book}' has been returned by {user}.")
    else:
        print("\n You have not borrowed any books.")
        

def main():
   while True:
        print("\n Welcome to the Library")
        print("1. View Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            user = input("\nEnter your name: ")
            borrow_book(user)
        elif choice == "3":
            user = input("\nEnter your name: ")
            return_book(user)
        elif choice == "4":
            print("\n Exiting Library System. Have a nice day!")
            break
        else:
            print("\n Invalid choice! Please select from 1-4.")



main()

