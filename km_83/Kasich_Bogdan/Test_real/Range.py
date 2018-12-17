m=int(input("The start "))
n=int(input("The end "))
counter=0
for i in range(m,n+1):
    if i%2==1:
        counter+=1
print(counter)