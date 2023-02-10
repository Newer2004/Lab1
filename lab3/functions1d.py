def filter_prime(list):
    for x in list:
        ix = int(x)
        sum=0
        for y in range(2,ix):
            if(ix % y == 0):
              sum+=1
        if(sum==0 and int(x) > 1):
            print(x)    


input_int = input()
list  = input_int.split()
filter_prime(list)