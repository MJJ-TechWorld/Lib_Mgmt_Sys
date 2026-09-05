# # import os

# # var = os.path.exists(r"C:\Users\Sanky\Desktop\training_Python_batch1\Build_day\Banking App\bank_record.xlsx")

# # print(var)




# # if not (1 == 1): #if not (True) #if False
# #     print("ok")
# # else:
# #     print("NOk")


from rich.console import Console 


console = Console()

print("Login Successful")
console.print("1")
# console.print("[bold green]Login Successful[/bold green]")
# console.print("[cyan]Current Balance: ₹5000[/cyan]")



# from pyfiglet import figlet_format
# var = figlet_format("ABC BANK", font="slant")

# console.print(f"[green]{var}[/green]")


# import emoji

# print(emoji.emojize(":bank:"))
# print(emoji.emojize(":credit_card:"))
# print(emoji.emojize(":money_bag:"))
# print(emoji.emojize(":dollar:"))

# # from getpass import getpass

# # dum = getpass("Enter PIN: ")

# # print(type(dum))
# # print(dum)


# from pwinput import pwinput
# pin = pwinput("Enter PIN: ", mask="*")

# print(pin)



from rich.progress import track
import time

for _ in track(range(30), description="Processing..."):
        time.sleep(0.01)

import uuid

print(str(uuid.uuid4())[:8])
