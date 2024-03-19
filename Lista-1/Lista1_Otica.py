n=int(input())
while True:
    if n==0:
        break
    for i in range(0,n):
        lista=[]
        contador=0
        lista=[float(x) for x in input().split()]
        if lista[0]<=127:
            contador+=1
        if lista[1]<=127:
            contador+=1
        if lista[2]<=127:
            contador+=1
        if lista[3]<=127:
            contador+=1
        if lista[4]<=127:
            contador+=1
        if contador ==1:
            for z in range(0,5):
                if lista[z]<=127:
                    if z==0:
                        print("A")
                    elif z==1:
                        print("B")
                    elif z==2:
                        print("C")
                    elif z==3:
                        print("D")
                    elif z==4:
                        print("E")
        else:
            print("*")
    n=int(input())