import random
import string


def generate_password(length):
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# User Input
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 for security.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:", password)
except ValueError:
    print("Please enter a valid number.")
