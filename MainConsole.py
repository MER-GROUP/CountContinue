###############################################################################################################
# импортируем написанный молуль Conductor (структура программы)
from Conductor import Conductor
# импортируем молуль os - работа с файлами и директориями (папками)
# mkdir - создает директорию files в текущей директории
# getcwd - определение в какой папке мы находимся
from os import mkdir, getcwd
# импортируем молуль os.path - работа с файлами и директориями (папками)
# dirname - определяем текущую директорию
# join - объеденяем директорию + файл (правильный путь файла)
# exists - существует ли файл или директория
from os.path import dirname, join, exists
# импортируем молуль os - работа с файлами и директориями (папками)
# listdir - показывает файлы в конкретной папке
from os import listdir
###############################################################################################################
#если программа не модуль то выполнить условие
if __name__ == '__main__':
    # функция рисует линию
    def line():
        print('-----------------------------------------------------------------------------')

    # основная функция - логика программы
    def main():
        # вывод информации о программе
        print('-----------------------------------------------------------------------------')
        print('CountContinue v1.4 - программа для посчета одинаковых строк в текстовом файле')
        # определение директории нахождения
        print('-----------------------------Directory is------------------------------------')
        print(getcwd())
        # наименование директории где будут файлы для подсчета повторений
        DIRECTORY = './FilesForSearch'
        # проверка существует ли директория
        # если нет то создать 
        if not exists(DIRECTORY):
            mkdir(DIRECTORY)
        # показать файлы директории FilesForSearch
        lst = listdir(DIRECTORY)
        for i in lst:
            print(i)
        print('-----------------------------------------------------------------------------')
        # ввод имени файла который находится в директории FilesForSearch
        while True:
            try:
                # ввод имени файла который находится в директории FilesForSearch
                # для находждения одинаковых строк в текстовом файле
                FILENAME = input('Введите имя файла: ')
                FILE_DIR = DIRECTORY + '/' + FILENAME
                # определяем текущую директорию, гбе будет храниться файл
                CURRENT_DIR = dirname(__file__)
                # объединяем текущую директорию и директорию FilesForSearch и находящейся в ней файл
                FILE_PATH = join(CURRENT_DIR, FILE_DIR)
                # проверяем существует ли файл
                # если не существует то вызываем исключение
                # и заново вводим имя файла
                # если ыыели q, то выйти из программы
                if not exists(FILE_PATH):
                    raise FileNotFoundError
                else: break
            except FileNotFoundError:
                # если ввели q, то выходим из программы
                # иначе повторяемм ввод
                if FILE_PATH.lower().endswith('q'):
                    print('Вы вышли из программы')
                    # нарисовать линию
                    line()
                    exit()
        print('-----------------------------------------------------------------------------')
        # читаем файл
        conductor = Conductor()
        arr = conductor.file_read_utf8(FILE_PATH)
        # вывод файла в консоль
        # print(arr)
  
        # находим повторяющиеся строки
        my_dict = conductor.search(arr)

        # написать фильтр для вывода строк

        '''
        # выводим повторяющиеся строки в консоль
        for k, v in my_dict.items():
            print(k, ':', v)
        '''

        # выводим повторяющиеся строки в файл
        OUT_FILE = './FilesForSearch/result.txt'
        # conductor.file_write(OUT_FILE, list(my_dict))
        conductor.file_write_dict(OUT_FILE, my_dict)

        # конец программы
        # определяем текущую директорию и файл, гбе будет храниться информация
        # и выводим в консоль
        CURRENT_DIR = dirname(__file__)
        OUT_FILE = '/FilesForSearch/result.txt'
        FILE_PATH = CURRENT_DIR + OUT_FILE
        print(f'Результаты записаны в {FILE_PATH}')
        print('-----------------------------------------------------------------------------')

    main()
    ###############################################################################################################