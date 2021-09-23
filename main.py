from library_funcs import Library

class user:
    def __init__(self, name):
        self.name = name

    def menu_options(self, choice):
        if choice == 1:
            self.display_book()
        elif choice == 2:
            self.lend_book()
        elif choice == 3:
            self.add_book()
        elif choice == 4:
            self.return_book()
    
    def menu(self):
        lib = Library(self.name)
        print(f"Welcome to {self.name}'s library:")
        print("1. Display Book List")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        choice = int(input("Enter your choice : "))
        user.menu_options(lib, choice)


name = input("Enter your name : ")
user1 = user(name)
user1.menu()

        