from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} заведена.")
      
    @abstractmethod
    def refuel(self):
        pass

class BenzinCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def refuel(self):
        print(f"{self.make} {self.model} заправлена бензином.")
     
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = "75 kWh"
    
    def refuel(self):
        print(f"{self.make} {self.model} заряжена.")
        
    def get_battery_size(self):
        return self.battery_size
    
    def set_battery_size(self, size):
        self.battery_size = size
        print(f"Размер батареи {self.make} {self.model} установлен на {size}.")
        
    def __str__(self):
        return f"Это электро-кар {self.make} {self.model} {self.year} года"

# mercedes = Car("Mercedes", "Benz", 2023) 
audiRs6 = BenzinCar("Audi", "RS6", 2023)
tesla = ElectricCar("Tesla", "Model S", 2023)


audiRs6.start()
audiRs6.refuel()
tesla.start()
tesla.refuel()

print(tesla.get_battery_size())

tesla.battery_size = "60 kWh"

print(tesla.get_battery_size())
print(tesla)

