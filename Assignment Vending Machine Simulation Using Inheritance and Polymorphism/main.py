 
from Snack import Snack
from Candy import Candy
from Drink import Drink

def fill_products(filename):
       products =[]      
       with open(filename,'r') as file: 
            for line in file: 
                 parts =line.strip().split(',')
                 if(len(parts) == 4 ):
                        product_type, name, price, extra = parts
                        if product_type == 'Drink':
                            products.append(Drink(name, price, extra))
                        elif product_type == 'Snack':
                            products.append(Snack(name, price, extra))
                        elif product_type == 'Candy':
                            products.append(Candy(name, price, extra))
       return products

class Main:

    def run(self):
          products = fill_products('products.txt')

          print("Welcome to the Python Vending Machine!")
          print("Please select what you want:") 
        #   print("1. Drink - Cola")
        #   print("2. Snack - Chips")
        #   print("3. Candy - Gummy Bears")
        #   print("4. Drink - Water")
        #   print("5. Snack - Cookies")   for make Dynamic 
          for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.__class__.__name__} - {product.name}")
          
          selection = int(input("Enter the number of your choice: "))
          if 1 <= selection  <=  len(products):
                  print("Product Information:")
                  print(products[selection -1].display_info())   

          else:
                  print("Invalid Selection. Please try again.")       


if __name__ == "__main__":
    main = Main()
    main.run()

