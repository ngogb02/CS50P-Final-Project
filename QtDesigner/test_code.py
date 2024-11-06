import json

with open ('inventory.json', 'r') as file:
    dict = json.load(file)

print(len(dict))
print(dict)
