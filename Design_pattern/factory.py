class Pet:
    def __init__(self, name=""):
        self._name = name
    
    def name(self, name=""):
        if len(name) == 0 :
            return self._name
        else:
            self._name = name
            return None
    
    def speak(self):
        return None

class Dog(Pet):
    def speak(self):
        return "Woof"

class Cat(Pet):
    def speak(self):
        return "Meow"


def get_pet(pet="dog"):
    pets = {"dog": Dog(), "cat": Cat()}
    return pets[pet]

if __name__ == "__main__":
    d = get_pet("dog")
    d.name("joe")
    print(d.name())
    print(d.speak())

    c = get_pet("cat")
    c.name("mimi")
    print(c.name())
    print(c.speak())
