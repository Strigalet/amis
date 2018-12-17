from data import dataset
from Task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки грошей витратив.

data = {}
for user_email in list (dataset.keys()):
    for product, product_list in dataset[user_email].items():
        if user_email in data:
            data[user_email] += sum(product_list)
        else:
            data[user_email] = sum(product_list)

print(data)

diagram = go.Bar(
    x=list(data.keys()),
    y=list(data.values())
)

fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='user expenses.html')