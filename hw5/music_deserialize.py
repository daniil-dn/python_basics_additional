import json, pickle

result_pickle = {}
with open('group.pickle', 'rb') as f:
    pick = f.read()
    result_pickle = pickle.loads(pick)

print(result_pickle)
print(type(result_pickle))

result_json = {}

with open('group.json', 'r') as f:
   result_json = json.load(f)

print(result_json)
print(type(result_json))