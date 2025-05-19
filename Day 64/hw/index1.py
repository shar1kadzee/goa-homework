class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        return self.grade > 5
    
student1 = Student("barbare", 15, 9)
print(student1.name, "is he passing?", student1.is_passing())
