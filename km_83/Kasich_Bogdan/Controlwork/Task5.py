from data import dataset
from Task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: якого товару на яку суму продано.

data = dict()
for user_email in list (dataset.keys()):
    for product, products_list in (dataset[user_email]).items():
        if product in data:
            data[product] += sum(products_list)
        else:
            data[product] = sum(products_list)
print(data)

diagram = go.Pie(labels=list(data.keys()), values=list( data.values()))

plotly.offline.plot([diagram], filename='products.html')
