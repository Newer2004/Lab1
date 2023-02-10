def solve(numheads, numlegs):
    R=int((numlegs-(numheads*2))/2)
    C=int((numheads-R))
    print("Rabbits:", R)
    print("Chickens:", C)
heads=35
legs=94
solve(heads, legs)