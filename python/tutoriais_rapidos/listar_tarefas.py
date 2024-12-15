"""
Exercício - lista de tarefas com desfazer e refazer
"""
class ToDo:
    def __init__(self, list_name: str) -> None:
        self.__list_name = list_name
        self.__to_do_list = []
        self.__to_do_list_bkp = []
    
    @property
    def list_name(self):
        return self.__list_name

    @list_name.setter
    def list_name(self, name):
        self.__list_name = name
    
    def add_task(self, task):
        if task == "to list":
            self.to_list()
        elif task == "to undo":
            self.to_undo()
        elif task == "to ramake":
            self.to_remake()
        else:
            self.__to_do_list.append(task)

    def to_list(self):
        for item in self.__to_do_list:
            print(item)

    def to_undo(self):
        if self.__to_do_list:
            task = self.__to_do_list.pop()
            self.__to_do_list_bkp.append(task)

    def to_remake(self):
        if self.__to_do_list_bkp:
            task = self.__to_do_list_bkp[-1]
            self.__to_do_list.append(task)


def main():
    list_name = input("Name your to do list: ")
    my_list = ToDo(list_name)

    print("Available actions: list, undo and remake")
    action = input("Choose one: ")
    
    my_list.add_task(action)


if __name__ == "__main__":
    main()