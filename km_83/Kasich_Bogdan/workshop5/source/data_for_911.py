file = open('data/911.csv')

info = file.read()

lines = info.splitlines()
dataset = dict()

calls=[]
for call in lines[1:]:
    calls.append(call.split(','))

for call in calls:
    latitude=call[0]
    longtitude=call[1]
    description=call[2]
    zip_code=call[3]
    title=call[4]
    date_and_time=call[5]
    town=call[6]
    address=call[7]
    dataset[description] = {
        "longtitude": longtitude,
        "latitude": latitude,
        "zip_code": zip_code,
        "title": title,
        "date_and_time": date_and_time,
        "town": town,
        "address": address,
                            }

for key,value in dataset.items():
        print(key,value)

