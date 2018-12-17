from data_for_911 import dataset

# Адреса , которые не сопровождены почтовым индексом, и их количество , чичество
counter=0
for description in dataset:
    if dataset[description]["zip_code"]=="":
        print(dataset[description]["address"])
        counter+=1

print("The amount of people without zip_code is",counter)