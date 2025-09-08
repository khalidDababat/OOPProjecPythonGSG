
from Product import Product
class Snack(Product):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

    def display_info(self):
        super().display_info()
        return f"Snack Calories: {self.calories} kcal"