#import numpy
def multiply(nums):
    total=1
    for x in nums:
        total *= x
    return total
orig=input()
nums=list(map(int, orig.split(" ")))
print(multiply(nums))
#mult=numpy.prod(nums)
#print(mult)
