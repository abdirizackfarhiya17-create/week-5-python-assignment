import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        # Missing line filled: Add one random character from characters to password
        password += random.choice(characters)
    return password

# Make one password using the default length, and one with a length of 12
p1 = make_password()
p2 = make_password(12)

# Print each password and its length
print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))
