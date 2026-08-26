# import csv
# #from csv import * NONONONO

# with open("students_sample.csv", "r") as file:
#     data = csv.reader(file)
#     count = 0
#     for row in data:
#         if row[2] == "Python":
#             print(row[1])
        

import csv

total = 0

with open("students_sample.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        total = total + int(row[4])

print("Total Fees:", total)        


