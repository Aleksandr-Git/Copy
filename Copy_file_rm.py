# копирует файлы из одной папки в другую
# проверяет обе папки на наичие всех скопированных файлов
# если проверка прошлая, удаляет первую папку
# если нет, копирует недостающие файла и т.д.

import os
import shutil

path_origin = '.\\Copy'
path_copy = '.\\Arhiv'

print(os.listdir(path_origin))

def test_copy():
    for i in os.listdir(path_origin):
        if i in os.listdir(path_copy):
#            print(i)
            continue
        else:
            return False
    return True

def copy():
    for i in os.listdir(path_origin):
        if i in os.listdir(path_copy):
#            print('continue')
            continue
        try:
            shutil.copyfile(path_origin+'\\'+i, path_copy+'\\'+i)
        except PermissionError:
            continue

    if test_copy():
        shutil.rmtree(path_origin)
    else:
        copy()

copy()

