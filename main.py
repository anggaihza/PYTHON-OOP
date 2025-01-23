from car import Car


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = False

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")


# print(car1.model)
# print(car1.color)
# car1.drive()
# car1.stop()
# car1.describe()

print(dog.name)
print(dog.is_alive)
print(cat.name)
cat.eat()

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")