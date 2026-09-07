import password_utils
password = input("Enter password for new user: ")
result = password_utils.check_password_strength(password)
print("Password Strength:", result)