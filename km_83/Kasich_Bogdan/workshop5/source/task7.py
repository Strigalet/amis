from data import *

dictilio={}
for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            if product in dictilio:
                if date > dictilio[product]["date"]:
                    dictilio[product] = {'price': float(dataset[name][date][product]["price"]) / float(dataset[name][date][product]["quantity"]),
                                         'date': date}
            else:
                dictilio[product]={'price': float(dataset[name][date][product]["price"])/float(dataset[name][date][product]["quantity"]),
                                  'date': date}



prices=[]
for key in dictilio.keys():
    prices.append(dictilio[key]["price"])

for product in dictilio:
    if dictilio[product]["price"]==max(prices):
        print("The most expensive product is",product,"with the cost of",max(prices))