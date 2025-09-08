
from Product import Product

class Drink(Product): 
    def __init__(self, name, price, volume):
        super().__init__(name, price)  
        self.volume = volume

    def display_info(self):
           
          super().display_info()
          return  f"Drink Volume: {self.volume}ml"
           
    