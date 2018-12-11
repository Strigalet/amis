from data_for_911 import dataset


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


importing(dataset,"40.3123323","-75.1234432","19525","EMS: HEAD INJURY","2018-09-23","18:54:48","Kiev","Registry Office 'Pcholka'","334A")
importing(dataset,"44.8943423","-72.6662532","18999","Traffic: VEHICLE ACCIDENT -","2018-12-29","23:34:20","Kiev","Pyatyorochka na uglu","")
#for key,value in dataset.items():
 #   print(key,value)
