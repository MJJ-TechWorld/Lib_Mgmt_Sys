import openpyxl
try:
    wb = openpyxl.load_workbook("students_copy.xlsx")
    wb1 = openpyxl.load_workbook("students_copy_1.xlsx")
    sheet = wb["Students"]
    sheet_1 = wb["Sheet1"]

    total = 0
    
    # for i in range(2,22):
    #     total = total + int(sheet[f"E{i}"].value)
    #     #print(wb["Students"]["A2"].value)

    # for row in sheet.iter_rows(min_row=2,max_row=10,min_col=2, max_col=6,values_only=True):
    #     if row[-1] > 80:
    #         print(f"{row[0]:<50}         {row[1]:>20}")
    #         print(row)
    total = 0
    for row in sheet.iter_rows(min_row=2,min_col=2, max_col=6,values_only=True):
        if row[0] is None:
            pass
        else:
            total = total + row[-2]
    sheet["E22"].value = total

    wb.save("students_copy.xlsx")
    wb.close()
except FileNotFoundError:
    print("File Nathi")
finally:
    wb.close()

print("Total Fee Collected is :: ", total)



# git rm --cached shubham.txt
# git commit -m "removed shubham.tx"

# git push origin main 

# git add  shubham.txt
# git commit -m "removed shubham.tx"

# git push origin main 


# builtin in scope aur nonlocal keyword 1 bar batana

