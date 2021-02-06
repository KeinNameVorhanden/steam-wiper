import os
import shutil
import winreg
import json
import time

def list_contains(l, n): 
    check = False
    for m in l:
        if m == n:
            check = True
            return check  
    return check 

with open(".\\settings.json", "r+") as file:
    data = json.load(file)
    settings = data['settings']
    steam_user = settings['excludelist']
    steam_data = settings['steam_userdata_path']

path = os.path.normpath('HKCU/Software/Valve/Steam/Users/c').replace('c', '')
data_list = []

for item in os.listdir(steam_data):
    time.sleep(0.2)
    if list_contains(steam_user, item) == True:
        print(f"excluded: {item}")
    else:
        data_list.append(item)
        
print(f"{data_list}")

for data in data_list:
    time.sleep(0.2)
    shutil.rmtree(f'{steam_data}\\{data}')
    print(f'{path}{data}')
    os.system(f'reg delete {path}{data} /f')

time.sleep(5)