from data_for_911 import dataset
import plotly
import plotly.graph_objs as go

# Cколько в каждом городе было инцидентов
towns=[]
quantity_of_incidents=[]
for description in dataset:
    if dataset[description]["town"] not in towns:
        towns.append(dataset[description]["town"])

for town in towns:
    counter=0
    for description in dataset:
        if town==dataset[description]["town"]:
            counter+=1
    quantity_of_incidents.append(counter)

diagram=[go.Bar(x=towns,y=quantity_of_incidents)]
plotly.offline.plot(diagram,filename="incidents_in_towns.html")