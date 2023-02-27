N=int(input())
squares_generator = (i * i for i in range(N))

for i in squares_generator:
    print(i)
