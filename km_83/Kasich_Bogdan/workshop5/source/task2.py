from data import dataset

def setting(sets,result):
    if len(sets)==0:
        return result
    result=result&sets[0]
    return setting(sets[1:],result)
for key,value in dataset.items():
    print(key,value)
sets=[set() for i in range(len(dataset))]
i=0
for name in dataset:
    main_set=set()
    for date in dataset[name]:
        for product in dataset[name][date]:
            main_set.add(product)
    sets[i]=main_set.union(sets[i])
    i+=1
print(sets)
rezik=setting(sets,sets[0])
for i in rezik:
    print("Each person bought",i)


