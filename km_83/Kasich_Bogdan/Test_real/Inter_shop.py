with open("data/text.txt") as file:
    keys=[]
    values=[]
    info=file.readline()
    while info:
        info=info.rstrip().split(", ")
        keys.append(info[0])
        del info[0]
        values.append(set(info))
        info=file.readline()
    row_dict=dict(zip(keys,values))
    for key,value in row_dict.items():
        print(key,value)