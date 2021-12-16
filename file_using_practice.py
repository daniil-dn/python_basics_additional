f_1 = open('first.txt', 'w')

# f_1.write("Write hello world \n")
# f_1.write("Write hello world")

f_1.writelines(['hello\n', 'Python'])

f_1 = open('first.txt', 'r')
# print(type(f_1))
#
print(f_1.read())
print(f_1.readlines())
for line in f_1:
    # pass
    print(line.replace('\n', ' '))
    # line = 'adf'
#

with open('first.txt', 'r') as file:
    for line in file:
        # pass
        print(line.replace('\n', ' '))
f_1.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line)

