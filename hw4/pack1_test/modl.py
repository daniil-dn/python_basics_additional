import sys, os, random


def mk_several_dirs(count):
    current_path = os.getcwd()
    print(current_path)
    for i in range(count):
        new_path = os.path.join(current_path, f'created_{i}_dir')
        try:
            os.mkdir(new_path)
        except:
            pass


def rm_several_dirs(count):
    current_path = os.getcwd()
    print(current_path)
    for i in range(count):
        new_path = os.path.join(current_path, f'created_{i}_dir')
        try:
            os.rmdir(new_path)
        except:
            pass


def rand_list_item(list_):
    if list_:
        return random.choice(list_)
