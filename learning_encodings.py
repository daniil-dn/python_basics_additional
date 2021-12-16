s = 'hello'
sb = b'hello'

# print(type(sb))

with open("bytes.txt", 'w', encoding='utf-16') as f:
    str = 'hello world'
    f.write(str)

with open("bytes.txt", 'rb') as f:
    s = f.read()

    print(s)

with open('bytes.txt', 'r', encoding='utf-16') as f:
    s = f.read()

    print(s)
