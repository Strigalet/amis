from data_for_911 import dataset
from adding import importing
from validators.lib import  *

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

addAccidentValidator()
for key,value in dataset.items():
    print(key,value)
