import openpyxl,os,time
import uuid
from rich.console import Console
from rich.progress import track
from pyfiglet import figlet_format
from pwinput import pwinput
from datetime import datetime
console = Console()



#INITIALIZATION
file_name = "bank_records_1.xlsx"
bank_name = figlet_format("PY BANK", font="slant") 

#==========================================================
# PROGRESS BAR 3 SEC
#==========================================================
def progress_bar(val=1):
    for _ in track(range(val), description="Processing..."):
        time.sleep(1)

#==========================================================
# Current date and Time 
#==========================================================
def cur_date():
    now = datetime.now()
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_1 = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_1
    #print("Format 1:", formatted_1)  # Output: 2026-09-05 22:00:00





#==========================================================
# Excel Creation function
#==========================================================
def create_excel_file():
    """This functions Creates a excel named bank_records_1.xlsx IF it does not exists"""
    if  not os.path.exists(file_name):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Bank Records"
        headers = ["Account No","Name","PIN","Transaction ID","Transaction Type","Amount",
                "Previous Balance","Current Balance","Date-Time"]

        sheet.append(headers)

        # for i in range(1,10):
        #     sheet.cell(row=2, column=i).value = "abc"
        # # sheet["A1"].value = ""
        # sheet["B1"].value = ""

        wb.save(file_name)
        wb.close()
        console.print("[bold cyan]Excel database Created Successfully [/bold cyan]")

#==========================================================
# Error Message
#==========================================================
def err_msg(error):
    console.print(f"[bold red] Invalid {error} Try again [/bold red]")

#==========================================================
# Create Account
#==========================================================

def create_account():
    console.print("\n[bold yellow] Create Account [/bold yellow]")
    name = input("Enter your name")
    acc_nr = input("Enter Account Number")

    if not acc_nr.isdigit():
        err_msg("Account Number")
        return
    if acc_nr == "exists":
        pass

    pin = pwinput("CREATE A 4 DIGIT PIN: ", mask="*")

    if len(pin) != 4 or not pin.isdigit():
        err_msg("PIN")
        return

    try:
        amount = float(input("Enter a Opening Balance"))
        if amount < 0:
            err_msg("Opening balance")
            return
    except ValueError:
        err_msg("Value Entered")
        return
    transaction_id = str(uuid.uuid4())[:8]
    status = "Opening"
    dt = cur_date()

    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active
    sheet.append([acc_nr,name,pin,transaction_id,status,amount,0,amount,dt])
    wb.save(file_name)
    wb.close()

    progress_bar(5)

    console.print("[bold yellow] Account Created Succefully [/bold yellow]")

#==========================================================
# CHECK BALANCE
#==========================================================
def check_balance(acc_nr):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2,values_only=True):
            if (row[0]  == acc_nr):
                amount = row[7]

    console.print(f"[bold magenta] YOUR BALANCE IS {amount} [/bold magenta]")
                
    
    wb.close()


#==========================================================
# SUB MENU 
#==========================================================
def sub_menu(acc_nr):
    while True:
        console.print("""BANKING OPTIONS
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        4. Transaction History
        5. Logout
        """)
        choice = input("Enter Choice")

        if choice == "1":
            check_balance(acc_nr)
        elif choice == "2":
            dep_money(acc_nr)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            err_msg("CHOICE")
        
#==========================================================

#==========================================================
#   LOGIN
#==========================================================
def login():
    console.print("[bold yellow] LOGIN [/bold yellow]")
    acc_nr = input("Enter Account Number")
    pin = pwinput("enter your pin", mask="*")
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active
    for row in sheet.iter_rows(min_row=2, max_col=3,values_only=True):
        if (row[0]  == acc_nr)  and (row[-1] == pin ) :
            user_name = row[1]
            break
    wb.close()
    console.print("Verifying Account ....")
    progress_bar(5)
    console.print("[bold green]LOGIN SUCCESSFULL [/bold green]")
    console.print(f"Welcome [cyan] {user_name} [/cyan]")
    print()
    sub_menu(acc_nr)
    console.print("[bold magenta] Thank You Visit Again [/bold magenta]")



#==========================================================
#   MAIN PROGRAM
#==========================================================

if __name__ == "__main__":
    create_excel_file()
    while True:
        console.print(f"[green] {bank_name} [/green]")
        print()
        console.print("[bold cyan] Welcome to Python Banking System [/bold cyan]")
        print("""1. Create Account
2. Login
3. Exit""")
        print()
        choice = console.input("[bold purple]Enter Your Choice : [/bold purple]") 

        if choice == "1":
            create_account()     
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            err_msg("CHOICE")
            

