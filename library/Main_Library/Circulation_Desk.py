#============  Backend =================

# *** WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI ***

#-----------------------------------------
# Initialising important paths
#-----------------------------------------

emp_data_path = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Employee_details.csv"
books_data_path = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Books_Data.xlsx"
data_path = r"C:\Users\HP\Desktop\training\Python\Library\library_Data\Data.xlsx"
premium_mem_path = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Pre_members_info.csv"
notice_path_1 = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Notice1.txt"

#-----------------------------------------------
# Import some important libraries : 
#-----------------------------------------------

import csv
import random
import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from datetime import datetime, timedelta

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
#  Functions for decorative purposes :
#------------------------------------------------

def underline(text):
    """
    Gives underline to the text.
    Args:text: Text to be display in underline.
    Returns:underlines the text given as parameter. 
    """
    return f"\033[4m{text}\033[0m"

#------------------------------------------------
#  Fn of displaying login title :
#------------------------------------------------

def login_title():
    """Display attractive title of login portal."""
    a = Back.LIGHTCYAN_EX + "     "
    r,b,re,s = Fore.GREEN + Style.BRIGHT,Fore.BLUE + Style.BRIGHT + Back.LIGHTYELLOW_EX,Fore.RED  + Back.LIGHTMAGENTA_EX," "*101
    d,t1,T1,t2,t3,t4 = "*"*50,"="*91," "*85,"💻    DIGITAL LIBRARY     💻","OF","🗺️      NAVI MUMBAI       🗺️"
    t5 = "( By MJJ-TECHWORLD )"

    print("\n\n")
    print(Back.LIGHTCYAN_EX + s)
    print(a,r + t1,a, sep = "")
    print(a,r + t1,a, sep = "")
    print(a,r + "|| ",r + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{t2:^83}",r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{t3:^85}",r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{t4:^87}",r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{d:^85}",r + " ||",a, sep = "")
    print(a,r + "|| ",re + f"{t5:^85}",r + " ||",a, sep = "")
    print(a,r + "|| ",r + T1,r + " ||",a, sep = "")
    print(a,r + t1,a, sep = "")
    print(a,r + t1,a, sep = "")
    print(Back.LIGHTCYAN_EX + s, "\n\n")

#------------------------------------------------
#  2) Fn for displaying and checking login details:
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
                if (row and row[1] == u and "a" in row[5]):
                    print(f"\n{noerror_color}✅ Username Found \n")
                    return "yes"
                
            print(f"\n{error_color}⚠️  Invalid Username \n")
        
    except FileNotFoundError:
        filenoterror()
#------------------------------------------------

