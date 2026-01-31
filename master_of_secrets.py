# TODO: password generator with entropy
#  - ask users for input - done
#  - generates password - done
#  - generates chart to show password strength

import secrets
import string

def main():
    generate_password()

def get_user_input():
    print("Greetings, The Master of Secrets is at your service!")
    user_input = input("Would you like to know a secret? (Yes/No): ")
    return user_input

def generate_password():
    user_input = get_user_input()
    if user_input == "Yes":
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for i in range(16)).encode()
        return password
    elif user_input == "No":
        print ("Come back soon!")
    return None

def display_strength():
    pass

main()