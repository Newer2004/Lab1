def square(a,b):
    for n in range(a,b):
        yield n ** 2
a=int(input())
b=int(input())
squares = square(a,b)
for square in squares:
    print(square)


