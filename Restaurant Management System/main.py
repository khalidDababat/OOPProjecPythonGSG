

import __main__
from  MenuItem import MenuItem
from Restaurant import Restaurant


def main(): 
     restaurant = Restaurant()

     while True: 
          print("\nWelcome to the Restaurant Management System!")
          print("Choose an option:")
          print("1. Add menu item")
          print("2. View menu")
          print("3. Create new order")
          print("4. List all orders")
          print("5. Exit") 


          selection = input("Enter your choice: ").strip() 
          if selection == "1":
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                category = input("Enter item category: ")
                item = MenuItem(name, price, category)
                restaurant.menu.append(item)
                print(f"Added {item.get_name()} to the menu successfully.") # for notify  
         
          elif selection == "2":
                print(restaurant.view_menu()) 
          elif selection == "3":
               print(restaurant.view_menu())  
               if restaurant.menu: 
                     numbers = input("Enter item numbers for the order separated by commas (e.g., 1,2): ")  
                     item_numbers = [int(num.strip()) for num in numbers.split(",") if num.strip().isdigit()]   
                     restaurant.createOrder(item_numbers)
                     print("Order created successfully.") # for notify
          elif selection == "4":    
              print(restaurant.list_orders() )       
                   

          elif selection == "5":
            print("Thank you for using the Restaurant Management System!")
            break

          else:
            print("Invalid choice, please try again.")
      
                      






if __name__ == "__main__":
    main()

