from operations import add, subtract, multiply, divide


def calculate(a, b, choice):

    if choice == "1":
        return add(a, b)

    elif choice == "2":
        return subtract(a, b)

    elif choice == "3":
        return multiply(a, b)

    elif choice == "4":

        if b == 0:
            return "Cannot divide by zero"

        return divide(a, b)

    else:
        return "Invalid choice"