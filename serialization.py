import pickle

ob = {'name': 'Max', 'phones': ["1234", '8203']}

with open('person.dat', 'wb') as f:
    pickle.dump(ob, f)

with open('person.dat', 'rb') as f:
    s = f.readline()
    print(s, pickle.loads(s), sep='\n')



