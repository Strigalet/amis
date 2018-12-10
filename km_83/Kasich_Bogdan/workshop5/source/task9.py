from data import *

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

importing_new(dataset,"Gleb","10.01.2019","chocolate",3,45)
importing_new(dataset,"Jane","12.11.2018","milk",2,30)
importing_new(dataset,"Mike","16.11.2018","meat",17,150)
importing_new(dataset,"John","24.10.2018","apple",2,6)
for value in dataset.values():
    print(value)