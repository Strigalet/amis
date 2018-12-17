#Variant1
def maxAge(smth,sup=0):
    global age
    if len(smth) == 0:
        return sup
    if smth[0]["age"] >= sup:
        sup = smth[0]["age"]
    return maxAge(smth[1:], sup)




def addMark(smth, name, disc, mark):
    for i in smth:
        if i["name"] == name:
            i["marks"][disc] = mark



def getNames_pupils(smth):
    count=1
    for i in smth:
        print(count,"name:",i["name"])
        count+=1
    return "===================================="


#Variant2
def getBrand(smth,sup=0):
    global brand
    if len(smth)==0:
        return brand
    if  len(smth[0]["owners"]) >= sup:
        sup=len(smth[0]["owners"])
        brand=smth[0]["brand"]
    return getBrand(smth[1:],sup)


def addOwner(smth,brand,name):
    for i in smth:
        if i["brand"]==brand:
            i["owners"].add(name)

def getNames_cars(smth):
    j=0
    for i in smth:
        print(i["brand"] + " owners:")
        for j in i["owners"]:
            print(j)
    return "===================================="