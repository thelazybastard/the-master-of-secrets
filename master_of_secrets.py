# TODO: password generator with entropy
#  - ask users for input - done
#  - generates password - done
#  - hashes password

import secrets
import string
import hashlib

def main():
    get_user_input()

def get_user_input():
    print("Greetings, The Master of Secrets is at your service!")
    user_input = input("Would you like to know a secret?")

def generate_password():

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for i in range(32))



main()