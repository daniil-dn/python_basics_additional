def get_sep(sep_sign, sep_len):
    # print(sep_sign * sep_len)
    return sep_sign * sep_len


def hello(who):
    print("hello", who)


hello('max')


def greeting(who="Nobody", say= "hello"):
    print(say, who)


greeting(say='who are you?', who="leo")
