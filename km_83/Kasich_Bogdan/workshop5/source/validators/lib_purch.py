import re

def get_name():
    user_input = input("Print the name: ")

    if re.match(r"^[A-Z][a-z]+$", user_input):
        return user_input
    else:
        return False

def get_date():
    user_input = input("Print the date: ")

    if re.match(r"^(0[1-9]|1[0-9]|2[0-9]|3[01])\.(0[1-9]|1[012])\.[0-9]{4}$", user_input):
        return user_input
    else:
        return False

def get_product():
    user_input = input("Print the product: ")

    if re.match(r"^[a-z]+$", user_input):
        return user_input
    else:
        return False

def get_quantity():
    user_input = input("Print the quantity: ")

    if re.match(r"^(\d+|\d+\.\d+)$", user_input):
        return user_input
    else:
        return False

def get_price():
    user_input = input("Print the price: ")

    if re.match(r"^(\d+|\d+\.\d+)$", user_input):
        return user_input
    else:
        return False