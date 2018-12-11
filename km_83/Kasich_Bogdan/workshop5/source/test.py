from data_for_911 import dataset

# Количество транспортных проишествий
counter=0
for description in dataset:
    if "Traffic" in dataset[description]["title"]:
        counter+=1

print("The quantity of traffic incidents is",counter)
