class CLI: # Class to handle the command line interface
    def display_menu(self): # Method to display the main menu
        try:
                print ('''
                Welcome to the Library Management System!

                Main Menu: 📃✨
                1. Book Operations
                2. User Operations
                3. Author Operations
                4. Quit
                ''')
        except Exception as e:
                print(f"\n\n\n༼ つ ◕_◕ ༽つError while displaying main menu: {e} ..Try again! ")

    def display_books(self): # Method to display the book operations menu
        try:    
                print ('''
                Book Operations: 📚
                1. Add a new book
                2. Borrow a book
                3. Return a book
                4. Search for a book
                5. Display all books
                6. Back to main menu
                ''') 
        except Exception as e:
                print(f"\n\n\n༼ つ ◕_◕ ༽つError while displaying book operations menu: {e} ..Try again! ")       

    def display_users(self): # Method to display the user operations menu
        try:
                print ('''
                User Operations: 👥
                1. Add a new user
                2. View user details
                3. Display all users
                4. Back to main menu
                ''')
        except Exception as e:
                print(f"\n\n\n༼ つ ◕_◕ ༽つError while displaying user operations menu: {e} ..Try again! ")

    def display_authors(self): # Method to display the author operations menu
        try:
                print ('''
                Author Operations: ✍📕
                1. Add a new author
                2. View author details
                3. Display all authors
                4. Back to main menu
                ''')
        except Exception as e:
                print(f"\n\n\n༼ つ ◕_◕ ༽つError while displaying author operations menu: {e} ..Try again! ")        
