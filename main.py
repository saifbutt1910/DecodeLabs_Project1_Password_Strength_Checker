print("Password Strength Checker")
print("-------------------------")

password = input("Enter your password: ")

# Check for empty password
if password.strip() == "":
    print("\nWarning: Password cannot be empty or only spaces.")

# Check for commonl passwords
common_passwords = [
    "password",
    "12345678",
    "qwerty123",
    "admin123",
    "password123"
]

if password.lower() in common_passwords:
    print("\nWarning: This is a commonly used password!")

# Security checks
length_ok = len(password) >= 8
has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

print("\nPassword checks:")
print("Length (8+):", length_ok)
print("Uppercase:", has_uppercase)
print("Number:", has_number)
print("Symbol:", has_symbol)

# Calculate score
score = 0

if length_ok:
    score += 1

if has_uppercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

print("\nScore:", score, "/ 4")

# Check password strength
if score <= 1:
    strength = "Weak"
elif score <= 3:
    strength = "Medium"
else:
    strength = "Strong"

print("\nResult:", strength)

# Security recommendation
if strength == "Weak":
    print("Suggestion: Use a longer password with uppercase letters, numbers, and symbols.")
elif strength == "Medium":
    print("Suggestion: Add more character variety to improve your password.")
else:
    print("Good job! Your password meets all four security checks.")