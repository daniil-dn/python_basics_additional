import random

print(random.randint(0,100))

players = ['max', "kate", 'tom', 'ron', "bill"]
print(random.choice(players))

print(random.sample(players, 3))

random.shuffle(players)
print(players)

cards = list('qwertyuio')
print(cards)

random.shuffle(cards)
print(cards)