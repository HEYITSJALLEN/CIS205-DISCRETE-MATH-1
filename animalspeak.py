class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

#Both Dog and Cat can be passed to make_animal_speak()

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Outputs: Woof!
make_animal_speak(cat)  # Outputs: Meow!