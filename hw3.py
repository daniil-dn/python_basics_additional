# 1: Создайте функцию, принимающую на вход имя,
# возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
def name_age_town(name, age, town):
    print("{}, {} год(а), проживает в городе {}".format(name, age, town))


# 2: Создайте функцию, принимающую на вход числа и возвращающую наибольшее из них
def biggest_among_nums(*args):
    print(sorted(args, reverse=True)[0])


def damage_armor_calculation(damage, armor_ratio):
    return damage / armor_ratio


def attack(attacker, survivor, armor=1.0):
    damage = damage_armor_calculation(attacker["damage"], armor)

    survivor["health"] -= damage


player = {
    "name": "Max",
    "health": 100,
    "damage": 50,
    'armor': 1.2,
}
enemy = {
    "name": "the enemy - your terrible dreammmm))) ",
    "health": 100,
    "damage": 50
}
print(player)
print(enemy)
print("before an attack")
attack(enemy, player, player["armor"])
print(player)
print(enemy)
