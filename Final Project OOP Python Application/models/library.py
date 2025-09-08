 

# import 
import json
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User

from models.Reservable import Reservable 

from exceptions.item_not_available import ItemNotAvailableError
from exceptions.user_not_found import UserNotFoundError
from exceptions.item_not_found import ItemNotFoundError

class Library:
     def __init__(self, items_file="items.json", users_file="users.json"):
        self.items_file = items_file
        self.users_file = users_file
        self.items = self.load_items()
        self.users = self.load_users()


     def load_items(self):
        try:
            with open(self.items_file, "r") as f:
                data = json.load(f)
                items = []
                for item in data:
                    item_type = item.get("type")
                    if item_type == "Book":
                        item.pop("type", None)
                        items.append(Book(**item))
                    elif item_type == "Magazine":
                        item.pop("type", None)
                        items.append(Magazine(**item))
                    elif item_type == "DVD":
                        item.pop("type", None)
                        items.append(DVD(**item))
                return items
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error loading items: {e}")
            return []
        

     def load_users(self):
          try:
             with open(self.users_file, "r") as f:
                data = json.load(f)
                return [User(**user) for user in data] # (**)>shorthand in python for argument in The Constructor 
          except FileNotFoundError:
            return []
          except Exception as e:
            print(f"Error loading users: {e}")
            return [] 
        

     def save_data(self):
        try:
            items_data = []
            for item in self.items:
                d = item.__dict__.copy()
                d["type"] = item.__class__.__name__
                items_data.append(d)
            with open(self.items_file, "w") as f:
                json.dump(items_data, f, indent=4)

            users_data = [user.__dict__ for user in self.users]
            with open(self.users_file, "w") as f:
                json.dump(users_data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
        finally:
            print("Save operation completed.") 


     def add_item(self, item):
           self.items.append(item)
           self.save_data()

     def remove_item(self, item_id):
            self.items = [item for item in self.items if item.item_id != item_id]   
         
     def add_user(self, User):
             self.users.append(User)

     def remove_user(self, user_id):
            self.users = [user for user in self.users if user.user_id != user_id]        

     def find_user(self, user_id):
            for user in self.users:
               if user.user_id == user_id:
                  return user
            return None

     def find_item(self, item_id):
           for item in self.items:
               if item.item_id == item_id:
                   return item
           return None  

     def borrow_item(self, user_id, item_id):
            
            user = self.find_user(user_id)
            if not user:
                raise UserNotFoundError(f"User with ID {user_id} not found.")
            item = self.find_item(item_id)
            if not item:
                raise ItemNotFoundError(f"Item with ID {item_id} not found.")
            if not item.check_availability():
                raise ItemNotAvailableError(f"Item '{item.title}' is not available.")
            item.available = False
            user.borrowed_items.append(item.item_id)
            print(f"{user.name} borrowed {item.title}.") 

       
     def return_item(self, user_id, item_id):
            user = self.find_user(user_id)
            item = self.find_item(item_id)
            if user and item and item_id in user.borrowed_items:
               user.borrowed_items.remove(item_id)
               item.available = True
               print(f"{user.name} returned {item.title}.")
            else:
               print("Return failed: Invalid user or item.")
       
     def reserve_item(self, user_id, item_id):
            user = self.find_user(user_id)
            if not user:
               raise UserNotFoundError(f"User with ID {user_id} not found.")
            item = self.find_item(item_id)
            if not item:
               raise ItemNotFoundError(f"Item with ID {item_id} not found.")
            if isinstance(item, Reservable):
               item.reserve(user)
            else:
               print("This item cannot be reserved.")
        
          





