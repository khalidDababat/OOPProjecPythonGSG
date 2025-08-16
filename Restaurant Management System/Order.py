

class Order:  

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def get_total(self):  
        return sum(item.get_price() for item in self.__items)  

    
    def __str__(self):
        if not self.__items:
            return "Order is empty."
        order_details = "\n".join(f"- {item}" for item in self.__items)  # هنا نستدعي __str__ تبع MenuItem
        return f"{order_details}\nPrice: ${self.get_total()}"
    
    