from data import *
import plotly
import plotly.graph_objs as go

products=set()
for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            products.add(product)
product_list=[]
quantity_list=[]
for product in products:
    counter=0
    for name in dataset:
        for date in dataset[name]:
            if product in dataset[name][date]:
                counter+=1
                break
    print("The",product,"was purchased by",counter,"people")
    product_list.append(product)
    quantity_list.append(counter)

graph=[go.Bar(x=product_list,y=quantity_list)]
plotly.offline.plot(graph,filename="quantity_of_purchasing.html")

