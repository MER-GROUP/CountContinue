# класс для поиска повторных строк
class SearchCountContinue:
    # конструктор
    def __init__(self) -> None:
        self.__res__ = dict()

    # поиск повторяющихся строк
    def search(self, arr: list) -> dict[str, list[int]]:
        for i in range(len(arr)):
            if 1 < arr.count(arr[i]):
                try:
                    if self.__res__[arr[i]] is None:
                        raise KeyError
                    else:
                        self.__res__[arr[i]] += [i + 1]
                except KeyError:
                    self.__res__[arr[i]] = [i + 1]
        return self.__res__

# проверка класса и методов
# если программа не модуль то выполнить условие
if __name__ == '__main__':
    def main():
        arr = ['11111',
                '22222',
                '33333',
                '11111',
                '44444',
                '55555',
                '77777',
                '22222',
                '66666',
                '77777',
                '11111',
                '88888',
                '22222']
        search = SearchCountContinue()
        res = search.search(arr)
        print(res)

    main()