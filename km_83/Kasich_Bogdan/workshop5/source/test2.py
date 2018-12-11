from data_for_911 import dataset
import plotly
import plotly.graph_objs as go
# Диаграмма количества конкретных проишествий
incidents=[]
quantity_of_incidents=[]
for description in dataset:
    if dataset[description]["title"] not in incidents:
        incidents.append(dataset[description]["title"])

for incident in incidents:
    counter=0
    for description in dataset:
        if incident==dataset[description]["title"]:
            counter+=1

    quantity_of_incidents.append(counter)

diagram=[go.Bar(x=incidents,y=quantity_of_incidents)]
plotly.offline.plot(diagram,filename="quantity_of_incidents.html")