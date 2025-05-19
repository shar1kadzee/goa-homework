class Person:
    def __init__(self, name):
        self.name = name

    def lower(self):
        return self.name.lower()

p1 = Person("barbare")
print(p1.lower()) 