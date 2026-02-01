# TODO: password generator with entropy
#  - ask users for input - done
#  - generates password - done
#  - generates chart to show password strength

import secrets
import string
import numpy as np
from scipy.stats import entropy


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
        password = ''.join(secrets.choice(characters) for i in range(20))
        return password
    elif user_input == "No":
        print ("Come back soon!")
    return None


def calculate_password_entropy():
    password = generate_password()
    chars, counts = np.unique(list(password), return_counts=True)
    probabilities = counts / len(password)
    ent = entropy(probabilities, base=2)
    return ent


def display_strength():
    pass

main()