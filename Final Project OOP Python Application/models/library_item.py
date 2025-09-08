

from abc import ABC, abstractmethod 

class LibraryItem(ABC): #abstract Class 
     def __init__(self, item_id, title, author,available=True ):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.available = available


     @abstractmethod   # abstract method 
     def  display_info(self):
         pass   
     
     def check_availability(self):
        return self.available