import password_utils

pwd = input("Enter your password")
result = password_utils.check_password_strength(pwd)

print("Strength of Password is :: ", result)
