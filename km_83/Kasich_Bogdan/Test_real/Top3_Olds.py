Ages = {
        "Bob":19,
        "Boba":20,
        "Boban":18,
        "Tolyan":87,
        "Jora": 47
}

keys=[]
values=[]
for name in Ages:
        keys.append(name)
        values.append(Ages[name])
copylka=values.copy()
values.sort()
values.reverse()
for age in values[:3]:
        print(keys[copylka.index(age)],age)