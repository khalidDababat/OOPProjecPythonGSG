from  Order import Order 

class Restaurant:
    def __init__(self):
        self.menu =[]
        self.orders = [] 



    def add_order(self,order):
        self.orders.append(order)

    def createOrder(self,item_numbers):
          orderCustomer = Order() 
          for num in item_numbers:
            if 1 <= num <= len(self.menu):
                orderCustomer.add_item(self.menu[num - 1])
          self.orders.append(orderCustomer)

             

         
    def list_orders(self):
        if not self.orders:
            return "No orders yet."
        output = []
        for idx, order in enumerate(self.orders, 1):
            output.append(f"Order {idx}:\n{order}")
        return "\n\n".join(output)


    def view_menu(self):
        if not self.menu:
            return "Menu is empty."
        return "\n".join(f"{item.get_name()} - ${item.get_price()} ({item.get_category()})" for item in self.menu)