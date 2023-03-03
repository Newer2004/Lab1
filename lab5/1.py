import re

txt = "abbbbbb abbb abbbb"

pattern = r'a*b'

print(re.search(pattern, txt))