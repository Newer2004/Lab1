import re
def f(mObject):
    return mObject.group("g1").casefold()+ " "

text="my_world"
pattern = "(?P<g1>[a-z])(?P<g2>[_])+"
print(re.sub(pattern, f, text))
