import openpyxl
try:
    wb = openpyxl.load_workbook("students_copy.xlsx")
    sheet = wb["Students"]
    print(type(sheet["A2"].value))
except FileNotFoundError:
    print("File Nathi")
finally:
    wb.close()
