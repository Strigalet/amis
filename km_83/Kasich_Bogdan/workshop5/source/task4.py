from data import *
import plotly
import plotly.graph_objs as go

dicti={}
for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            if name in dicti:
                dicti[name]+=float(dataset[name][date][product]["price"])
            else:
                dicti[name]=float(dataset[name][date][product]["price"])

print(dicti)

diagram = [go.Bar(x=list(dicti.keys()),
                  y=list(dicti.values()))]
plotly.offline.plot(diagram,filename="prices.html")