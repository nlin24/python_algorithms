# A singleton example of shared dictionary data store using Borg pattern

class Borg():
    _store = dict()
    def __init__(self):
        self.__dict__ = self._store

class Singleton(Borg):
    def __init__(self):
        Borg.__init__(self)

    def addItem(self, **kwargs):
        self._store.update(kwargs)
    
    def __str__(self):
        return str(self._store)

if __name__ == "__main__":
    x = Singleton()
    x.addItem(a= "b")
    x.addItem(c="d")
    print(x)
    y = Singleton()
    y.addItem(e="f")
    print(y) # both y and x objects share the same _store dictionary queue from the parent class 