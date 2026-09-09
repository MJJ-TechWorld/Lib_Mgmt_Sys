#----------------    BACKEND    -----------------

#------------------------------------------------
# IMPORTANTS IMPORTS FOR THIS PROGRAM
#------------------------------------------------

import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from rich import console
from datetime import datetime, timedelta
from pyfiglet import figlet_format


import csv
import random
import time
import uuid
import os
import emoji

from getpass import getpass
from datetime import datetime, timedelta
from pyfiglet import figlet_format

from rich.console import Console
from rich.table import Table
from rich.progress import track
console = Console()
#------------------------------------------------
# ASSIGNING IMP PATHS TO THE VARIABLES
#------------------------------------------------

books_data_path = r"C:\Users\HP\Desktop\training\Python\books_store\books_copy.xlsx"
users_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\users_data.xlsx"
empls_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\empls_data.csv"
credt_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\credentials.txt"

#------------------------------------------------
# ASSIGNING VALUES TO IMP VARIABLES :
#------------------------------------------------


#------------------------------------------------
# DEFINING IMP FUNCTIONS OF DECORATIVE STUFFS :
#------------------------------------------------

def error_message(error):
    console.print(f"\n[bold red]⚠️ {error}[/bold red]")

def info_message(message):
    console.print(f"[cyan]{message}[/cyan]")

def correct_message(message):
    console.print(f"\n[bold cyan]✅ {message}[/bold cyan]")

def decor_line():
    decor = "-"*80
    console.print(f"[#8A2BE2]{decor}[/#8A2BE2]")

def decor1_color(message):
    console.print(f"\n[bold underline #FFAA33]{message}[/]")

def head_color(message):
    console.print(f"\n[bold underline #FF8C00]{message}[/]")

def text_color(message):
    console.print(f"[bold #FFBF00]{message}[/]")

def user_input(message):
    return console.input(f"[#00D9FF]{message}[/]").strip()

def ask_option_number():
    message = "Enter option number to proceed further : "
    return console.input(f"\n[#00D9FF]{message}[/]").strip()

def option_error():
    message = "Please enter valid option number from given options"
    error_message(message)

def progress_bar(val=1):
    for _ in track(range(30), description="Processing..."):
            time.sleep(0.1)

#------------------------------------------------
# PROGRAM START FROM HERE :
#------------------------------------------------

# DEFINING IMP FUNCTIONS USED IN THIS PROGRAM ---

def display_login_title():
    pass
if __name__ == "__main__":
    pass
    # while True:
    #     username = input("Enter Your Username : ")

