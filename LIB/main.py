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

books_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\books_data.xlsx"
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
    console.print("[bold cyan]✅ {message}[/bold cyan]")



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
    while True:
        username = input("Enter Your Username : ")

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