


class MenuItem: 
   
   def __init__(self,name,price,category):
       self.__name = name
       self.__price = price
       self.__category = category
 
   def get_name(self):
        return self.__name

   def get_price(self):
        return self.__price

   def get_category(self): 
        return self.__category        
   
   def set_name(self, name):
        self.__name = name
   
   def set_price(self, price):
        self.__price = price

   def set_category(self, category):
       self.__category = category

   def __str__(self):
        return f"{self.__name} (${self.__price}) [{self.__category}]"