def check_username(u):
    """
    Check the username whether it is in record or not.
    Parameters: u : Username of employee who have access to this program.
    Returns: str: "yes" for correct username, "no" for wrong username. 
    """

    with open(empls_data_path, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if (row and row[1] == u and "a" in row[5]):
                correct_message("Username Found")
                return "yes"
            
        error_message("Invalid Username!")


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
    with open(empls_data_path, "r") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            if (row and len(row)>1 and row[1] == u  and row[2] == p):
                correct_message("Logged in successfully!\n")
                return "yes"

        error_message("Wrong Password!\n")

def search_book():
    while True:
        decor_line()

        head_color("Available ways to search book(s) Or to check Unique Code of book(s):\n")
        text_color("\t1.By Name of Book -")
        text_color("\t2.By Name of Author of Book -")
        text_color("\t3.By Publishing Date of Book -\n")

        sel_option = user_input("Enter option number to proceed further : ")

        if sel_option == "1":
            check_by_book_name()
            break

        if sel_option == "2":
            check_by_author_name()
            break

        if sel_option == "3":
            check_by_publish_date()
            break

        else:
            error_message("Please enter valid option number from given options")

def check_by_book_name():
    while True:
        decor_line()
        value = False
        book_name = user_input("Enter name of books : ")

        wb = load_workbook(books_data_path)
        for sheet in wb.sheetnames:
            s = wb[sheet]
            for row in s.iter_rows(min_row=2,values_only=True):
                if book_name in str(row[2]).strip().lower():
                    info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                    decor_line()
                    value = True

        wb.save(books_data_path)

        if value:
            decor_line()
            break
        else:
            error_message("Book Not Found!")

def check_by_author_name():
    while True:
        decor_line()
        value = False
        author_name = user_input("Enter author name of book : ")

        wb = load_workbook(books_data_path)
        for sheet in wb.sheetnames:
            s = wb[sheet]
            for row in s.iter_rows(min_row=2,values_only=True):
                if author_name in str(row[3]).strip().lower():
                    info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                    decor_line()
                    value = True

        wb.save(books_data_path)

        if value:
            decor_line()
            break
        else:
            error_message("Book Not Found!")

def check_by_publish_date():
    while True:
        decor_line()
        value = False
        info_message("The date should be in format : dd-mm-yy \n")
        publish_date = user_input("Enter publishing date of book : ")

        wb = load_workbook(books_data_path)
        for sheet in wb.sheetnames:
            s = wb[sheet]
            for row in s.iter_rows(min_row=2,values_only=True):
                if publish_date in str(row[5]).strip().lower():
                    info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                    decor_line()
                    value = True

        wb.save(books_data_path)

        if value:
            decor_line()
            break
        else:
            error_message("Book Not Found!")

def buy_book():
    value = False
    decor_line()
    head_color("---Buy Book(s)---\n")
    uc = user_input("Enter Unique Code Of Book : ").upper()
    wb = load_workbook(books_data_path)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if uc == str(row[1]).strip():
                correct_message(f"{row[2]} : By {row[3]} : Rs.{row[7]} : Avail. {row[9]}\n")
                avail_q = row[9]
                value = True

    wb.save(books_data_path)

    if value:
        while True:
            value = False
            quantity = user_input("Enter quantity of this book : ")
            if int(quantity) <= int(avail_q) :
                correct_message("Book Sold Successfully!")
                
                wb = load_workbook(books_data_path)
                for sheet in wb.sheetnames:
                    s = wb[sheet]
                    for row in s.iter_rows(min_row=2,values_only=False):
                        row[9].value = int(row[9].value) - int(quantity)
                wb.save(books_data_path)

                while True:
                    head_color("Want to buy more book(s)?\n")
                    text_color("\t1.Yes")
                    text_color("\t2.No")

                    sel_option = ask_option_number()

                    if sel_option == "1":
                        buy_book()
                        break

                    elif sel_option == "2":
                        pass

                    else:
                        option_error()
                break
            elif int(quantity) <= 0:
                error_message("Please enter valid quantity")
            else:
                error_message("Insufficient quantity of book available!")
    else:
        error_message("Book Not Found!") 



def choose_option():
    while True:
        decor_line()
        head_color("Available Options :\n")

        info_message("\t1. Want to check unique code of book once ?")
        info_message("\t2. Buy book(s) directly\n")

        sel_option = user_input("Enter option number to proceed further : ")

        if sel_option == "1":
            search_book()
            break

        if sel_option == "2":
            buy_book()
            break
        else:
            error_message("Please enter valid option number from given options!")


def change_rate():
    wb = load_workbook(books_data_path)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=False):
            if row[6].value is None:
                continue
            row[6].value = int((int(row[7].value)) - int((int(row[7].value) * 30)/100))
            row[8].value = int((int(row[7].value) * 30)/100)
    wb.save(books_data_path)  



print(emoji.emojize(":bank:"))

decor_line()
head_color("Actions Available :\n")
text_color("\t1. Search book(s)")
text_color("\t2. Buy book(s)")
text_color("\t3. Exit")
decor_line()

while True:
    select_option = user_input("Enter option number from options : ")

    if select_option == "1":
        search_book()
        break
    if select_option == "2":
        buy_book()
        break

    if select_option == "3":
        break

    else:
        error_message("Please enter valid option nuber from above give options")

# def check_book_name():
#     while True:
#         print(decor2)
#         book_name = input(text_color + "Enter name of book : ").strip().lower()
#         value =  False # Initialising

#         wb = load_workbook(books_data_path, data_only=True)
#         for s in wb.worksheets:
#             for row in s.iter_rows(min_row=2,values_only=True):
#                 if book_name in str(row[2]).strip().lower():
#                     print(decor2)
#                     print(f"{row[1]} : {s.capitalize()} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}")
#                     value = True
        
#         if value:
#             print(decor2)
#             break
#         else : 
#             print(f"\n{error_color}⚠️  Book(s) with this name Not Found ! \n")



head_color("Hello World")
text_color("Hello World")
