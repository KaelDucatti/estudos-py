class Foo:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

    @property
    def publico(self):
        return self.publico
    
    @publico.setter
    def publico(self, valor):
        self.publico = valor

    @property
    def protegido(self):
        return self._protegido

    @protegido.setter
    def protegido(self, valor):
        self._protegido = valor

    @property
    def privado(self):
        return self.__privado

    @privado.setter
    def privado(self, valor):
        self.__privado = valor


        