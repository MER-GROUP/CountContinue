###############################################################################################################
# модуль для легкого копирования файлов и папок
import shutil
# модуль для работы с вводом и выводом в консоль
import sys
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

    # запись информации в файл
    def file_write(self, out: str, arr: list) -> None:
        for i in range(len(arr)):
            arr[i] += '\n'
        with open(out, 'w') as f:
            f.writelines(arr)

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

# проверка класса и методов
# если программа не модуль то выполнить условие
if __name__ == '__main__':
    def main():
        FILE = 'CountContinue/test.py'
        #FILE = 'CountContinue/test.txt'
        OUT = 'CountContinue/out.txt'
        f = File()
        #arr = f.file_read(FILE)
        #f.file_output_console(arr)
        #f.file_output_console_utf8(FILE)
        ############################
        arr = f.file_read_utf8(FILE)
        #f.file_output_console(arr)
        ############################
        print(arr[0])
        print(len(arr))
        ############################
        f.file_write(OUT, arr)

    main()