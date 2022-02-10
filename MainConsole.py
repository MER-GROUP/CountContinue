from Conductor import Conductor
from os import mkdir
from os.path import exists

#если программа не модуль то выполнить условие
if __name__ == '__main__':
    def main():
        # наименование директории где будут файлы для подсчета повторений
        #DIRECTORY = 'FilesForSearch'
        DIRECTORY = 'CountContinue/FilesForSearch'
        # проверка существует ли директория
        # если нет то создать 
        if not exists(DIRECTORY):
            mkdir(DIRECTORY)

        print('-----------------------------------------------------------------------------')
        print('CountContinue v1.2 - программа для посчета одинаковых строк в текстовом файле')
        print('-----------------------------------------------------------------------------')
        FILE = input('Введите имя файла: ')
        FILE_DIR = DIRECTORY + '/' + FILE
        print('-----------------------------------------------------------------------------')

        # читаем файл
        conductor = Conductor()
        arr = conductor.file_read_utf8(FILE_DIR)
        # print(arr)
        
        # находим повторяющиеся строки
        my_dict = conductor.search(arr)

        # написать фильтр для вывода строк

        # выводим повторяющиеся строки в консоль
        for k, v in my_dict.items():
            print(k, ':', v)

    main()