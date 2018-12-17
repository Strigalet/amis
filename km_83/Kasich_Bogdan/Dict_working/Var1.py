from Funcs import maxAge, addMark, getNames_pupils
smth = [
    {
        "name": "Bob",
        "age": 20,
        "marks": {
            "Math": 98,
            "Python": 100
        }
    },
    {
        "name": "Boba",
        "age": 19,
        "marks": {
            "Physic": 98

        }
    },
    {
        "name": "Boban",
        "age": 22,
        "marks": {
        }
    }
]


print(maxAge(smth))
print("====================================")
print(getNames_pupils(smth))
b=addMark(smth,"Boba","History",99)
a=addMark(smth,"Boban","Memology",8000)
for i in smth:
    for a in i:
        print(a,i[a])
