import string

# Common weak words and patterns blacklist
BLACKLIST = {
    "password",
    "welcome",
    "admin",
    "birthday",
    "name",
    "user",
    "qwerty",
    "abc",
    "1234",
    "0000"
}

password = input("Enter Password: ")

# Minimum length check
if len(password) < 8:
    print("\n❌ WEAK PASSWORD")
    print("Reason: Password must contain at least 8 characters.")
    exit()

# Blacklist check
password_lower = password.lower()

for word in BLACKLIST:
    if word in password_lower:
        print("\n❌ WEAK PASSWORD")
        print(f"Reason: Password contains a common weak pattern ('{word}').")
        exit()

# Character checks
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

# Strength score
score = 0

if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1
if len(password) >= 12:
    score += 1

# Classification
if score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

# Report
print("\n========== PASSWORD SECURITY REPORT ==========")
print(f"Password Length : {len(password)}")
print(f"Uppercase       : {'✔ Present' if has_upper else '✘ Missing'}")
print(f"Lowercase       : {'✔ Present' if has_lower else '✘ Missing'}")
print(f"Numbers         : {'✔ Present' if has_digit else '✘ Missing'}")
print(f"Special Symbols : {'✔ Present' if has_symbol else '✘ Missing'}")
print(f"Length ≥ 12     : {'✔ Yes' if len(password) >= 12 else '✘ No'}")

print(f"\n🔐 Password Strength: {strength}")

# Suggestions
if strength != "STRONG":
    print("\nSuggestions to Improve Security:")

    if not has_upper:
        print("- Add at least one uppercase letter.")

    if not has_lower:
        print("- Add at least one lowercase letter.")

    if not has_digit:
        print("- Add at least one number.")

    if not has_symbol:
        print("- Add at least one special symbol.")

    if len(password) < 12:
        print("- Increase password length to 12 or more characters.")

print("\n==============================================")
