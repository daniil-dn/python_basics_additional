my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

set_from_list_1 = set(my_list_1)
set_from_list_2 = set(my_list_2)

print(set_from_list_1 - set_from_list_2)

date = "02.11.2013"
days_month = {
    "days": ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое',
             'седьмое', 'восьмое', 'девятое', 'десятой', 'одиннадцатое',
             'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое'],
    "month": ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь'],
}
date = date.split('.')
print(days_month['days'][int(date[0]) - 1], days_month['month'][int(date[1]) - 1], date[2], "года")

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_1_sorted = []

for x in my_list_1:
    if my_list_1.count(x) == 1:
        my_list_1_sorted.append(x)
print(my_list_1_sorted)