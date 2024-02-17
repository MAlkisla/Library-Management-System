import os

class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    # Lists all books in the library.
    def list_books(self):
        with open(self.file_path, "r") as file:
            books = file.readlines()
            if not books:
                print("The book list is empty. If you want to add a book, go to Add book (2) in the menu.")
                return
            print("Listing books:")
            for book_info in books:
                book_data = book_info.strip().split(",")
                if len(book_data) >= 2:
                    title, author = book_data[:2]
                    print(f"- Title: {title}, Author: {author}")
                else:
                    print("Invalid book information:", book_info)

    # Adds a new book to the library.
    def add_book(self):
        
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        while True:
            try:
                release_year = int(input("Enter release year: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")
        while True:
            try:
                pages = int(input("Enter number of pages: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of pages.")

        book_info = f"{title},{author},{release_year},{pages}\n"
        with open(self.file_path, "a") as self.file:
            self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    # Removes a book from the library.
    def remove_book(self):
        title = input("Enter title of the book to remove: ")
        found_books = []
        with open(self.file_path, "r") as file:
            for book_info in file.readlines():
                book = book_info.strip().split(",")
                if book[0] == title:
                    found_books.append(book)

        if not found_books:
            print(f"Book '{title}' not found. Please check the book title.")
            return

        if len(found_books) == 1:
            book = found_books[0]
            confirm = input(f"Are you sure you want to remove '{book[0]}' by {book[1]}? (y/n): ").lower()
            if confirm == "y":
                self._remove_book_from_file(title)
                print(f"Book '{title}' removed successfully.")
            elif confirm == "n":
                print("Removal canceled.")
            else:
                print("Invalid choice. Removal canceled.")
        else:
            print(f"Multiple books found with title '{title}'. Please select which one to remove:")
            for index, book in enumerate(found_books, start=1):
                print(f"{index} - '{book[0]}' by {book[1]}")
            while True:
                try:
                    choice_index = int(input("Enter the index of the book you want to remove: "))
                    if 1 <= choice_index <= len(found_books):
                        book = found_books[choice_index - 1]
                        confirm = input(f"Are you sure you want to remove '{book[0]}' by {book[1]}? (y/n): ").lower()
                        if confirm == "y":
                            self._remove_book_from_file(book[0])
                            print(f"Book '{book[0]}' removed successfully.")
                        elif confirm == "n":
                            print("Removal canceled.")
                        else:
                            print("Invalid choice. Removal canceled.")
                        break
                    else:
                        print("Invalid index. Please enter a valid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid index.")

    # Removes a book from the file.
    def _remove_book_from_file(self, title):
        books_to_keep = []
        with open(self.file_path, "r") as file:
            for line in file:
                if not line.strip().split(",")[0] == title:
                    books_to_keep.append(line)

        with open(self.file_path, "w") as file:
            for book in books_to_keep:
                file.write(book)

def main():
    lib = Library()
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice.lower() == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()