import random
import string

def generate_password(length):
    # Define the character set to include uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly choosing characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user to enter the desired password length
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Generated password:", password)
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__k":
    main()