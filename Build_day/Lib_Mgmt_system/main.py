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
    

# Initialize colorama (autoreset=True reverts to default color after every print)

while True:
    menu()
    choice = input("Enter your choice between 1 to 6 :: ")
    if choice == "1":
        print("Add Book")
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
    
    