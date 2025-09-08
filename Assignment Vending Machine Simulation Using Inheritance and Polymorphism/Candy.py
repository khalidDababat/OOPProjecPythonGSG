

from Product import Product

class Candy(Product):
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor

    def display_info(self):
        
        return super().display_info() + f"Candy Flavor: {self.flavor}"
