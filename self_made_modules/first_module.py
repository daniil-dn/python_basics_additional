foo = 'foo A'

def bar():
    print('first module')

print('not main module')

print(__name__)
if __name__ == '__main__':
    print('you see it, so it is the main py program')