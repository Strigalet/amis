from data_for_911 import dataset
from validators.lib import  *


def importing(dataset,latitude,longtitude,zip_code,title,date,time,town,address,station):
    if station!="":
        station="Station "+station+"; "
    dataset[address+"; "+town+"; "+station+date+" @ "+time+";"] = {
        "longtitude": longtitude,
        "latitude": latitude,
        "zip_code": zip_code,
        "title": title,
        "date_and_time": date+" "+time,
        "town": town,
        "address": address,
    }

def addAccidentValidator():

    latitude=get_latitude()
    while not latitude:
        print("Print correct data:" )
        latitude = get_latitude()

    longtitude=get_longtitude()
    while not longtitude:
        print("Print correct data:" )
        longtitude = get_longtitude()

    zip_code=get_zip_code()
    while not zip_code:
        print("Print correct data:" )
        zip_code = get_zip_code()

    title = get_title()
    while not title:
        print("Print correct data:")
        title = get_title()

    date = get_date()
    while not date:
        print("Print correct data:")
        date = get_date()

    time = get_time()
    while not time:
        print("Print correct data:")
        time = get_time()

    town = get_town()
    while not town:
        print("Print correct data:")
        town = get_town()

    address = get_address()
    while not address:
        print("Print correct data:")
        address = get_address()

    station = get_station()
    while not station:
        print("Print correct data:")
        station = get_station()


    importing(dataset, latitude, longtitude,zip_code,title,date,time,town,address,station)

importing(dataset,20.12341234,130.67885678,54543,"Fire: HATA GORIT","2018-09-15","13:54:23","RIO","PEREULOK LOLOVICHEY","")
addAccidentValidator()
for key,value in dataset.items():
    print(key,value)
