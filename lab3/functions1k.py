def histogram(nums):
    for n in nums:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
orig=input()
nums=list(map(int, orig.split(" ")))
histogram(nums)