def check_password(u,p): 
    """
    Check the password whether it is in record with accordance with its username or not.
    Takes username & password as parameters and check accordingly.
    Args:u : Username of employee who have access to this program.
         p : Password of employee with registered username as well.
    Returns:str: "yes" for correct password, "no" for incorrect password.
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
        filenoterror()

#------------------------------------------------
#  Fn to create title of interface :
#------------------------------------------------

def interface_title():
    """Creates attractice title of main interface after logged in."""
    print(decor2, "\n")
    color0,color1,color2,color3,decor = Fore.YELLOW,Fore.GREEN,Fore.CYAN,Fore.MAGENTA,"*"*36

    print(Fore.CYAN + 
    f'''                        \t╔══════════════════════════════════════════════╗
                        \t║                                              ║
                        \t║        {color0}                                      ║
                        \t║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
                        \t║        {color1}                                      ║
                        \t║               ( By MJJ-TECHWORLD )           ║
                        \t║                                              ║
                        \t║{color3}     {decor}     ║
                        \t║        {color2}                                      ║
                        \t╚══════════════════════════════════════════════╝''')

#------------------------------------------------
#  Fn for displaying instructions and notices :
#------------------------------------------------

def instruction():
    # a = "Type 'backp' and press Enter to go to main portal directly."
    b = "Type 'exitp' and press Enter to exit the program"
    print(decor3)
    print(f"{info_color}{underline('✯  Instructions  ✯')} : \n")
    # print(Fore.YELLOW + f"\t☞ Back : {a} ")
    print(Fore.YELLOW + f"\t☞ Exit : {b} \n")
    print(decor3)

def notice(path):
    print(Fore.BLUE + Style.BRIGHT + "🆕  NOTICE","\n")
    with open(path) as f:
        data = f.read()
        print(Fore.GREEN + data[:101])
        print(Fore.GREEN + data[101:201])
        print(Fore.GREEN + data[201:301])
        print(decor3)


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
    print(f"\t{noerror_color}1. Search for Unique Code of Book(s) ?")
    print(f"\t{noerror_color}2. Rent Book(s) for rental customers?")
    print(f"\t{noerror_color}3. Rent Book(s) for premium members? ")
    print(f"\t{noerror_color}4. Return Book(s) of rental customers? ")
    print(f"\t{noerror_color}5. Return Book(s) of premium members? \n")

    while True:
        print(decor2)
        sel_option = input("Select above option number to proceed further : ").strip()

        if sel_option == "1":
            print(decor2)
            search_uc()
            break

        if sel_option == "2":
            print(decor2)
            rent_by_uc()
            break

        if sel_option == "3":
            print(decor2)
            premium_mem()
            break

        if sel_option == "4":
            print(decor2)
            return_books("Sheet1")
            break

        if sel_option == "5":
            print(decor2)
            return_books("Sheet2")
            break

        else :
            print(f"\n{error_color} ⚠️ Please Enter Correct Option Number (ex. 1 or 2)!\n")

#--------------------------------------------------
# Fn for displaying main portal after calling backp
#--------------------------------------------------

def main_portal():
    interface_title()
    display_actions()

#------------------------------------------------
#  Fn for shortcuts of exit and back options:
#------------------------------------------------

# def backp():
#         print(f"{info_color}Session Expired!")
#         print(decor2)
#         main_portal()

def exitp(p):
    if p.strip().lower() == "exitp":
        print(decor2)
        print(f"{info_color}Program Exited!")
        print(decor2)
        exit()


#------------------------------------------------
#  Fn for creating renter's details :
#------------------------------------------------

def create_renter_detail():
    """
    Take first name, last name and phone number from users, clear them and check according to need.
    Returns:list: 0 or 1 if all details are correct, first_name, last_name, phone_number of renter
    """

    a,b,c = 0,0,0 # Initializing
    while True:
        print(decor2)
        first_name = input(text_color + "Enter first name of renter : ").strip().lower().title()
        exitp(first_name)

        if first_name.isalpha() == True:
            print(f"\n{noerror_color}✅  First Name Verified : {first_name}\n")
            a = 1
            break

        else:
            print(f"\n{error_color}⚠️  Please enter valid name\n")           

    if a == 1:
        while True:
            print(decor2)
            last_name = input(text_color + "Enter last name of renter : ").strip().lower().title()
            exitp(last_name)

            if last_name.isalpha() == True:
                print(f"\n{noerror_color}✅  Last Name Verified : {last_name}\n")
                b = 1
                break

            else:
                print(f"\n{error_color}⚠️  Please enter valid name\n")

    if b == 1:
        while True:
            print(decor2)
            phone_number = input(text_color + "Enter Phone Number of renter : ").strip()
            exitp(phone_number)

            if ( phone_number.isdigit() and len(phone_number) == 10 ):
                print(f"\n{noerror_color}✅  Phone Number Verified : {phone_number}\n")
                c = 1
                break
            
            else:
                print(f"\n{error_color}⚠️  Please enter valid phone number\n")

    return [c,first_name,last_name,phone_number]

#------------------------------------------------
#   Fn to check uc by name of book :
#------------------------------------------------

def check_book_name():
    while True:
        print(decor2)
        book_name = input(text_color + "Enter name of book : ").strip().lower()
        print(decor2)
        exitp(book_name)

        value =  False # Initialising

        wb = load_workbook(books_data_path, data_only=True)
        for s in wb.worksheets:
            for row in s.iter_rows(min_row=2,values_only=True):
                if book_name in str(row[2]).strip().lower():
                    print(decor2)
                    print(f"{row[1]} : {s.title} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
                    value = True
        
        if value:
            print(decor2)
            main_portal()
            break
        else : 
            print(f"\n{error_color}⚠️  Book(s) with this name Not Found ! \n")

#------------------------------------------------
#   Fn to check uc by author name of book :
#------------------------------------------------

def check_author_name():
    while True:
        print(decor2)
        author_name = input(text_color + "Enter author name of book : ").strip().lower()
        print(decor2)
        exitp(author_name)

        value =  False # Initialising

        wb = load_workbook(books_data_path, data_only=True)
        for s in wb.worksheets:
            for row in s.iter_rows(min_row=2,values_only=True):
                if author_name in str(row[3]).strip().lower():
                    print(decor2)
                    print(f"{row[1]} : {s.title} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
                    value = True
            
        if value:
            print(decor2)
            main_portal()
            break
        else : 
            print(f"\n{error_color} ⚠️  Book(s) with this name Not Found \n")

#------------------------------------------------
#   Fn to check uc by publishing date of book :
#------------------------------------------------

def check_publish_date():
    while True:
        print(decor2)
        publish_date = input(text_color + "Enter publishing date of book in format 'dd-mm-yy' : ").strip().lower()
        print(decor2)
        exitp(publish_date)

        value = False

        wb = load_workbook(books_data_path, data_only=True)
        for s in wb.worksheets:
            for row in s.iter_rows(min_row=2, values_only=True ):
                if publish_date in str(row[5]).strip().lower():
                    print(decor2)
                    print(f"{row[1]} : {s.title} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
                    value = True
        
        if value:
            print(decor2)
            main_portal()
            break
        else : 
            print(f"\n{error_color} ⚠️  Book(s) with this 'Date Of Publish' Not Found \n")

#------------------------------------------------
#   ) Fn for displaying genres in excel in proper format :
#------------------------------------------------

def display_genres():
    try : 
        print(decor2, "\n")
        print(Fore.CYAN + "GENRES OF BOOKS AVAILABLE IN LIBRARY \n")
        print(decor2)
        wb = load_workbook(books_data_path)
        sheet_names = wb.sheetnames
        for i in sheet_names:
            if sheet_names.index(i) % 2 == 0:
                print(f"   {info_color}{i:<50}|", end = "")
            else:
                print(f"{info_color}{i:>50}")

        print("\n", decor2)

    except FileNotFoundError:
        filenoterror()

#------------------------------------------------
#  Fn to check uc by genre of book :
#------------------------------------------------

def check_genre_book():

    display_genres()
    while True:
        print(decor2)
        genre_books = input(text_color + "Enter genre of desire book from above table : ").strip().lower()
        print(decor2)
        exitp(genre_books)

        value = False

        wb = load_workbook(books_data_path, data_only=True)
        for s in wb.worksheets:
            if genre_books in str(s.title).strip().lower():
                for row in s.iter_rows(min_row=2, values_only=True ):
                    print(decor2)
                    print(f"{row[1]} : {s.title} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
                    value = True
        
        if value:
            print(decor2)
            main_portal()
            break
        else : 
            print(f"\n{error_color} ⚠️  Book(s) with this genre Not Found \n")

#------------------------------------------------
#  Fn to rent book by searching other factors first then unique code :
#------------------------------------------------

def search_uc():
    print(f"\n{decor4}\n\t{Fore.MAGENTA}   Search Unique Code Of Book(s) \n{decor4}\n")
    while True : 
        print(f"\t{Fore.CYAN}{underline('Ways to find Unique Code (uc) of book(s)')} : ")
        print("\t")
        print(f"{info_color}1. By name of book")
        print(f"{info_color}2. By author name of book")
        print(f"{info_color}3. By publishing date of book")
        print(f"{info_color}4. By genre of book (gives list of all books under this genre)\n")

        print(decor2)
        sel_option = input("Select option to proceed further : ").strip()
        exitp(sel_option)

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

#------------------------------------------------
#   ) Fn to rent book via unique code :
#------------------------------------------------

def rent_by_uc():
    a = 0 # initializing
    s = " "*35
    while True:
        print(decor2)
        unique_code = input(f"{text_color}Enter the unique code of desire book : ").strip()
        print(decor2)
        exitp(unique_code)

        details = []
        wb = load_workbook(books_data_path)
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(min_row=2,values_only=False):
                for cell in row:
                   if unique_code == str(cell.value):
                       a = 1
                       details.append(f"{row[1].value} | Name : {row[2].value} |\n{s} Author : {row[3].value} |Language : {row[4].value}")

        if a == 1:
            print(f"\n{noerror_color}✅ Book Found with this unique code {details[0]} \n")
            record_rent_book_detail(unique_code)
            break
        else:
            print(f"\n{error_color}⚠️ Book with this unique code not found !\n")

#------------------------------------------------
#  Fn to ask to rent more books or not :
#------------------------------------------------

def ask_add_more(fn,ln,pn,cl,bl,al,Cl,tl,t,r):
    print(f"{info_color}{underline('Want to rent more books ?')}\n")
    print(f"\t{noerror_color}1. Yes")
    print(f"\t{noerror_color}2. No")

    while True:
        print(decor2)
        sel_option = input("Select above option number to proceed further : ").strip()
        if sel_option == "1":
            print(decor2)
            add_more(fn,ln,pn,cl,bl,al,Cl,tl,t,r)
            break

        if sel_option == "2":
            print(decor2)
            bill_printer(fn,ln,pn,cl,bl,al,Cl,tl,t,r)
            main_portal()
            break

        else :
            print(f"\n{error_color} ⚠️ Please Enter Correct Option Number (ex. 1 or 2)!\n")

#------------------------------------------------
#  Fn to rent books for premium members : 
#------------------------------------------------

def add_more(fn,ln,pn,cl,bl,al,Cl,tl,t,r="NO"):
    # initializing
    a,b,c = 0,0,0
    s = " "*35
    if r == "NO":
        sn = "Sheet1"
    elif r == "YES":
        sn = "Sheet2"
    while True:
        print(decor2)
        unique_code = input(f"{text_color}Enter the unique code of desire book : ")
        print(decor2)
        exitp(unique_code)

        details = []
        wb = load_workbook(books_data_path)
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(min_row=2,values_only=False):
                for cell in row:
                   if unique_code == str(cell.value):
                       a = 1
                       details.append(f"{row[1].value} | Name : {row[2].value} |\n{s} Author : {row[3].value} | Language : {row[4].value}")

        if a == 1:
            print(f"\n{noerror_color}✅ Book Found with this unique code {details[0]} \n")
            while True:
                print(decor2)
                tenure = input(text_color + "Enter borrowing period days : ")
                print(decor2)
                exitp(tenure)

                if tenure.isdigit() == True:
                    b = 1
                    break
                else:
                    print(f"{decor1}{error_color}Please enter valid number of days (ex. 3 or 5)\n{decor1}")
                    b = 0

        if b == 1:
            try:
                now_date = datetime.today()
                then_date = now_date + timedelta(days=int(tenure))
                issue_date = now_date.strftime('%d-%m-%Y')
                due_date = then_date.strftime('%d-%m-%Y')
                wb = openpyxl.load_workbook(books_data_path, data_only=True)
                for s in wb.worksheets:
                    for row in s.iter_rows(min_row=2,values_only=False):
                        for cell in row:
                            if unique_code in str(cell.value):
                                c = 1
                                wd = load_workbook(data_path)
                                sheet = wd[sn]
                                sheet.append([f"{fn} {ln}",f"{int(pn)}",row[1].value, row[2].value, row[3].value, row[6].value, row[8].value, issue_date, int(tenure), due_date, int(tenure)*int(row[8].value),"NO"])
                                cl.append(row[1].value)
                                bl.append(row[2].value)
                                al.append(row[3].value)
                                Cl.append(int(row[8].value))
                                tl.append(int(tenure))
                                t.append(int(tenure)*int(row[8].value))
                                for cell in sheet[sheet.max_row]:
                                    cell.alignment = align_centre
                                wd.save(data_path)
                                mod_books(cl,sn,"NO")
                if c == 1:
                    ask_add_more(fn,ln,pn,cl,bl,al,Cl,tl,t,r)

            except FileNotFoundError:
                print(filenoterror)

            except PermissionError:
                print(filecloseerror)
            break
        else:
            print(f"\n{error_color}⚠️ Book with this unique code not found !\n")

#------------------------------------------------
#   ) Fn to record details of book rented : 
#------------------------------------------------

def record_rent_book_detail(uc):
    d,e,code_list,book_list,author_list,charges_list,tenure_list,total = 0,0,[],[],[],[],[],[]
    renter_data = create_renter_detail()
    if renter_data[0] == 1:

        while True:
            print(decor2)
            tenure = input(text_color + "Enter borrowing period days : ")
            print(decor2)

            if tenure.isdigit() == True and tenure != "0":
                d = 1
                break
            else:
                print(f"{decor1}{error_color}Please enter valid number of days (ex. 3 or 5)\n{decor1}")
                d = 0

    if d == 1:
        try:
            now_date = datetime.today()
            then_date = now_date + timedelta(days=int(tenure))
            issue_date = now_date.strftime('%d-%m-%Y')
            due_date = then_date.strftime('%d-%m-%Y')
            wb = openpyxl.load_workbook(books_data_path,data_only=True)
            for s in wb.worksheets:
                for row in s.iter_rows(min_row=2,values_only=False):
                    for cell in row:
                        if uc in str(cell.value):
                            e = 1
                            wd = load_workbook(data_path)
                            sheet = wd["Sheet1"]
                            sheet.append([f"{renter_data[1]} {renter_data[2]}",int(renter_data[3]),row[1].value, row[2].value, row[3].value, row[6].value, row[8].value, issue_date, int(tenure), due_date, int(tenure)*int(row[8].value), "NO"])
                            code_list.append(row[1].value)
                            book_list.append(row[2].value)
                            author_list.append(row[3].value)
                            charges_list.append(int(row[8].value))
                            tenure_list.append(int(tenure))
                            total.append(int(tenure)*int(row[8].value))
                            for cell in sheet[sheet.max_row]:
                                cell.alignment = align_centre
                            wd.save(data_path)
                            mod_books(code_list,"Sheet1","NO")
            if e == 1:
                ask_add_more(renter_data[1], renter_data[2], renter_data[3],code_list,book_list,author_list,charges_list,tenure_list,total,r="NO")


        except FileNotFoundError:
            print(filenoterror)

        except PermissionError:
            print(filecloseerror)

#------------------------------------------------
#   ) Fn to print bill of books rented : 
#------------------------------------------------

def bill_printer(fn,ln,pn,cl,bl,al,Cl,tl,t,r):
    tc = Fore.YELLOW
    title_text1 = Fore.BLUE
    title_text2 = Fore.RED 
    line = Fore.CYAN
    d = line + "║"

    bill_tiltle1 = "📚   DIGITAL LIBRARY OF NAVI MUMBAI   📚"
    bill_tiltle2 = "( By MJJ-TechWorld )"

    l1,l2,l3,l4,l5 = "Name Of Books","Name Of Authors","Charges/","Tenure","Total"
    l7 = f"{text_color}Have membership ? {tc}{r}"
    l8 = f"{Fore.BLUE}--- Thank You Visit Again ---"
    l6 = f"{text_color}Date: {tc}{datetime.today().strftime('%d-%m-%Y')}"
    name = f"{fn} {ln}"

    good_quotes = ["'Books are uniquely portable magic'",
                   "'Today a reader,tomorrow a leader'",
                   "'Read what you love until you love to read'"
                   "'There is no friend as loyal as a book'",
                   "'A book dream is a dream that you hold in your hand'"]

    q = Fore.YELLOW + Style.BRIGHT + random.choice(good_quotes)

    total = 0
    if r == "NO":
        for i in t:
            total = total + int(i)
    else:
        total = 0

    print(line + "╔",line + "═"*108,line + "╗", sep = "")
    print(d," "*108,d, sep = "")
    print(f"{d}{title_text1}{bill_tiltle1:^106}{d}")
    print(d," "*33,Fore.MAGENTA + "-"*45," "*30,d, sep = "")
    print(d," "*108,d, sep = "")
    print(f"{d}{title_text2}{bill_tiltle2:^108}{d}")
    print(d," "*108,d, sep = "")
    print(d,Fore.MAGENTA + "*"*108,d, sep = "")
    print(d," "*108,d, sep = "")
    print(f"{d} {text_color} Name: {tc}{name:<82}{l6}  {d}")
    print(f"{d} {text_color} Mobile No : {tc}{pn:<71} {l7}  {d}")
    print(d," "*108,d, sep = "")
    print(d,Fore.BLUE + "*"*108,d, sep = "")
    print(d," "*108,d, sep = "")
    print(d,Fore.YELLOW + "="*108,d, sep = "")
    print(f"{d} Sr. {d} Unique Code {d}{l1:^36}{d}{l2:^25}{d} {l3:^8}{d}{l4:^6}{d}{l5:^7} {d}")
    print(d," "*5,d," "*13,d," "*36,d," "*25,d,Fore.CYAN + "    day  ",d," "*6,d," "*8,d, sep = "")
    print(d,Fore.YELLOW + "="*108,d, sep = "")

    for i in range(len(cl)):
        print(f"{d} {i+1:^3}.{d} {cl[i]:^12}{d}{bl[i][:36]:^36}{d}{al[i][:25]:^25}{d}{str(Cl[i])[:9]:^9}{d}{tl[i]:^6}{d}{t[i]:^7} {d}")

    print(d,Fore.YELLOW + " "*108,d, sep = "")
    print(d,Fore.YELLOW + "="*108,d, sep = "")
    print(d," "*86,f"{Fore.GREEN}{Style.BRIGHT}Total : Rs {total:^7}/-  ",   d,sep = "")
    print(d," "*108,d, sep = "")
    print(d,Fore.MAGENTA + "*"*108,d, sep = "")
    print(d,f"{l8:^113}",d,sep = "")
    print(d,Fore.MAGENTA + "*"*108,d, sep = "")
    print(d,f"{q:^117}",d, sep = "")
    print(line + "╚",line + "═"*108,line + "╝", sep = "")

#------------------------------------------------
#   ) Fn to rent books for premium members : 
#------------------------------------------------

def premium_mem():
    a,b,c,d,cl,bl,al,Cl,tl,t = 0,0,0,0,[],[],[],[],[],[] # Initializing
    while True:
        print(decor2)
        first_name = input(text_color + "Enter first name of member : ").strip().lower().title()
        exitp(first_name)

        if first_name.isalpha() == True:
            a = 1
            break

        else:
            print(f"\n{error_color}⚠️  Please enter valid name\n")           

    if a == 1:
        while True:
            print(decor2)
            last_name = input(text_color + "Enter last name of renter : ").strip().lower().title()
            exitp(last_name)

            if last_name.isalpha() == True:
                b = 1
                break

            else:
                print(f"\n{error_color}⚠️  Please enter valid name\n")

    if b == 1:
            try:
                with open(premium_mem_path, "r") as f:
                    data = csv.reader(f)
                    next(data)
                    print(Fore.YELLOW + "\nRecords Found from given inputs : ")
                    for row in data:
                        if (row and row[0] == first_name and row[1] == last_name):
                            print(f"{decor2}\n{noerror_color}{row[0]} {row[1]}  :  {row[2]}\n")
                            pn = row[2]
                            c = 1
        
                            if c != 1:
                                print(f"\n{error_color}⚠️ Name not found in data ! \n")
                        
            except FileNotFoundError:
                print(filenoterror)

    if c == 1:
            while True:
                print(decor2)
                phone_number = input(text_color + "Enter Phone Number From above table : ")
                exitp(phone_number)

                if ( phone_number == pn):

                    otp = random.randint(1000, 9999)
                    print(f"\n{Fore.BLUE}{Style.DIM}Hint : Your OTP is: {otp}")
                    while True:
                        print(decor2)
                        take_otp = input(f"{text_color}Enter otp sent on {phone_number} : ")

                        if take_otp == str(otp):
                            print(f"\n{noerror_color}✅  Member's Details Verified successfully !\n")
                            d = 1
                            break
                        else:
                            print(f"\n{error_color}⚠️ Invalid otp\n")

                    break
                else:
                    print(f"\n{error_color}⚠️ Invalid phone number \n")

    if d == 1:
        add_more(first_name,last_name,phone_number,cl,bl,al,Cl,tl,t,r="YES")

#------------------------------------------------
#  Fn to return books for rental and premium customers : 
#------------------------------------------------

def return_books(m):
    a,b,c,nf,s,updated_books = 0,0,0,[],set(),[]
    while True:
            print(decor2)
            first_name = input(text_color + "Enter first name of returner : ").strip().lower().title()
            print(decor2)
            exitp(first_name)
    
            if first_name.isalpha() == True:
                a = 1
                break
    
            else:
                print(f"\n{error_color}⚠️  Please enter valid name\n")           
    
    if a == 1:
        while True:
            print(decor2)
            last_name = input(text_color + "Enter last name of returner : ").strip().lower().title()
            print(decor2)
            exitp(last_name)
    
            if last_name.isalpha() == True:
                b = 1
                break

            else:
                print(f"\n{error_color}⚠️  Please enter valid name\n")
    
    if b == 1:
            name = f"{first_name} {last_name}"
            wb = load_workbook(data_path, data_only=True)
            sheet = wb[m]
            print(decor2)
            print(f"{Fore.BLUE}Phone Numbers associated with this name : ")
            for row in sheet.iter_rows(min_row=2,values_only=True):
                if name.strip().lower() == str(row[0]).strip().lower():
                    s.add(f"{row[1]}")
                    pn,c = row[1],1
            for i in s:
                print(Fore.YELLOW + i)
            wb.save(data_path)
    
    if c == 1:     
        while True:
            print(decor2)
            phone_number = input(text_color + "Enter Phone Number From above table : ")
            exitp(phone_number)

            if ( int(phone_number) == int(pn)):
                print(decor2)
                print(f"\n{info_color} Books remaining to be returned : \n")

                wd = load_workbook(data_path, data_only=False)
                sheet = wd[m]
                for row in sheet.iter_rows(min_row=2):
                    if str(row[11].value) == "NO":
                        print(Fore.YELLOW + row[2].value,  row[3].value)
                print(decor2)

                print(f"{info_color}{underline('Important Instructions')}\n")
                print(f"\t{noerror_color}You can write multiple unique codes separated by commas.")
                print(f"\t{noerror_color}Example: MYTH10001, NOV10001\n")
                rbooks = input(text_color + "Enter unique codes of books in given format : ")
                exitp(rbooks)

                books = rbooks.replace(" ","")
                book_list = books.split(",")
                for book in book_list:
                    book = book.strip()
                    if not book:
                        continue
                    found = False

                    for row in sheet.iter_rows(min_row=2):
                        if book == str(row[2].value) and str(row[11].value) == "NO":
                            row[11].value = "YES"
                            found = True
                            mod_books(book_list,m,"YES")
                            updated_books.append(book)
                            break
                    if not found:
                        nf.append(book)

                wd.save(data_path)
                if len(updated_books) > 0:
                    print(f"\n{noerror_color}✅  Records Updated successfully !\n")
                    mod_books(updated_books,m,"YES")

                if len(updated_books) == 0:
                    print(f"\n{noerror_color}✅  Nothing Updated already marked yes!\n")
                    main_portal()

                if len(nf) > 0:
                    er =str(nf).replace("[","")
                    er = er.replace("]","")
                    print(f"\n{error_color}⚠️  Note that book with uc : {er} not found !\n")
                    main_portal()

                break
            else:
                print(f"\n{error_color}⚠️ Invalid phone number \n")


#------------------------------------------------
#  Fn to modify data in excel according to books rented or returned : 
#------------------------------------------------

def mod_books(l,s,r):
    for book in l:
        wd = load_workbook(books_data_path, data_only=True)

        wd = load_workbook(books_data_path)
        for sheet in wd.worksheets:
            for row in sheet.iter_rows(min_row=2,values_only=False):
                if book == str(row[1].value):
                    if r == "NO":
                        row[7].value = int(row[7].value) - 1
                    elif r == "YES":
                        row[7].value = int(row[7].value) + 1
        wd.save(books_data_path)

#------------------------------------------------
#  Fn to call functions after login : 
#------------------------------------------------

def after_login_display():
    interface_title()
    instruction()
    notice(notice_path_1)
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