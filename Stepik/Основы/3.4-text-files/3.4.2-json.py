import json


def add_all_kids(name):
    result = kids[name]
    if len(kids[name]) != 0:
        for kid in kids[name]:
            result += kids[kid]
    return result


json_data = '[{"name": "ABAB", "parents": []}, {"name": "B", "parents": ["ABAB", "C"]}, {"name": "C", "parents": ["ABAB"]}]'
data = json.loads(json_data)
classes = {}
kids = {}

for item in data:
    name = item['name']
    parents = item['parents']
    if name not in kids:
        kids[name] = []
    for parent in parents:
        if parent not in kids:
            kids[parent] = []
        kids[parent] += [item['name']]

for key in sorted(kids):
    print(f'{key} : {kids[key]}')

for key in sorted(kids):
    kids[key] = add_all_kids(key)


for key in sorted(kids):
    kids[key] = set(kids[key])
    print(f'{key} : {len(kids[key]) + 1}')
