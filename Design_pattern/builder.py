# A simple car builder exercise using the builder pattern, including dirctor, abstract builder, concrete builder, and car
class Director():
    """
    The director class that orchestrates the build
    """
    def __init__(self, concrete_builder):
        self._builder = concrete_builder
    
    def construct_skylart(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tire()
        self._builder.add_engine()
    
    def get_skylart(self):
        return self._builder._car

class Builder():
    """
    Abastract builder
    """
    def __init__(self):
        self._car = None
    
    def create_new_car(self):
        self._car = Car()

class SkylartBuilder(Builder):
    """
    Concrete builder for Skylart car
    """    
    def add_model(self):
        self._car.model("Skylark")
    def add_tire(self):
        self._car.tire("Regular tires")
    def add_engine(self):
        self._car.engine("Turbo")


class Car():
    def __init__(self):
        self._model = None
        self._tires = None
        self._engine = None
    
    def tire(self, tire=None):
        """
        tire getter/setter
        """
        if tire is None:
            return self._tires
        else:
            self._tires = tire

    def model(self, data=None):
        """
        model getter/setter
        """
        if data is None:
            return self._model
        else:
            self._model = data    

    def engine(self, data=None):
        """
        engine getter/setter
        """
        if data is None:
            return self._engine
        else:
            self._engine = data
    
    def __str__(self):
        return 'Model: {0} | Tire: {1} | Engine: {2}'.format(self.model(), self.tire(), self.engine())

if __name__ == "__main__":
    builder = SkylartBuilder()
    director = Director(builder)
    director.construct_skylart()
    print(str(director.get_skylart()))
