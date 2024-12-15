class Pen:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

pen = Pen("blue")

pen.color