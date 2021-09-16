from user import User
from credentials import Credentials
import random
import string

user_data =None
credentials_data = None
def signup(user_name, password, email, p_number):
    user_data = User(user_name, password, email, p_number)
    return user_data

def main():
    print("Hello, Welcome to your password locker.  What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print("\n")


    while True:
        print("Use these short codes : su - create a new password locker account, lg - login to password locker account, ex - exit the contact list")

        short_code = input().lower()

        if short_code == 'su':
            print ("Input your username ...")
            user_name = input()

            print("Input your email address...")
            email= input()

            print("Phone number ...")
            p_number = input()

            print("Do you want to the app to generate a password for you?")
            print("y - yes, n - no ")

            short_code_gen = input().lower()
            
            if(short_code_gen == "y"):
                password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

            else:
                print("Input the password...")
                password = input()

            user_data = signup(user_name, password, email, p_number)
            print('\n')
            print(user_data.username +" have successfully created and account with the password "+ user_data.password)

        elif short_code == 'lg':
            print('\n')
            print("Welcome to the login page")
            print('\n')

            print ("Input your username....")
            login_user_name = input()

            print ("Input your password...")
            login_password = input()

            if (login_user_name == user_data.username and login_password == user_data.password):
                print ("You are successfully logged in")
            else:
                print("Wrong credentials")
            while True:
             print("Use these short codes : cc - create credentials, dc - Display credentials, ex - exit")
             short_code2 = input().lower()
             if short_code2 == 'cc':
                 print("Input the website name ....")
                 website_name = input()

                 print("Input the website name email address ....")
                 website_email = input()

                 print("Do you want the app to generate a password for you?")
                 print("y - yes, n - no")

                 short_code_gen = input().lower()

                 if (short_code_gen == "y"):
                     password = input()

                 else:
                     print("Input the password...")
                     password= input()

                     credentials_data = Credentials(website_name, website_email, password)
                     credentials_data.add_credentials()

             elif short_code2 == 'dc':
                for item in credentials_data.credentials:
                    print("Here is the website" + item.website_name)
             else:
                 print("Thank you for visiting our website")

        else:
            break


if __name__ == "__main__":
    main()





