from registration import *

def check():
    print("Check login")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    for user in userData:
        if name == user["name"] and password == user["password"]:
            return True
    return False
