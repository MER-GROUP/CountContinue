from SearchCountContinue import SearchCountContinue
from File import File

# класс делает множественное наследование от классов SearchCountContinue и File
# собирает в себе все методы классов для простой работы в MainConsole
class Conductor(SearchCountContinue, File):
    # конструктор
    def __init__(self) -> None:
        # вызов явно конструктора класса SearchCountContinue
        SearchCountContinue.__init__(self)
        # так работать не будет (если вызывать не явно)
        # super(SearchCountContinue, self).__init__()