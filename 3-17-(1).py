import re

with open("zen.txt", "r", encoding="cp932") as f:
    zen = f.read()
    print(zen)

m = re.findall("Dutch", zen, re.MULTILINE)
print(m)
