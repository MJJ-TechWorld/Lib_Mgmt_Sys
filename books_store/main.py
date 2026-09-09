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
    console.print("[bold red]⚠️ {error}[/bold red]")

def info_message(message):
    console.print("[cyan]{message}[/cyan]")

def correct_message(message):
    console.print(f"[bold cyan]✅ {message}[/bold cyan]")

def decor_color():
    decor = "-"*80
    console.print(f"[#8A2BE2]{decor}[/#8A2BE2]")

def decor1_color(message):
    console.print(f"[bold underline #FFAA33]{message}[/]")

def head_color(message):
    console.print(f"[bold underline #FF8C00]{message}[/]")

def text_color(message):
    console.print(f"[bold #FFBF00]{message}[/]")

def user_input(message):
    return console.input(f"[#00D9FF]{message}[/]").strip()

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


def check_by_book_name():
    while True:
        value = False
        book_name = user_input("Enter name of books : ")

        wb = load_workbook(books_data_path)
        for sheet in wb.sheetnames:
            s = wb[sheet]
            for row in s.iter_rows(min_row=2,values_only=True):
                if book_name in str(row[2]).strip().lower():
                    text_color(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[8]} : Price {row[7]}")
                    value = True

        wb.save(books_data_path)

        if value:
            break


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


decor_color()
head_color("Actions Available :\n")
text_color("\t1. Search book(s)")
text_color("\t2. Buy book(s)")
decor_color()

while True:
    sel_option = user_input("Enter option number from options : ")

    if sel_option == "1":
        check_by_book_name()
        break
    if sel_option == "2":
        break


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
