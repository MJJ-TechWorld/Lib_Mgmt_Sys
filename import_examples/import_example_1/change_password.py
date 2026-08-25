import password_utils 
password = input("Enter New password ")
result = password_utils.check_password_strength(password)
print("Password Strength:", result)