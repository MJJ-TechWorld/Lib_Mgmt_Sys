
def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong"
    return "Weak"


pwd = input("Enter your password")
result = check_password_strength(pwd)

print("Strength of Password is :: ", result)