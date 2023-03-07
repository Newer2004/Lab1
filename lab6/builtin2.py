def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for c in s:
        if c.isupper():
           d["upper_case"]+=1
        elif c.islower():
           d["lower_case"]+=1
        else:
           pass
    print ("Number of Upper case characters : ", d["upper_case"])
    print ("Number of Lower case Characters : ", d["lower_case"])

string_test(input())