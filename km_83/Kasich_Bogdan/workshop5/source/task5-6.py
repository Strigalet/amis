from data import *

counting=[]
for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            counting.append(product)
dictos={}
for name in dataset:
    for date in dataset[name]:
        for product in dataset[name][date]:
            dictos[product]=counting.count(product)

list_keys=[]
list_values=[]
for key,value in dictos.items():
    list_keys.append(key)
    list_values.append(value)

for i in range(len(list_values)):
    if list_values[i]==min(list_values):
        print("The least popular product is", list_keys[i], "which was purchased",min(list_values), "times")
    if list_values[i]==max(list_values):
        print("The most popular product is",list_keys[i],"which was purchased",max(list_values),"times")


