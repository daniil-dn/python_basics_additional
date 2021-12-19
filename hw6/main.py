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

def sqrt_lists_nums(ls=None):
    if ls is None:
        pass
    result = [n**2 if n>0 else n for n in ls]
    return result


print(sqrt_lists_nums(nums))
