import random
import string

def generate_password(length):
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
   
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

       
        password = generate_password(length)

       
        print("Generated password:", password)
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__k":
    main()
