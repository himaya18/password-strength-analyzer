import re
common_passwords = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "abc123",
    "password123",
    "admin",
    "welcome",
    "letmein"
}
def analyze_password(password):
    score = 0
    suggestions = []
    if password.lower() in common_passwords:
        return "Weak", ["Your password is a common/weak password. Choose a unique password."]
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character such as @, #, $, or !.")
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    return strength, suggestions

password = input("Enter your password: ")

strength, suggestions = analyze_password(password)

print("\n----- Password Strength Analyzer -----")
print("Password length:", len(password))
print("Strength:", strength)

print("\nPassword Checks:")
print("Uppercase:", "Yes" if re.search(r"[A-Z]", password) else "No")
print("Lowercase:", "Yes" if re.search(r"[a-z]", password) else "No")
print("Numbers:", "Yes" if re.search(r"[0-9]", password) else "No")
print("Special characters:", "Yes" if re.search(r"[^A-Za-z0-9]", password) else "No")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password meets all the basic strength requirements!")
