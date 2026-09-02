import colorama
from colorama import Fore, Back, Style, init
from datetime import datetime
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
              
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
    
#Initialization

def read_book():
    """This is a function to merely read contents iof a file  """
    try:
        with open("book_data.txt", "r") as f:
            book_data = f.readlines()
        return book_data
        
    except FileNotFoundError:    
        book_data = []
        return book_data



def view_book():
    book_data = read_book()    
    if len(book_data) == 0:
        print(Fore.RED + "There is no Book in DataBase to View")
    else:
        for i in book_data:
            i = i.replace("\n", "")
            i = i.split()
            print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")

def search_book(param):
    book_data = read_book() 
    if len(book_data) == 0:
       print(Fore.RED + "There is no Book in DataBase to Search")
    else:
       for i in book_data:
            i = i.replace("\n", "")
            i = i.split()
            if param.isdigit():
                # print(f"{i[0]} --> {type(i[0])}")
                # print(param, type(param))
                if i[0] == param + ",":
                   print("\n\n")
                   print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
                   return i
            else:
                if i[1].lower() == param.lower() + ",":
                    print("\n\n")
                    print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
                    return i




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
    
def issue_book():
    user_id = input("Enter a user id ")
    #User Exists or NOt Homework 
    val = input("Enter either a book id or a Book name :: ")
    book_details = search_book(val)
    quantity = input("Enter Quantity :: ")
    print(f"For the User {user_id} book {book_details[1]} has been issued on {datetime.now().strftime("%d-%m-%Y")}")


if __name__ == "__main__" :
    while True:
        menu() 
        clear_screen()       
        choice = input("Enter your choice between 1 to 6 :: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_book()
        elif choice == "3":
            val = input("Enter either a book id or a Book name :: ")
            search_book(val)
        elif choice == "4":
            pass
        elif choice == "5":
            issue_book()
        elif choice == "6":
            print(Fore.CYAN + "Thank You for using our System, Visit Again")
            break
        else:
            print(Fore.RED + "Invalid Choice")
