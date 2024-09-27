class Book:
    def __init__(self, category, id, name, quantity) -> None:
        self.category = category
        self.id = id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} (Category: {self.category}, ID: {self.id}, Quantity: {self.quantity})'


class User:
    def __init__(self, id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrowed_books = []
        self.returned_books = []

    def __str__(self):
        return f'User: {self.name} (ID: {self.id})'


class Library:
    def __init__(self, owner, name) -> None:
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, category, id, name, quantity):
        book = Book(category, id, name, quantity)
        self.books.append(book)
        print(f'\n\t{name} book added successfully.')

    def add_user(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
        print(f'\n\tUser {name} added successfully.')
        return user
    
    def borrow_book(self, user, id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowed_books:
                    print('\n\tAlready borrowed this book!')
                    return
                elif book.quantity < 1:
                    print("\n\tNo available copies!")
                else:
                    user.borrowed_books.append(book)
                    book.quantity -= 1
                    print(f'\n\t{book.name} borrowed successfully!')
                    return
        print(f'\n\tBook with ID {id} not found.')

    def return_book(self, user, id):
        for book in user.borrowed_books:
            if book.id == id:
                user.borrowed_books.remove(book)
                user.returned_books.append(book)
                book.quantity += 1
                print(f'\n\t{book.name} returned successfully.')
                return
        print(f'\n\tYou have not borrowed a book with ID {id}.')

# Instantiate the library
Neer = Library('Ismail', 'Neer Pathagor')
admin = Neer.add_user(1, 'admin', 'admin')
rahim = Neer.add_user(43, 'rahim', '1234')
Neer.add_book('Sci-Fi', 15, 'Dune', 5)

# Main program loop
run = True
current_user = admin

while run:
    if current_user is None:
        print(f'\n\tNo user logged in!')
        option = input("Login or Register (L/R): ").strip().upper()

        if option == 'R':
            id = int(input("\n\tEnter ID: "))
            name = input("\n\tEnter Name: ")
            password = input("\n\tEnter Password: ")
            current_user = Neer.add_user(id, name, password)

        elif option == 'L':
            id = int(input("\tEnter ID: "))
            password = input('\tEnter Password: ') 
            match = False
            for user in Neer.users:
                if user.id == id and user.password == password:
                    current_user = user
                    match = True
                    print(f'\n\tWelcome, {user.name}!')
                    break

            if not match:
                print(f'\n\tNo matching user found!')
    
    else:
        if current_user.name == 'admin':
            print('\nOptions: ')
            print("1 : Add Book")
            print("2 : Show Users")
            print("3 : Show Books")
            print("4 : Logout")

            ch = int(input("\nEnter Option: "))
            if ch == 1:
                cat = input("\tEnter category: ")
                id = int(input("\tEnter ID: "))
                name = input("\tEnter Name: ")
                q = int(input("\tEnter quantity: "))
                Neer.add_book(cat, id, name, q)

            elif ch == 2:
                for user in Neer.users:
                    print(user)

            elif ch == 3:
                for book in Neer.books:
                    print(book)

            elif ch == 4:
                current_user = None

        else:
            print('\nOptions: ')
            print("1 : Borrow Book")
            print("2 : Return Book")
            print("3 : Show Available Books")
            print("4 : Show Returned Books")
            print("5 : Logout")

            ch = int(input("\nEnter Option: "))
             
            if ch == 1:
                id = int(input("\tEnter book ID: "))
                Neer.borrow_book(current_user, id)

            elif ch == 2:
                id = int(input("\tEnter book ID to return: "))
                Neer.return_book(current_user, id)

            elif ch == 3:
                for book in Neer.books:
                    print(book)

            elif ch == 4:
                if current_user.returned_books:
                    print("\nReturned Books:")
                    for book in current_user.returned_books:
                        print(book)
                else:
                    print("\nNo books returned yet.")

            elif ch == 5:
                current_user = None
