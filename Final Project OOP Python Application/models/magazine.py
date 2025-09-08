
from models.library_item import LibraryItem
from models.Reservable import Reservable


class Magazine(LibraryItem,Reservable):  
    def __init__(self, item_id, title, author, issue, available=True):
        super().__init__(item_id, title, author, available)
        self.issue = issue

    def display_info(self):
        print(f"[Magazine] {self.title} (Issue: {self.issue}) by {self.author} | Available: {self.available}")
     

    def reserve(self, user): #Save User Will borrowed items
        if self.available:
            self.available = False
            user.borrowed_items.append(self.item_id)
            print(f"{user.name} reserved the book '{self.title}'.")
        else:
            print(f"Sorry, the book '{self.title}' is not available.") 