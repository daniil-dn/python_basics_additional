import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('The folder with such name already exists.')


def get_list(folders_only=False):
    res = os.listdir()
    if folders_only:
        res = [f for f in res if os.path.isdir(f)]
    print(res)


if __name__ == '__main__':
    create_file('text.dat')
    create_folder('new_f')
    get_list(folders_only=True)
