import os
import json
import re
import shutil


file_list_installed = os.listdir('E:/steam-down/steamapps/workshop/content/431960')
# with open('E:/steam-down/steamapps/workshop/test.json') as f:
#     subcription = json.load(f)

# with open('test.json') as f:
#     compent = f.read()

# print(compent)

# reg = r'"[a-z0-9]+?/s{2}"(.*?)"'
# reg = r'"(.*?)"'
# result = re.findall(reg, compent)
# print(result)

file_list = os.listdir('H:/SteamLibrary/steamapps/workshop/content/431960')
copy_dir = 'H:/copydir'

index = 0
for file in file_list:
    if file not in file_list_installed:
        now_file = 'H:/SteamLibrary/steamapps/workshop/content/431960/' + file
        print(now_file)
        shutil.move(now_file, copy_dir)
        # shutil.copytree(now_file, copy_dir + '/' + file)
        index += 1

print('---------------')
index_1 = 0
for file in file_list_installed:
    if file not in file_list:
        print(file)
        index_1 += 1

print(len(file_list_installed))
print(len(file_list))
print(index)
print(index_1)

print('------------')

with open('E:/steam-down/steamapps/workshop/appworkshop_431960.acf') as f:
    compent = f.read()

reg = '"([0-9]*)"\n\t\t{'
result = re.findall(reg, compent)
print(len(result))
result = list(set(result))
print(len(result))

print('----------')

for file in result:
    if file not in file_list_installed:
        print(file)



# result_replace, number = re.subn(reg, '":"', compent)
# with open('c:/Users/heyefu/Desktop/test_1.json', 'w') as f:
#     f.write(result_replace)

with open('subcription.json', encoding='utf-8') as f:
    subcription = json.loads(f.read())

print(len(subcription))

inex = 0
for file in subcription:
    if file not in file_list_installed:
        print(file, subcription[file])
        index += 1

print(index)
