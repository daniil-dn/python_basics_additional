import json

# dump, dumps, load, loads

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': "Leo", "age": 33}
]

print(type(friends))

json_friends = json.dumps(friends)
# print(json_friends)
# print(type(json_friends))

friends = json.loads(json_friends)
# print(friends)
# print(type(friends))

with open('friends_json.json', 'w') as f:
    f.write(json_friends)
with open('friends_json.json', 'rb') as f:
    # print('its from a new file *json')
    print(f.read())


with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(friends, f)

print('dumped to file ')

