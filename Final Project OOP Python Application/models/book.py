

from models.Reservable import Reservable
from models.library_item import LibraryItem

class Book(Reservable, LibraryItem):
     
     def __init__(self, item_id, title, author,genre,available=True):
        super().__init__(item_id, title, author, available)
        self.genre = genre

     def display_info(self):
        print(f"[Book] {self.title} by {self.author} | Genre: {self.genre} | Available: {self.available}")


     def reserve(self, user): #Save User Will borrowed items
        if self.available:
            self.available = False
            user.borrowed_items.append(self.item_id)
            print(f"{user.name} reserved the book '{self.title}'.")
        else:
            print(f"Sorry, the book '{self.title}' is not available.")