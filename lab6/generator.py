import string

def generator1():
    for h in string.ascii_uppercase:
      yield h
def generator():
    for h in string.ascii_lowercase:
      yield h

g=generator()
g1=generator1()
for i in g:
  print(i)
for u in g1:
   print(u)
