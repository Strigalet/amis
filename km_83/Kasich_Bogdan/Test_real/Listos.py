def go(list,counter=0):
    if len(list) <= counter*3:
        return
    print(list[counter*3])
    counter+=1
    return go(list,counter)



listos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print(go(listos))