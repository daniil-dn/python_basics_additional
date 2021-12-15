import sys
import os
import math

print(sys.executable)
if (input("to exit press 1") == '1'):
    sys.exit()

print(sys.platform)
print(sys.path)
print(sys.argv)


print(type(sys.path))
sys.path.append('/Users/daniildosin')

print(sys.path)

# import test_sys
#

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{} {}'.format(i, name))
    # os.rmdir(new_path)
