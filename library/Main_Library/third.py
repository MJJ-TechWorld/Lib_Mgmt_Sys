#======================== - -       Backend       - - ==============================

#******************  WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI  ********************

#===================================================================================


# Important Note : ✖️✅➤⚠️
# Please ensure that you had also cloned "Data.txt" file from program link -
# Please change the default path of "Data.txt" to the actual path where you have saved "Data.txt" file -

emp_data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Employee_details.csv"
books_data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx"
data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx"
premium_mem_path = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Pre_members_info.csv"
notice_path_1 = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Notice1.txt"
notice_path_2 = r"C:\Users\HP\Desktop\training\Python\library\Library_Data\Notice2.txt"

#-----------------------------------------------
# Import some important libraries : 
#-----------------------------------------------

import csv
import random
import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment,Font,Border,Side
from datetime import datetime, timedelta
from Login import underline,login_title,interface_title
from second import check_stock,check_avail_book,check_author_name,check_book_name,check_genre_book,check_publish_date
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
                if (row and row[1] == u and "d" in row[5]):
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
def display_actions():
    """
    Displays actions to be proceed by taking option number as input in str.

    According to option number given by user, it calls to specific functions regarding to it.

    Returns:
        None
    """
    print(f"{info_color}{underline('Available actions')} : \n")
    print(f"\t{noerror_color}1. Check available books in library")
    print(f"\t{noerror_color}2. Check stock of existing books with less copies left ")
    print(f"\t{noerror_color}3. Add new employee")
    print(f"\t{noerror_color}4. Grant access to existing employee \n")
    print(f"\t{noerror_color}5. Revoke access from existing employee \n")
    print(f"\t{noerror_color}6. Give any notice to circulation assistant \n")
    print(f"\t{noerror_color}7. Give any notice to cataloguer \n")
    print(f"\t{noerror_color}8. Give subscription to members \n")
    print(f"\t{noerror_color}9. Remove subscription of members \n")
    print(f"\t{noerror_color}10. Change renting interest of all books of library\n")

    while True:
        print(decor2)
        sel_option = input("Select above option number to proceed further : ").strip()

        if sel_option == "1":
            print(decor2)
            check_avail_book()
            break

        if sel_option == "2":
            print(decor2)
            check_stock()
            break

        if sel_option == "3":
            print(decor2)
            add_employee()
            break

        if sel_option == "4":
            print(decor2)
            grant_revoke_access("g")
            break

        if sel_option == "5":
            print(decor2)
            grant_revoke_access("r")
            break

        if sel_option == "6":
            print(decor2)
            notice_1()
            break

        if sel_option == "7":
            print(decor2)
            notice_2()
            break

        if sel_option == "8":
            print(decor2)
            add_pre_mem()
            break

        if sel_option == "9":
            print(decor2)
            grant_revoke_access("r")
            break

        if sel_option == "10":
            print(decor2)
            change_rate()
            break

        else :
            print(f"\n{error_color} ⚠️ Please Enter Correct Option Number (ex. 1 or 2)!\n")


def actual_program():
    interface_title()
    display_actions()

def login():
    login_title()
    result = login_display()
    if result == "1":
        actual_program()


#------------------------------------------------
#   ) Fn to display actions' options :
#------------------------------------------------

def create_detail(i):
    """
    Take first name, last name and phone number from users, clear them and check according to need.
    Parameters : str : i : It takes of which person's details to be taken
    Returns:
        list: 0 or 1 if all details are correct, first_name, last_name, phone_number of renter
    """

    a,b,c = 0,0,0 # Initializing
    while True:
        print(decor2)
        first_name = input(text_color + f"Enter first name of {i} : ").strip().lower().title()

        if first_name.isalpha() == True:
            print(f"\n{noerror_color}✅  First Name Verified : {first_name}\n")
            a = 1
            break

        else:
            print(f"\n{error_color}⚠️  Please enter valid name\n")           

    if a == 1:
        while True:
            print(decor2)
            last_name = input(text_color + f"Enter last name of {i} : ").strip().lower().title()

            if last_name.isalpha() == True:
                print(f"\n{noerror_color}✅  Last Name Verified : {last_name}\n")
                b = 1
                break

            else:
                print(f"\n{error_color}⚠️  Please enter valid name\n")

    if b == 1:
        while True:
            print(decor2)
            phone_number = input(text_color + f"Enter Phone Number of {i} : ")

            if ( phone_number.isdigit() and len(phone_number) == 10 ):
                print(f"\n{noerror_color}✅  Phone Number Verified : {phone_number}\n")
                c = 1
                break
            
            else:
                print(f"\n{error_color}⚠️  Please enter valid phone number\n")

    return [c,first_name,last_name,phone_number]


