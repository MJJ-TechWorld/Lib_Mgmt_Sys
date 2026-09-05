import openpyxl
import os
from rich.console import Console
from pyfiglet import figlet_format
console = Console()



#INITIALIZATION
file_name = "bank_records_1.xlsx"
bank_name = figlet_format("PY BANK", font="slant") 

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
        if choice == "3":
            break      
