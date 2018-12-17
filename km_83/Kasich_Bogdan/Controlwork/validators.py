"""
    Написати валідатор email у домені @kpi.ua:
    Перша літера англійської абетки у нижньому регістрі, далі стоїть крапка потім прізвище студента.
"""

import re

def getUserEmail():

    user_input = input("Enter your KPI email:\n")

    if (re.match(r"^[a-z]\.[a-z]+@kpi\.ua$", user_input) ):
        return user_input
    else:
        return False



"""
    Написати валідатор product name:
    не більше 10 літер англійської абетки у нижньому регістрі.
"""

def getProductName():

    user_input = input("Enter your product name:\n")

    if (re.match(r"^[a-z]{1,10}$", user_input)):
        return user_input
    else:
        return False


"""
    Написати валідатор price: додатне дійсне число з двома знаками після десяткової коми
"""


def getProductPrice():

    user_input = input("Enter product price:\n")

    if (re.match(r"^\d+\.\d{2}$", user_input)):
        return user_input
    else:
        return False