from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct(user_name, product_name, product_price):

    #   Якщо є інформація про користувача у dataset
    if user_name in dataset:

        #   Якщо користувач вже купляв цей товар раніше, отримуємо список покупок та додаємо покупку
        if product_name in dataset[user_name]:
            product_list = dataset[user_name][product_name]
            product_list.append(product_price)

        #   Якщо користувач не купляв цей товар раніше - створюємо список
        else:
            dataset[user_name][product_name] = [product_price]

    #   Якщо інформація відсутня - створюємо нову структуру і словник для запису інформації про покупку
    else:
        dataset[user_name] = { product_name: [product_price] }


print("Task 1")

#Додати нового користувача та нову покупку
addUserProduct("b.bober@kpi.ua","cake",42.50)

#Додати існуючому користувачу нову покупку нового продукту
addUserProduct("b.bober@kpi.ua","fish",12.00)

#Додати існуючому користувачу нову покупку існуючого продукту
addUserProduct("b.bober@kpi.ua","cake",24.00)

print(dataset)


print("\n\n")