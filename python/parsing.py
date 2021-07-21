import json

'''
items = {
    "coke": 1.0, 
    "fanta": 3.0, 
    "sprite": 4.0, 
    }


items["Yoghurt"] = 3.0

items_json = json.dumps(items)

print(items)
print(items_json)

with open("try.txt", 'w') as f:
    json.dump(items, f)

'''

with open('try.txt', 'r') as f:
    data = json.load(f)


data["Fan Ice"] = 3.0

print(data)

with open("try.txt", "w") as f:
    json.dump(data, f)