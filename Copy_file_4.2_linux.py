# работает, но копирует все в оодну папку ня яндексдиске
# копирует на яндекс диск, перед запуском проверить примонтирован ли диск
# копированме пересено в отдельный поток


import os
import shutil
import time
from threading import Thread

path_origin = './pap_2'
path_copy = '/mnt/yandex_disk/pap_3'
status_copy = False

size = os.path.getsize(path_origin)
#files = os.listdir(path)
total_size = 0

os.system('sudo mount -a')

def fun(path):   # определяет размер папки
    global total_size
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):

            fun(path + '/' + i)

        else:
            s = os.path.getsize(path + '/' + i)
            total_size += s
    return total_size / 1024 / 1024

#fun(path)
print(str(total_size) + ' Мб')

#fun_copy(path)

cur_dir = os.getcwd()
print(cur_dir)

print(os.listdir(path_origin))


def last_pap():
    dir_list = [os.path.join(path_origin, x) for x in os.listdir(path_origin)]
    print(dir_list)
    if dir_list:
    # Создадим список из путей к файлам и дат их создания.
        date_list = [[x, os.path.getctime(x)] for x in dir_list]
  
    # Отсортируем список по дате создания в прямом порядке
        sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=False)

        return sort_date_list[0][0]
  
'''
def copy_folder():
    global status_copy
#    shutil.move(last_pap(), './pap_3')
    shutil.move(last_pap(), path_copy)
    status_copy = False
'''
print(fun(path_origin))
print(last_pap())

def test_copy():
    for i in os.listdir(last_pap()):
        if i in os.listdir(path_copy):
#            print(i)
            continue
        else:
            return False
    return True

def copy():
    for i in os.listdir(last_pap()):
        if i in os.listdir(path_copy):
#            print('continue')
            continue
        try:
            shutil.copyfile(last_pap()+'/'+i, path_copy+'/'+i)
        except PermissionError:
            continue

    if test_copy():
        shutil.rmtree(last_pap())
    else:
        copy()

while True:
    total_size = 0


#    if fun(path_origin) > 20 and status_copy == False:
    if fun(path_origin) > 20:
        status_copy = True
#        time.sleep(5)
#        try:
        Thread(target = copy())
#        copy_folder()

#        except Exception:
#            continue
        print(str(total_size / 1024 / 1024) + ' Мб')
        print(os.listdir(path_origin))


