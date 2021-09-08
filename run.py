from user import User
from credentials import Credentials
import random
import string

user_data =None
Credentials_data = None
def signup(user_name, password, email, p_number):
    user_data = User(user_name, password, email, p_number)
    return user_data

def main():
    print("Hello, Welcome to your password locker.  What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print("\n")


