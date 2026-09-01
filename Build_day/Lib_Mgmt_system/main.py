import colorama
from colorama import Fore, Back, Style, init

def menu():
    init(autoreset=True)
    print(Fore.CYAN + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''')
    print(Fore.GREEN + '''1. Add Book
2. View Books
3. Search Book
4. Register User
5. Issue Book
6. Exit''')
    

def read_book():
    """This is a function to merely read contents iof a file  """

    with open("book_data.txt", "r") as f:
        book_data = f.readlines()
    return book_data
def view_book():
    book_data = read_book()
    #HomeWork

#docstring
def add_book():
    """This is a add book Function . It takes Book Id, Book Name, Author,Quantity as input """
    book_data = read_book()
    print(Fore.GREEN + "--- ADD BOOK ---" )
    book_name = input("Enter the Book name  :")
    for i in book_data:
        if book_name in i:
            print(Fore.GREEN + "The Book Already Exists")
            print(Fore.RED + "Terminating the function Please use Update Function")
            return 10
    book_id = len(book_data) + 1
    
    # while True:
    #     book_id = input("Enter Book Id  :").strip()
    #     if book_id.isdigit():
    #         book_id = int(book_id)
    #         break
    #     else:
    #         print(Fore.RED + "Invalid Book Id \n It should be a number only")   
    book_author = input("Enter author Name Please : ")
    print(Fore.GREEN + "Book Id is :: ", book_id)
    
    error_message = Fore.RED + "Invalid quantity entered \n Please Enter a valid Value"
    while True:
        book_quantity = input("Enter Quantity :").strip()
        if book_quantity.isdigit() :
            if int(book_quantity) > 0:
                book_quantity = int(book_quantity)
                break
            else:
                print(error_message)    
        else:
            print(error_message)
    print(Fore.GREEN + f'{"Book added successfully.":^100}')

    with  open("book_data.txt", "a") as f:
        f.write(f"{book_id}, {book_name}, {book_author}, {book_quantity} \n")
    




   

if __name__ == "__main__" :
    while True:
        menu()        
        choice = input("Enter your choice between 1 to 6 :: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            print("View Book")
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print(Fore.CYAN + "Thank You for using our System, Visit Again")
            break
        else:
            print(Fore.RED + "Invalid Choice")
