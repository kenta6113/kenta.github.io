import re

strings = 'The ghost that says boo haunts the loo'
search = re.findall('.oo',strings,re.IGNORECASE)
print(strings)