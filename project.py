class Dog:
    
    animal = 'dog'

    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    
    def display_details(self):
        print(f'Animal: {Dog.animal}')
        print(f'Breed: {self.breed}')
        print(f'Color: {self.color}')


dog1 = Dog('Labrador', 'Black')
dog2 = Dog('Beagle', 'Brown')

print('Details of Dog 1:')
dog1.display_details()
print('\nDetails of Dog 2:')
dog2.display_details()
