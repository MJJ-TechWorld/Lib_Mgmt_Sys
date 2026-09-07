import csv

with open("students.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        if (len(row) == 4) and (row[2].lower() == "error"):
            with open("students_error.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(row)


with open("students_error.csv", "w", newline="") as file:
    writer = csv.writer(file)
    with open("students.csv", "r") as file:
        data = csv.reader(file)
        for row in data:
           if (len(row) == 4) and (row[2].lower() == "error"): 
                writer.writerow(row)


# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     for i in range(100):
#         writer.writerow(["id", "name", "course", "fees"])
#         writer.writerow([101, "Aman", ])
#         writer.writerow([102, "Riya", "Error", 18000])
#         writer.writerow([103, "Rahul", "Python", 15000])