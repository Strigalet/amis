from data import *
from validators.lib_purch import *


def importing_new(dataset,name,date,product,quantity,price):
    if name in dataset:
        if date in dataset[name]:
                dataset[name][date][product] = {'quantity': quantity,
                                                'price': price}
        else:
            dataset[name][date] = {product: {'quantity': quantity,
                                             'price': price}}
    else:
        dataset[name] = {date: {product: {'quantity': quantity,
                                          'price': price}}}

def addPurchaseValidator():

    name=get_name()
    while not name:
        print("Print correct data:" )
        name = get_name()

    date=get_date()
    while not date:
        print("Print correct data:" )
        date = get_date()

    product=get_product()
    while not product:
        print("Print correct data:" )
        product = get_product()

    quantity = get_quantity()
    while not quantity:
        print("Print correct data:")
        quantity = get_quantity()

    price = get_price()
    while not date:
        print("Print correct data:")
        price = get_price()

    importing_new(dataset, name, date, product, quantity, price)


addPurchaseValidator()
for key,value in dataset.items():
    print(key,value)