def add_employee():
    ed = create_detail("employee")
    if ed[0] == 1:
        while True:
            print(decor2)
            username = input(text_color + "Enter username of new employee : ").strip()

            if username == "":
                print(f"\n{error_color}⚠️  Please enter username\n")

            else:
                break

        while True:
            print(decor2)
            password = input(text_color + "Enter password of new employee : ").strip()

            if password == "":
                print(f"\n{error_color}⚠️  Please enter password\n")

            else:
                break

        with open(emp_data_path, "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                emp = row[0]
    
            digt = int(emp[3:]) + 1
            new_emp_id = "EMP" + str(digt)
            name = f"{ed[1]} {ed[2]}"
        new_emp = [new_emp_id,username,password,name,ed[3]]
        with open(emp_data_path, "a", newline="\n") as f:
            new = csv.writer(f)
            new.writerow(new_emp)

        print(f"\n{noerror_color}Employee details added successfully ! \n")

def grant_revoke_access(result):
    """
    Function to grant/ revoke the access given by user to the employee

    """
    a,b,c = 0,0,0 # Initializing
    while True:
        print(decor2)
        first_name = input(text_color + "Enter first name of employee : ").strip().lower().title()

        if first_name.isalpha() == True:
            print(f"\n{noerror_color}✅  First Name Verified : {first_name}\n")
            a = 1
            break

        else:
            print(f"\n{error_color}⚠️  Please enter valid name\n")           

    if a == 1:
        while True:
            print(decor2)
            last_name = input(text_color + "Enter last name of employee : ").strip().lower().title()

            if last_name.isalpha() == True:
                print(f"\n{noerror_color}✅  Last Name Verified : {last_name}\n")
                b = 1
                break

            else:
                print(f"\n{error_color}⚠️  Please enter valid name\n")

    if b == 1:
        while True:
            print(decor2)
            phone_number = input(text_color + "Enter Phone Number of employee : ")

            with open(emp_data_path, "r") as f:
                data = csv.reader(f)
                next(data)
                for row in data:
                    if ( str(row[5]) == phone_number):
                        while True : 
                            print(decor2)
                            print(f"{Fore.CYAN}{underline('Available accesses that you can grant/revoke to employees')} : \n")
                            print(f"{Fore.CYAN}{underline('You can grant/revoke only one access at a time')} : \n")
                            print(f"\t{Fore.YELLOW}1. Circular Assistant")
                            print(f"\t{Fore.YELLOW}2. Cataloguer")
                            print(f"\t{Fore.YELLOW}3. Director\n")

                            opt = input(text_color + "Enter option number from above data : ").strip()
                            
                            if opt == "1":
                                access = "a"
                                break

                            if opt == "2":
                                access = "c"
                                break

                            if opt == "3":
                                access = "d"
                                break

                            else :
                                print(f"\n{error_color}⚠️  Please enter valid option number from above data\n")


                        with open(emp_data_path, "r+", newline="") as f:
                            rows = list(csv.reader(f))

                            for row in rows:
                                if row[4] == str(phone_number):
                                    if result == "g":
                                        row[5] = row[5] + access
                                    else:
                                        row[5] = row[5].replace(access,"")

                            f.seek(0)
                            f.truncate()
                            write = csv.writer(f)
                            write.writerows(rows)
                        break
                    else:
                        print(f"\n{error_color}⚠️  Employee details with this phone number not in data\n")


def change_rate():
    while True:
        print(decor2)
        rate = input("Enter at which interest should books be rented in library : ")

        if rate.isdigit:
            wb = load_workbook(books_data_path)
            for sheet in wb.sheetnames:
                s = wb[sheet]
                for row in s.iter_rows(min_row=2,values_only=False):
                    if row[6].value is None:
                        continue
                    row[6].value = int((int(row[7].value)) - int((int(row[7].value) * int(rate))/100))
                    row[8].value = int((int(row[7].value) * rate)/100)

            wb.save(books_data_path)         
            print(f"\n{noerror_color}✅ Interest rates changed successfully !\n")
            break

        else:
            print(f"\n{error_color}⚠️ Please enter valid interest rate !\n")

def add_pre_mem():
    date = datetime.today().strftime('%d-%m-%Y')
    cd = create_detail("new member")
    if cd[0] == 1:
        new_mem = [cd[1],cd[2],cd[3],date,"31-12-2026"]
        with open(emp_data_path, "a", newline="\n") as f:
            new = csv.writer(f)
            new.writerow(new_mem)

def notice_1():
    print(decor2)
    notice = input(text_color + "Start writing notice : ")
    print(f"\n{noerror_color}✅ Notice updated successfully !\n")

    with open(notice_path_1, "a") as f:
        f.write(f"{notice}\n")

def notice_2():
    notice = input(text_color + "Start writing notice : ")
    print(f"\n{noerror_color}✅ Notice updated successfully !\n")
    with open(notice_path_2, "a") as f:
        f.write(f"{notice}\n")



# add_employee()

# employee_id,username,password,full name,mobile number,access
# EMP7777,Owner07,India@,Mayuresh Jagtap,8591000000,acd
# EMP1001,user@,pass7,Amit Mishra,7876000000,acd
# EMP1002,mahim01,mhcet2026,Mahim Sane,9584000000,a
# EMP1003,lakshmi@,12345,Lakshmi Sarod,7435000000,c
# EMP1004,varad123,varad07,Varad Mhatre,9898000000,ac
# EMP1005,sunny@,sunmoon,Sunny Tondre,8888000000,ac