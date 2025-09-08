 
from models.library import Library
from models.user import User
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.Reservable import Reservable

from exceptions.item_not_available import ItemNotAvailableError
from exceptions.user_not_found import UserNotFoundError
from exceptions.item_not_found import ItemNotFoundError

class Main: 
    def run(self):
        print("Running the main application...")
        library = Library() 
        


        while True:
            print("\nWelcome to the Library System")
            print("1. View all available items")#
            print("2. Search item by title")#
            print("3. Register a new user")#
            print("4. Add new item")# add item and Save Automatically 
            print("5. Borrow an item")
            print("6. Reserve an item")
            print("7. Return an item")
            print("8. Exit and Save")
            
            selection = input("Please select an option (1-7): ")
            if selection == "1":
                for item in library.items:
                         item.display_info() 
            elif selection =="2":
                  keyword = input("Enter title keyword: ").lower()
                  results = [item for item in library.items if keyword in item.title.lower()]
                  for item in results:
                     item.display_info()
            elif selection =="3":
                 name = input("Enter user name: ")
                 user_id =len(library.users)+1
                 library.add_user(User(user_id, name))
                 print(f"User '{name}' added with ID {user_id}.")  # When Save Enter 7 Will Show In JSON 
            elif selection =="4": 
                   print("Choose item type: 1. Book  2. Magazine  3. DVD")
                   type = input("Enter type: ")
                   item_id = f"{len(library.items)+1}"
                   title = input("Enter title: ")
                   author = input("Enter author: ") 

                   if type == "1":
                    genre = input("Enter genre: ")
                    item = Book(item_id, title, author, genre)
                   elif type == "2":
                    issue = input("Enter issue number: ")
                    item = Magazine(item_id, title, author, issue)
                   elif type== "3":
                    duration = input("Enter duration: ")
                    item = DVD(item_id, title, author, duration)
                   else:
                      print("Invalid type.")
                      continue
                   library.add_item(item)
                   print(f"Item '{title}' added successfully!") 

            elif selection =="5": 
                 user_id = input("Enter your user ID: ")
                 item_id = input("Enter item ID to borrow: ")
                
                 try:
                    library.borrow_item(user_id, item_id)
                 except (ItemNotAvailableError, UserNotFoundError, ItemNotFoundError) as e:
                     print(e) 
            elif selection =="6":
                 uid = input("Enter your user ID: ")
                 iid = input("Enter item ID to reserve: ")
                 try:
                    library.reserve_item(uid, iid)
                 except (ItemNotAvailableError, UserNotFoundError, ItemNotFoundError) as e:
                     print(e)              
            
            elif selection =="7":
                 uid = input("Enter your user ID: ")
                 iid = input("Enter item ID to return: ")
                 library.return_item(uid, iid)
            
            elif selection =="8": 
                   library.save_data()
                   print("Exiting...")
                   break 
            
            else: 
                  print("Invalid option. Try again.")

      






if __name__ == "__main__":
    main_app = Main()
    main_app.run()        