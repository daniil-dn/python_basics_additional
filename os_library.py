import os

print(os.name)
# os.chdir()
print(os.getcwd())
# os.mkdir()
# os.path
# etc...

new_path = os.path.join(os.getcwd(), 'new_test_file_os_path')
print(new_path)
try: os.mkdir(new_path)
except:pass