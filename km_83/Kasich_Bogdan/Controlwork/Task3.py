from data import dataset
from Task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByProducts(user_email, product_list, amount_of_money = 0):

    if product_list==[]:
        return amount_of_money

    current_product_list = dataset[user_email][product_list[0]]
    amount_of_money += sum(current_product_list)



    return recursionByProducts(user_email,product_list[1:],amount_of_money)


def recursionByUsers(user_emails = list(dataset.keys()), result_dict = dict()):

    if user_emails == []:
        return result_dict

    user_email= user_emails[0]
    product_list = list(dataset[user_email].keys())
    money = recursionByProducts(user_email, product_list)

    result_dict[user_email] = money

    return recursionByUsers(user_emails[1:], result_dict)


print("Task 3")

result = recursionByUsers()
print(result)

print("\n\n")
