import re

def get_latitude():

    user_input = input("Print the latitude: ")

    if re.match(r"^-?\d{1,2}\.\d+$", user_input):
        return user_input
    else:
        return False




def get_longtitude():

    user_input = input("Print the longtitude: ")

    if re.match(r"^-?\d{1,3}\.\d+$", user_input):
        return user_input
    else:
        return False



def get_zip_code():

    user_input = input("Print the zip_code: ")

    if re.match(r"^\d{5}$", user_input):
        return user_input
    else:
        return False



def get_title():
    user_input=input("Print the title of incident: ")

    if re.match(r"^[A-Z]+[a-z]*\:\s[A-Z]+[A-Z,\s]*\-?$", user_input):
        return user_input
    else:
        return False

def get_date():
    user_input = input("Print the date: ")

    if re.match(r"^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$", user_input):
        return user_input
    else:
        return False

def get_time():
    user_input=input("Print the time: ")

    if re.match(r"^([0-1]\d|2[0-3])(:[0-5]\d){2}$",user_input):
        return user_input
    else:
        return False
def get_town():
    user_input = input("Print the town: ")

    if re.match(r"^[A-Z]+$", user_input):
        return user_input
    else:
        return False

def get_address():
    user_input = input("Print the address: ")

    if re.match(r"^[A-Z]+[A-Z,\s]*\-?\&?[A-Z,\s]*$", user_input):
        return user_input
    else:
        return False

def get_station():
    user_input = input("Print the station number: ")

    if re.match(r"^\d+[A-Z]$", user_input):
        return user_input
    else:
        return False
"""
print(get_latitude())
print(get_longtitude())
print(get_zip_code())
print(get_title())
print(get_date())
print(get_time())
print(get_town())
print(get_address())
print(get_station())
"""