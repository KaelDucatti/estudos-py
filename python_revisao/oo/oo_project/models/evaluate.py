class Evaluate:
    def __init__(self, username, evaluation):
        self.__username = username
        self.__evaluation = evaluation

    @property
    def username(self):
        return self.__username
    
    @property
    def evaluation(self):
        return self.__evaluation

    @username.setter
    def username(self, name):
        self.__username = name
    
    @evaluation.setter
    def evaluation(self, value):
        self.__evaluation = value
        