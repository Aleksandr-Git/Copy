import os
import shutil
import time

path = './pap'
path_work = ''
path_origin = ''
path_copy = ''

size = os.path.getsize(path)
#files = os.listdir(path)
total_size = 0

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

def fun_copy(path):  # копирует файлы из папки, но не копирует папки

    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            fun(path + '/' + i)

        else:
            shutil.copy(path + '/' + i,
                        './copy_pap')

#fun_copy(path)

cur_dir = os.getcwd()
print(cur_dir)

print(os.listdir('./pap_2'))

def copy_folder():
    shutil.move('./pap_2' + '/' + os.listdir('./pap_2')[0], './pap_3')  # перемещает файлы из первой папки во вторую и удаляет первую
    #os.rename('./pap_3/0', './pap_3/' + str(int(os.listdir('./pap_3')[-1]) + 1))
    os.rename('./pap_3/0', './pap_3/' + str(int(len(os.listdir('./pap_3')))))
    for i in os.listdir('./pap_2'):
        os.rename('./pap_2' + '/' + i, './pap_2' + '/' + str(int(i) - 1))

while True:
    total_size = 0

    if fun('./pap_2') > 7:
        time.sleep(5)
        try:
            copy_folder()

        except Exception:
            continue
        print(str(total_size / 1024 / 1024) + ' Мб')
        print(os.listdir('./pap_2'))
