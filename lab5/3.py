import re

txt = "abbbbbb abb abbbb"

pattern = r'\w[a-z]+[_].+[a-z]'


print(re.search(pattern, txt))