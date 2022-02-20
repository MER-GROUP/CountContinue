###############################################################################################################
# модуль для легкого копирования файлов и папок
import shutil
# модуль для работы с вводом и выводом в консоль
import sys
# импортируем молуль os.path
# dirname - определяем текущую директорию
# join - объеденяем директорию + файл (правильный путь файла)
from os.path import dirname, join
###############################################################################################################
# класс для работы с файлом
class File:
    # конструктор
    def __init__(self) -> None:
        pass

    # чтение файла
    def file_read(self, file: str) -> list[str]:
        with open(file, 'r') as f:
            return f.readlines()

    # чтение в список содержимого файла содержащий текст в utf-8 кодировке
    def file_read_utf8(self, file: str) -> list[str]:
        str_byte = None
        with open(file, 'r', encoding='utf-8') as f:
            #shutil.copyfileobj(f, arr.extend)
            str_byte = f.read().encode('utf-8')
        #print(repr(str(arr, 'utf-8')))
        #print(str(arr, 'utf-8'))
        return str(str_byte, 'utf-8').split('\n')

    # запись информации (списка - list) в файл
    def file_write(self, out: str, arr: list) -> None:
        for i in range(len(arr)):
            arr[i] += '\n'
        with open(out, 'w') as f:
            f.writelines(arr)

    # запись информации (словаря - dict) в файл
    def file_write_dict(self, out: str, dictor: dict) -> None:
        with open(out, 'w') as f:
            for k,v in dictor.items():
                f.write(f'{k} {v}\n')

    # вывод в консоль содержимого файла (обычный текстовый файл)
    def file_output_console(self, arr: list) -> None:
        for line in arr:
            #print(line.strip())
            #print(repr(line))
            print(line, end='')

    # вывод в консоль содержимого файла содержащий текст в utf-8 кодировке (аналог type filename в cmd.exe)
    def file_output_console_utf8(self, file: str) -> None:
        with open(file, 'r', encoding='utf-8') as f:
            shutil.copyfileobj(f, sys.stdout)
###############################################################################################################
# проверка класса и методов
# если программа не модуль то выполнить условие
if __name__ == '__main__':
    def main():
        # определяем текущую директорию, гбе будет храниться файл
        CURRENT_DIR = dirname(__file__)
        # задаем имя файла для чтения данных
        FILENAME = './FilesForSearch/test_read.txt'
        # объединяем текущую директорию и находящейся в ней файл
        FILE_PATH = join(CURRENT_DIR, FILENAME)
        # задаем имя файла для вывода результатов
        OUT_FILE = 'FilesForSearch/test_write.txt'
        f = File()
        #arr = f.file_read(FILE_PATH)
        #f.file_output_console(FILE_PATH)
        #f.file_output_console_utf8(FILE_PATH)
        ############################
        # считываем файл с данными
        arr = f.file_read_utf8(FILE_PATH)
        #f.file_output_console(arr)
        ############################
        # вывести первую строку в консоль
        print(arr[0])
        # подсчет количества строк
        print(len(arr))
        ############################
        # записываем результат в файл
        f.file_write(OUT_FILE, arr)

    main()
###############################################################################################################