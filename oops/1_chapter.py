
#basic class Example
class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model =model

my_car = Car('Toyota','corola')
print(my_car.brand)
print(my_car.model)

my_new_car = Car('Tata','safari')
print(my_new_car.brand)
print(my_new_car.model)
