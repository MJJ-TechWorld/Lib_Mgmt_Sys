#===============     Backend    =================

# *** WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI ***

#-----------------------------------------
# Initialising important paths
#-----------------------------------------

emp_data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Employee_details.csv"
books_data_path = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Books_Data.xlsx"
data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx"
pre_mem_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Pre_members_info.csv"
notice_path_2 = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Notice2.txt"

#-----------------------------------------------
# Import some important libraries : 
#-----------------------------------------------

import csv
from colorama import init, Fore,Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment,Font,Border,Side
from Circulation_Desk import underline,login_title,interface_title,display_genres,check_author_name,check_book_name,check_genre_book,check_publish_date,notice,instruction,exitp,backp
#------------------------------------------------
# Declaring some variables regarding colors and program:
#------------------------------------------------

info_color = Fore.LIGHTYELLOW_EX
text_color = Fore.GREEN
error_color = Fore.RED + Style.BRIGHT
noerror_color = Fore.CYAN + Style.BRIGHT
decor1 = info_color + "*"*55 + "\n"
decor2 = Fore.MAGENTA + "-"*111
decor3 = info_color + "*"*111
decor4 = info_color + "*"*60
filenoterror = f"{Fore.RED + Style.BRIGHT}\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️\n{Fore.RED + Style.BRIGHT}⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n"
filecloseerror = f"{decor1}{error_color}Please ensure that you have closed books_data excel file & data excel file ! \n{decor1}"
genres_code = ["MYTH", "CRIMYS", "ROMNC", "BIOGR", "HIS", "NOV", "ECOCIV", "POET", "POLYSC", "MOTV"]
align_centre = Alignment(horizontal='center', vertical='center')

#------------------------------------------------
#  Fn for displaying and checking login details:
#------------------------------------------------

def login_display():
    """
    Take inputs as username & password one by one
    Check whether they are correct or not
    If not, it asks forever, else logged to main interface.
    """

    a = 0 # Initializing
    global username, password
    login_title = "--- LOGIN PORTAL ---"
    print(info_color + "="*100)
    print(Fore.CYAN + f"\n{login_title:^101}\n")
    print(info_color + "*"*100 + "\n\n")

    while True:
        print(decor2)
        username = input(text_color + "Enter Your Username : ").strip()

        if check_username(username) == "yes": 
            while True:
                print(decor2)
                password = input(text_color + "Enter Your Password : ").strip()

                if check_password(username,password) == "yes":
                    a = 1
                    print(decor3)
                    break
            break
    return a
#------------------------------------------------

