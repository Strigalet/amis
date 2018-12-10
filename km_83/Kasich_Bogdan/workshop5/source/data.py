file = open('data/orders.csv')

info = file.read()

lines = info.splitlines()
dataset = dict()

people = []
for client in lines[1:]:
    people.append(client.split(', '))


for client in people:
    name = client[0]
    date = client[1]
    product = client[2]
    quantity = client[3]
    price = client[4]
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




file.close()

