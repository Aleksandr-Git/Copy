import os
import time

'''
path = './pap_3'
a = os.path.getatime(path)  # время последнего доступа
b = os.path.getmtime(path)  # время последнего изменения
c = os.path.getctime(path)  # время создания (Windows), время последнего изменения (Unix)
print([time.ctime(x) for x in [a, b, c]])
'''

path = '.\pap_3' # Путь к вашей папке
  
# Получим список имен всего содержимого папки
# и превратим их в абсолютные пути
dir_list = [os.path.join(path, x) for x in os.listdir(path)]
  
if dir_list:
    # Создадим список из путей к файлам и дат их создания.
    date_list = [[x, os.path.getctime(x)] for x in dir_list]
  
    # Отсортируем список по дате создания в прямом порядке
    sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=False)
  
    # Выведем первый элемент списка. Он и будет самым первым по дате
    print(sort_date_list[0][0])
    print(sort_date_list)
