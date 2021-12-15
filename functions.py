def get_sep(sep_sign, *sep_len):
    # print(sep_sign * sep_len)
    return sep_sign * sep_len


def hello(who):
    print("hello", who)


hello('max')


def greeting(who="Nobody", say="hello"):
    print(say, who)


greeting(say='who are you?', who="leo")


def filter(nums, func):
    result = []
    for num in nums:
        if func(num):
            result.append(num)
    return result


numbers = [1, 2, 34, 5, 3, 2, 6]

print(filter(numbers, lambda x: x % 2 == 0))
list(map(lambda x: x**2, numbers))
