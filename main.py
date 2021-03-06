from library_funcs import Library
import os

clear = lambda: os.system('cls')

class user:
    def __init__(self, name):
        self.name = name

    def menu_options(self, choice, name):
        if choice == 1:
            clear()
            self.display_book(name)
        elif choice == 2:
            clear()
            self.lend_book(name)
        elif choice == 3:
            clear()
            book = input("Enter the book name : ")
            self.add_book(book, name)
        elif choice == 4:
            clear()
            self.return_book(name)
        elif choice == 5:
            clear()
            exit()
        else:
            print("Not a valid option!")
            user.continue_game()

    @classmethod
    def continue_game(cls, name):
        user1 = user(name)
        user_choice = input("Press q to quit and c to continue : ")
        while (user_choice.lower() != "c" or user_choice.lower() != "q"):
            if user_choice == "q":
                exit()
            elif user_choice == "c":
                user.menu(user1)

    
    def menu(self):
        lib = Library()
        clear()
        print(f"\n\n\nWelcome to the library:")
        print("1. Display Book List")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        print("5. Exit")
        choice = int(input("Enter your choice : "))
        user.menu_options(lib, choice, self.name)


if __name__ == "__main__":
    name = input("Enter your name : ")
    user1 = user(name)
    user1.menu()

        