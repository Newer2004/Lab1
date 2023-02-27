def deleteSecond(st):
    for i in range(len(st)):
        if(i%2==1):
            continue
        else:
            print(st[i])
st=input()
deleteSecond(st)