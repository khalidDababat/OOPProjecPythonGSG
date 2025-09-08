
from models.library_item import LibraryItem
from  models.Reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration, available=True):
        super().__init__(item_id, title, author, available)
        self.duration = duration

    def display_info(self):
        print(f"[DVD] {self.title} by {self.author} | Duration: {self.duration} mins | Available: {self.available}")

    def reserve(self, user):
        if self.available:
            self.available = False
            user.borrowed_items.append(self.item_id)
            print(f"{user.name} reserved the DVD '{self.title}'.")
        else:
            print(f"Sorry, the DVD '{self.title}' is not available.")