def check_username(u):
    """
    Check the username whether it is in record or not.
    Parameters: u : Username of employee who have access to this program.
    Returns: str: "yes" for correct username, "no" for wrong username. 
    """
    try:
        with open(emp_data_path, "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                if (row and row[1] == u and "c" in row[5]):
                    print(f"\n{noerror_color}✅ Username Found \n")
                    return "yes"
                
            print(f"\n{error_color}⚠️  Invalid Username \n")
        
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️")
        print(Fore.RED + Style.BRIGHT + "⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n")

#------------------------------------------------

def check_password(u,p): 
    """
    Check the password whether it is in record with accordance with its username or not.
    
    Takes username & password as parameters and check accordingly.

    Args:
        u : Username of employee who have access to this program.
        p : Password of employee with registered username as well.

    Returns:
        str: "yes" for correct password, "no" for incorrect password.
    """
    try: 
        with open(emp_data_path, "r") as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                if (row and len(row)>1 and row[1] == u  and row[2] == p):
                    print(f"\n{noerror_color}✅  Logged in successfully! \n")
                    return "yes"

            print(f"\n{error_color}⚠️  Wrong Password \n")
        
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️")
        print(Fore.RED + Style.BRIGHT + "⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n")


 
#------------------------------------------------
#  Fn to display actions' options :
#------------------------------------------------

def display_actions():
    """
    Displays actions to be proceed by taking option number as input in str.
    According to option number given by user, it calls to specific functions regarding to it.
    Returns:None
    """
    print(f"{info_color}{underline('Available actions')} : \n")
    print(f"\t{noerror_color}1. Check Stock Balance ")
    print(f"\t{noerror_color}2. Check availability of Book(s) ")
    print(f"\t{noerror_color}3. Add new genre in data")
    print(f"\t{noerror_color}4. Add new books in existing genres ")
    print(f"\t{noerror_color}5. Add more copies of existing books \n")

    while True:
        print(decor2)
        sel_option = input("Select above option number to proceed further : ").strip()

        if sel_option == "1":
            print(decor2)
            check_stock()
            break

        if sel_option == "2":
            print(decor2)
            check_avail_book()
            break

        if sel_option == "3":
            print(decor2)
            add_new_genre()
            break

        if sel_option == "4":
            print(decor2)
            add_new_books()
            break

        if sel_option == "5":
            print(decor2)
            add_more_exist_book()
            break

        else :
            print(f"\n{error_color} ⚠️ Please Enter Correct Option Number (ex. 1 or 2)!\n")

#------------------------------------------------
#  Fn to check stock balance of books :
#------------------------------------------------

def check_stock():
        while True:
            r = 0
            q = input(text_color + "Enter quantity of books to be checked, left in library : ").strip()
            if q.isdigit() and int(q) >= 0:
                print(Fore.BLUE + f"\n\nBooks with {q} or 0 quantities left : \n")
                wb = load_workbook(books_data_path)
                for sheet in wb.worksheets:
                    for row in sheet.iter_rows(min_row=2,values_only=False):
                        if str(row[7].value).strip() == str(q):
                            print(decor2)
                            print(f"{info_color}{row[1].value}  {row[2].value}  By {row[3].value}  Avail : {row[7].value}")
                            r = 1
            if r == 1:
                break
            else:
                print(f"\n{error_color}⚠️ Please enter valid quantity !\n")

#------------------------------------------------------------
#  Fn to check whether a book is availble in library or not :
#------------------------------------------------------------

def check_avail_book():
    while True : 
        print(f"\t{Fore.CYAN}{underline('Ways to check availability of book(s)')} : ")
        print("\t")
        print("1. By name of book")
        print("2. By author name of book")
        print("3. By publishing date of book")
        print("4. By genre of book (gives list of all books under this genre)\n")

        print(decor2)
        sel_option = input("Select option to proceed further : ").strip()

        if sel_option == "1":
            check_book_name()
            break
        if sel_option == "2":
            check_author_name()
            break
        if sel_option == "3":
            check_publish_date()
            break
        if sel_option == "4":
            check_genre_book()
            break
        else:
            print(f"\n{error_color} ⚠️ Please Enter Correct Option Number (ex. 1 or 2)!\n")

#----------------------------------------------
# Fn to add new genre 
#------------------------------------------------
def add_new_genre():
        try:
            
            print(decor2)
            new_genre = input(text_color + "Enter new genre name : ").strip().upper()
            print(decor2)
            print(Fore.YELLOW + "Add atleast one book's details under this new genre\n")
            new_code = input(text_color + "Enter general unique code for books under this genre (ex. MYTH, NOV) : ").upper()
            print(decor2)
            new_book_name = input(text_color + "Enter proper name of book : ").strip()
            print(decor2)
            new_author_name = input(text_color + "Enter proper name of author of book : ").strip().capitalize()
            print(decor2)
            new_lang = input(text_color + "Enter language in which book is written : ").strip().upper()
            print(decor2)
            new_publ_dt = input(text_color + "Enter publishing date of book in format (dd-mm-yy) : ").strip()
            print(decor2)
            new_mrp = input(text_color + "Enter market price of book (in Rs) : ").strip()
            print(decor2)
            new_qnt = input(text_color + "Enter quantity of copies of this book : ").strip()
            print(decor2)
            new_charge = int((int(new_mrp)*4)/100)
            print(decor2)
                                    
            wb = load_workbook(books_data_path)
            s = wb.create_sheet(new_genre)
            header = ["Sr No","DDC Code","Book Name","Author Name","Language","Published Date", "Market Price (INR)", "Quantities Available", "Charges per day (Rs)"]
            col_width = [7,15,50,28,17,20,18,21,20]
            f = Font(bold=True, underline="single")
            a = Alignment(horizontal="center")
            b = Border(left=Side("thin"),right=Side("thin"),top=Side("thin"),bottom=Side("thin"))
            for i in range(len(header)):
                col = i + 1
                c = s.cell(row=1, column=col)
                c.value = header[i]
                c.font = f
                c.alignment = a
                c.border = b
                s.column_dimensions[c.column_letter].width = col_width[i]
            s.append([1,f"{new_code}10001",new_book_name,new_author_name,new_lang,new_publ_dt,int(new_mrp),int(new_qnt),int(new_charge)])
            for cell in s[s.max_row]:
                cell.alignment = align_centre
            print(f"\n{noerror_color}✅ Data updated successfully !\n")
            print(decor2,decor3,sep = "\n")
            wb.save(books_data_path)

        except FileNotFoundError:
            print(filenoterror)
        except PermissionError:
            print(filecloseerror)

#------------------------------------------------
#   Fn to display actions' options :
#------------------------------------------------

def add_new_books():
    while True:
        display_genres()
        print(decor2)
        print(Fore.YELLOW + "--- Add New Book Details ---\n")
        new_genre = input(text_color + "Enter genre of this book from above table : ").strip()

        wb = load_workbook(books_data_path, data_only=True)
        req_s = None
        for s in wb.sheetnames:
            if new_genre.strip().lower() in s.strip().lower():
                req_s = s
                break

        if req_s:
            print(decor2)
            new_book_name = input(text_color + "Enter proper name of book : ").strip()
            print(decor2)
            new_author_name = input(text_color + "Enter proper name of author of book : ").strip().capitalize()
            print(decor2)
            new_lang = input(text_color + "Enter language in which book is written : ").strip().upper()
            print(decor2)
            new_publ_dt = input(text_color + "Enter publishing date of book in format (dd-mm-yy) : ").strip()
            print(decor2)
            new_mrp = input(text_color + "Enter market price of book (in Rs) : ").strip()
            print(decor2)
            new_qnt = input(text_color + "Enter quantity of copies of this book : ").strip()
            print(decor2)
            new_charge = int((int(new_mrp)*4)/100)
            print(decor2)

            wd = load_workbook(books_data_path)
            ws = wd[req_s]
            last_row = ws.max_row
            last_sr = ws.cell(row=last_row,column=1).value
            last_uc = ws.cell(row=last_row,column=2).value
            new_sr = int(last_sr) + 1
            text,digt = "",""
            for i in last_uc:
                if i.isdigit() == False:
                    text = text + i
                else:
                    digt = digt + i
            new_digt = int(digt) + 1
            new_uc = text + str(new_digt)
            ws.append([new_sr,new_uc,new_book_name,new_author_name,new_lang,new_publ_dt,int(new_mrp),int(new_qnt),int(new_charge)])
            for cell in ws[ws.max_row]:
                cell.alignment = align_centre
            wd.save(books_data_path)
            print(f"\n{noerror_color}✅ Data updated successfully !\n")

        else : 
            print(f"\n{error_color} ⚠️  Book(s) with this genre Not Found \n")


def add_more_exist_book():
    print(decor2)
    while True:
        unique_code = input(text_color + "Enter unique code of book : ").strip()
        wb = load_workbook(books_data_path)
        a = 0
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(min_row=2,values_only=False):
                if str(row[1].value).strip() == unique_code:
                    a = 1
                    break
            if a == 1:
                break
        if a == 1:
            print(f"\n{noerror_color}✅ Book Found with this unique code \n")

            while True:
                print(decor2)
                quantity = input(text_color + "Enter quantity of copies of this book to be added : ").strip()

                if quantity.isdigit() and int(quantity) > 0:
                        row[7].value = int(row[7].value) + int(quantity)
                        wb.save(books_data_path)
                        print(f"\n{noerror_color}✅ Data updated successfully ! \n")
                        return
                else:
                    print(f"\n{error_color}⚠️ Please enter valid quantity ! (ex. 2 or 4)\n")
        else:
            print(f"\n{error_color}⚠️ Book with this unique code not found !\n")
    

#------------------------------------------------
#  Fn to call functions after login : 
#------------------------------------------------

def after_login_display():
    interface_title()
    instruction()
    notice(notice_path_2)
    display_actions()

#------------------------------------------------
# Fn for starting program :
#------------------------------------------------

def start_program():
    login_title()
    if login_display() == 1:
        after_login_display()

#================================================
# Calling functions : 
#--------------------

if __name__ == "__main__":
    start_program()