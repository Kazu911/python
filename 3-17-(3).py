import re

word = "The ghost that says boo haunts the loo."

m = re.findall(".oo", word, re.IGNORECASE)
print(m)
