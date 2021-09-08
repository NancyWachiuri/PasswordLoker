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


    while True:
        print("Use these short codes : su - create a new password locker account, lg - login to password")

        short_code = input().lower()

        if short_code == 'su':
            print ("Input your username ....")
            user_name = input()

            print("Input your email address...")
            email= input()

            print("Phone number ...")
            p_number = input()

            print("Do you want to the app to generate a password for you?")
            print("y - yes, n - no ")

            short_code_gen = input().lower()

            if(short_code_gen =="y"):
                password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

            else:
                print("Input the password...")
                password = input()