import random

# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['strawberry', 'raspberry', 'banana']
fruits_2 = ['banana', 'watermelon', 'strawberry']

sim_fruits = [f for f in fruits_1 if f in fruits_2]
#
# print(sim_fruits)


# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям
#
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.

nums = [random.randrange(-100, 100) for n in range(10)]
print(nums)

filtered_nums_list = [n for n in nums if n > 0 and n % 3 == 0 and n % 4 != 0]


# print(filtered_nums_list)

# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное)
# и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться

def sqrt_lists_nums(ls=None):
    if ls is None:
        pass
    result = [n ** 2 if n > 0 else n for n in ls]
    return result


# print(sqrt_lists_nums(nums))
# print(nums)

def sqrt_but_not_for_13(num):
    if num == 13:
        raise Exception("num is 13 - i can't  square this number")
    else:
        return num ** 2

try:
    print(sqrt_but_not_for_13(13))
except Exception:
    pass
