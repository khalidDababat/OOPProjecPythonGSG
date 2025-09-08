


class User:   # user class 
    def __init__(self, user_id, name ,borrowed_items=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = borrowed_items if borrowed_items is not None else []
   
    def display_info(self):
        print(f"User: {self.name} (ID: {self.user_id}) | Borrowed Items: {self.borrowed_items}") 

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"    