def add12():
    pass


class temp:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """setting x property for temp object"""
        return self._x
    
    @x.setter
    def x(self, value):
        if value > 10:
            self._x =  value

    @x.deleter
    def x(self):
        self._x = None

if __name__ == "__main__":
    test = temp()
    test.x = 40
    print("test.x = " + str(test.x))
    del test.x
    print("test.x is now " + str(test.x))