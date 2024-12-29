  
password = input("Make Password: ")
print(f"You entered: {password}")


if len(password) >= 8:
    print("password length is good")
else:
    print("its to short")


has_upper = any(char.isupper() for char in password)
if has_upper:
    print("password got 1 uppercase")
else:
    print("no upper case")

has_lower = any(char.islower () for char in password)
if has_lower:
    print("password got lowercase letters")
else:
    print("no lowercase")


has_digit = any(char.isdigit () for char in password)
if has_digit:
    print("password got has numbers")
else:
    print("no numbers")

special_characters = ("!@#$%^&*()-_=+[]{};:'\",.<>?/")

has_special = any(char in special_characters for char in password)
if has_special:
    print("password got special characters")
else:
    print("no special characters")

has_upper = any(char.isupper() for char in password)  # Uppercase letters
has_lower = any(char.islower() for char in password)  # Lowercase letters
has_digit = any(char.isdigit() for char in password)  # Numbers
special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/"
has_special = any(char in special_characters for char in password)
score = sum([len(password) >= 8, has_upper, has_lower, has_digit, has_special])

if score == 5:
    print("password strength: strong")
elif 3 <= score < 5:
     print("password strength: moderate ")
else:
    print("Password strength: Weak")
