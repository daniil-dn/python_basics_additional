import os
import shutil


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


def delete_file(name):
    os.rmdir(name) if os.path.isdir(name) \
        else os.remove('text.dat')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("The directory exists.")
    else:
        shutil.copy(name, new_name)


if __name__ == '__main__':
    create_file('text.dat')
    create_folder('new_f')
    get_list(folders_only=True)
    # copy_file('new_f', './new/new')
    copy_file('text.dat', './new/tex2t.dat')

