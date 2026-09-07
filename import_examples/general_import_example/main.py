while True:

    print("\n==============================")
    print("     PYTHON IMPORT DEMO")
    print("==============================")

    print("1. Math Module")
    print("2. From Math Import")
    print("3. Random Module")
    print("4. Date and Time Module")
    print("5. Calendar Module")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # ----------------------------------
    # 1. MATH MODULE
    # ----------------------------------

    if choice == "1":

        import math

        print("\n--- MATH MODULE ---")

        print("Square Root of 100:", math.sqrt(100))
        print("Factorial of 5:", math.factorial(5))
        print("Value of Pi:", math.pi)
        print("Ceil of 4.2:", math.ceil(4.2))
        print("Floor of 4.9:", math.floor(4.9))


    # ----------------------------------
    # 2. FROM MATH IMPORT
    # ----------------------------------

    elif choice == "2":

        from math import sqrt, factorial

        print("\n--- FROM MATH IMPORT ---")

        print("Square Root of 100:", sqrt(100))
        print("Factorial of 5:", factorial(5))

        print("\nNotice:")
        print("Here we can directly use sqrt() and factorial()")
        print("because we imported them specifically.")


    # ----------------------------------
    # 3. RANDOM MODULE
    # ----------------------------------

    elif choice == "3":

        import random

        print("\n--- RANDOM MODULE ---")

        print("Random Number 1 to 10:")
        print(random.randint(1, 10))

        print("\nDice Roll:")
        dice = random.randint(1, 6)
        print(dice)

        print("\nRandom Student:")

        students = ["Aman", "Riya", "Sneha", "Rahul"]

        print(random.choice(students))

        print("\nRandom OTP:")

        otp = random.randint(1000, 9999)

        print(f"Your OTP is: {otp}")


    # ----------------------------------
    # 4. DATETIME MODULE
    # ----------------------------------

    elif choice == "4":

        from datetime import datetime

        print("\n--- DATE AND TIME ---")

        now = datetime.now()

        print("Current Date and Time:", now)
        print("Current Year:", now.year)
        print("Current Month:", now.month)
        print("Current Day:", now.day)

        print(
            "Formatted Date:",
            now.strftime("%d-%m-%Y")
        )


    # ----------------------------------
    # 5. CALENDAR MODULE
    # ----------------------------------

    elif choice == "5":

        import calendar

        print("\n--- CALENDAR MODULE ---")

        year = int(input("Enter year: "))
        month = int(input("Enter month: "))

        print("\nSelected Month:\n")

        print(calendar.month(year, month))

        show_year = input(
            "Do you want to see the complete year calendar? (yes/no): "
        )

        if show_year.lower() == "yes":

            print(calendar.calendar(year))


    # ----------------------------------
    # 6. EXIT
    # ----------------------------------

    elif choice == "6":

        print("\nProgram ended.")
        break


    # ----------------------------------
    # INVALID CHOICE
    # ----------------------------------

    else:

        print("\nInvalid choice. Please enter 1-6.")


