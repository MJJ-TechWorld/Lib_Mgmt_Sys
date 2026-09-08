#======================== - -       Backend       - - ==============================

#******************  WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI  ********************

#===================================================================================


# Important Note : ✖️✅➤⚠️
# Please ensure that you had also cloned "Data.txt" file from program link -
# Please change the default path of "Data.txt" to the actual path where you have saved "Data.txt" file -

emp_data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Employee_details.csv"
books_data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx"
data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx"
pre_mem_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Pre_members_info.csv"

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
from Login import underline
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
#   ) Fn to display actions' options :
#------------------------------------------------

def create_employee_detail():
    """
    Take first name, last name and phone number from users, clear them and check according to need.

    Returns:
        list: 0 or 1 if all details are correct, first_name, last_name, phone_number of renter
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

            if ( phone_number.isdigit() and len(phone_number) == 10 ):
                print(f"\n{noerror_color}✅  Phone Number Verified : {phone_number}\n")
                c = 1
                break
            
            else:
                print(f"\n{error_color}⚠️  Please enter valid phone number\n")

    return [c,first_name,last_name,phone_number]


def add_employee():
    ed = create_employee_detail()
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


grant_revoke_access("9584000000","0")
# add_employee()

# employee_id,username,password,full name,mobile number,access
# EMP7777,Owner07,India@,Mayuresh Jagtap,8591000000,acd
# EMP1001,user@,pass7,Amit Mishra,7876000000,acd
# EMP1002,mahim01,mhcet2026,Mahim Sane,9584000000,a
# EMP1003,lakshmi@,12345,Lakshmi Sarod,7435000000,c
# EMP1004,varad123,varad07,Varad Mhatre,9898000000,ac
# EMP1005,sunny@,sunmoon,Sunny Tondre,8888000000,ac