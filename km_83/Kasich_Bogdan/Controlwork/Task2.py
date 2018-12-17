from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators import getProductPrice
from validators import getProductName
from validators import getUserEmail


from Task1 import addUserProduct


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserProductValidator():

    user_email = getUserEmail()
    while not user_email:
        print("Error in email. Try again")
        user_email = getUserEmail()


    product_name = getProductName()
    while not product_name:
        print("Error in product name. Try again")
        product_name = getProductName()


    product_price_str = getProductPrice()
    while not product_price_str:
        print("Error in product price. Try again")
        product_price_str = getProductPrice()

    product_price = float (product_price_str)

    addUserProduct(user_email, product_name, product_price)



print("Task 1")
addUserProductValidator()
print(dataset)


print("\n\n")