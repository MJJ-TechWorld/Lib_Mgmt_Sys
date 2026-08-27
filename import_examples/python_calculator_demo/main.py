from banner import show_banner
from calculator import calculate
from validator import get_number


show_banner()

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice: ")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

result = calculate(num1, num2, choice)

print(f"Result: {result}")