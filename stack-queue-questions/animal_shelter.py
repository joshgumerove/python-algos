class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def __str__(self):
        return str([self.cats, self.dogs])

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        adopted_cat = self.cats.pop(0)
        return adopted_cat

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        adopted_dog = self.dogs.pop(0)
        return adopted_dog

    def dequeue_any(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
            return result
        result = self.cats.pop(0)
        return result


custom_queue = AnimalShelter()
custom_queue.enqueue("Cat1", "Cat")
custom_queue.enqueue("Dog1", "Dog")
custom_queue.enqueue("Cat2", "Cat")
custom_queue.enqueue('Dog2', "Dog")

print(custom_queue)
print(custom_queue.dequeue_dog())
print(custom_queue.dequeue_cat())
print(custom_queue)
print(custom_queue.dequeue_any())
print(custom_queue)
