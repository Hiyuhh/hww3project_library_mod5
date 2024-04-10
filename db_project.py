from connect_db import connect_db 
from cli import CLI
from classes import Book, User, Author
from datetime import date # Import the date module from the datetime library

def library(): # Main function to run the library management system
    global books, users, authors, borrowed_books # Global variables to store the books, users, authors, and borrowed books
    books = []
    users = []
    authors = []
    borrowed_books = []
    database() # Pull info from MySQL


    while True:
        try: 
            CLI().display_menu() # Display the main menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Book Operations
                book_op(books, users)
            elif user_input == "2": # User Operations
                user_op(users) 
            elif user_input == "3": # Author Operations
                author_op(authors)
            elif user_input == "4": # Quit
                print("\nThank you for using the Library Management System! Goodbye! 👋\n")
                break 
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue


def book_op(books, users): # Method to handle book operations
    while True: 
        try:
            CLI().display_books() # Display the book operations menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Add a new book
                add_book(books)
            elif user_input == "2": # Borrow a book
                borrow_book(books, users)
            elif user_input == "3": # Return a book
                return_book(books, users)
            elif user_input == "4": # Search for a book
                search_book(books, users)
            elif user_input == "5": # Display all books
                all_books(books)
            elif user_input == "6": # Back to main menu
                break
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue

def user_op(users): # Method to handle user operations
    while True:
        try:
            CLI().display_users() # Display the user operations menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Add a new user
                add_user(users)
            elif user_input == "2": # View user details
                user_details(users)
            elif user_input == "3": # Display all users
                all_users(users)
            elif user_input == "4": # Back to main menu
                break
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue

def author_op(authors): # Method to handle author operations
    while True:
        try:
            CLI().display_authors() # Display the author operations menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Add a new author
                add_author(authors)
            elif user_input == "2": # View author details
                author_details(authors)
            elif user_input == "3": # Display all authors
                all_authors(authors)
            elif user_input == "4": # Back to main menu
                break
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
#----------------------------------------------------Methods to pull info from MySQL----------------------------------------------------#
def database(): # Method to pull info from MySQL
        conn = connect_db() # Connect to the database
        if conn:
            try:
                cursor = conn.cursor() # Create a cursor object
                try:
                    global books, users, authors, borrowed_books # Global variables to store the books, users, authors, and borrowed books
                    books.clear() # Clear the books list
                    users.clear() # Clear the users list
                    authors.clear() # Clear the authors list
                    borrowed_books.clear() # Clear the borrowed books list

                    query = "SELECT * FROM books" # Query to select all books from the books table
                    cursor.execute(query) # Execute the query
                    for book in cursor.fetchall(): # Loop through the books
                        books.append(book) # Add the book to the books list

                    query = "SELECT * FROM users" # Query to select all users from the users table
                    cursor.execute(query) 
                    for user in cursor.fetchall(): # Loop through the users
                        users.append(user) # Add the user to the users list

                    query = "SELECT * FROM authors" # Query to select all authors from the authors table
                    cursor.execute(query)
                    for author in cursor.fetchall():
                        authors.append(author)

                    query = "SELECT * FROM borrowed_books" # Query to select all borrowed books from the borrowed_books table
                    cursor.execute(query)
                    for row in cursor.fetchall(): # Loop through the borrowed books
                        borrowed_books.append(row)
                                        
                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            finally: # Close the cursor and connection
                cursor.close()
                conn.close()
#-----------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------Methods for display_books----------------------------------------------------#
def  add_book(books): # Method to add a new book
    while True:
        conn = connect_db() # Connect to the database
        if conn: # If the connection is successful
            try:
                cursor = conn.cursor() # Create a cursor object
                try:
                    print("\n((Be sure to add the author first before adding the book))")
                    title = input("What is the name of the book you would like to add? (Back)\n")
                    if title.lower() == "back": # If user wants to go back to the main menu
                        return 

                    author = input("\nWho is the author of the book? ")
                    ISBN = input("\nWhat is the ISBN of the book? ")
                    genre = input("\nWhat is the genre of the book? ")
                    publication_date = input("\nWhat is the publication date of the book? ")
                    availability = True # Default availability of the book

                    query = "SELECT id FROM authors WHERE name = %s" # Query to select the author ID from the authors table
                    cursor.execute(query, (author,)) 
                    author_id = cursor.fetchall()[0][0] # Get the author ID
                    new_book = Book(title, author, ISBN, genre, publication_date, availability, author_id) # Create a new book object
                    books.append(new_book) # Add the new book to the books list
                    book_added = f"{new_book}" # Get the title and author of the book
                    insert_info = (title, author, ISBN, genre, publication_date, availability, author_id) # Insert the book info into the database
                    query = "INSERT INTO books (title, author, ISBN, genre, publication_date, availability, author_id) VALUES (%s,%s, %s, %s, %s, %s, %s)" # Query to insert the book info into the books table
                    cursor.execute(query, insert_info) # Execute the query
                    conn.commit() # Commit the changes to the database

                    print(f"\nYou have successfully added '{book_added}' to the library! 📖\n")
                    print(f"~Succesfully added to the database~")
                    break # Back to main menu

                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()

def borrow_book(books, users): # Method to borrow a book
    while True:
        conn = connect_db() # Connect to the database
        if conn: # If the connection is successful
            try:
                cursor = conn.cursor()
                try:
                    title = input("\nWhat is the name of the book you would like to borrow? (Back)\n") # Ask the user for the book title
                    if title.lower() == "back": # If user wants to go back to the main menu
                        return
                    unique_id = input("\nWhat is your Library ID: ") # Ask the user for their Library ID

                    book_found = None # Initialize book_found to None
                    for book in books: # Loop through the books
                        if book[1].lower() == title.lower(): # If the book is found
                            book_found = book # Set book_found to the book
                            break

                    if book_found is not None: # If the book is found
                        if book_found[6] == 1: # If the book is available
                            user_found = None # Initialize user_found to None
                            for user in users: # Loop through the users
                                if user[2] == unique_id: # If the user is found
                                    user_found = user # Set user_found to the user
                                    break
                                
                            if user_found is not None: # If the user is found
                                borrow_date = date.today() # Get the current date
                                query = "SELECT id FROM users WHERE library_id = %s" # Query to select the user ID from the users table
                                cursor.execute(query, (unique_id,))
                                user_id = cursor.fetchall()[0][0] # Get the user ID
                                query = "SELECT id FROM books WHERE title = %s" # Query to select the book ID from the books table
                                cursor.execute(query, (title,))
                                book_id = cursor.fetchall()[0][0] # Get the book ID
                                query = "UPDATE books SET availability = %s WHERE title = %s" # Query to update the availability of the book in the books table
                                cursor.execute(query, (0, title))
                                query = "INSERT INTO borrowed_books (title, user, borrow_date, book_id, user_id) VALUES (%s, %s, %s, %s, %s)" # Query to insert the borrowed book info into the borrowed_books table
                                cursor.execute(query, (title, user_found[1], borrow_date, book_id, user_id)) # Execute the query
                                conn.commit()
                                database() # Grab book info / borrowed books info from MySQL

                                print(f"\n{user_found[1]}, you have successfully borrowed '{book_found[1]}' from the library! 📖") 
                                print("Book status updated in the database")                    
                                return   
                                             
                            else: # If the user is not found
                                print(f"\nSorry, you are not a registered user in the library.\n")
                                return
                            
                        elif book_found[6] == 0: # If the book is not available
                            print(f"\n📖 '{book_found[1]}' is currently being borrowed.\n"
                                  "Would you like to borrow another book? (Yes/No)\n")
                            user_input = input() # Ask the user if they would like to borrow another book
                            if user_input.lower() == "yes":
                                continue
                            elif user_input.lower() == "no":
                                return
                            
                    else: # If the book is not found
                        print(f"\nSorry, '{title}' is not available in the library database.\n")
                        continue

                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()

def return_book(books, users): # Method to return a book
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                try:
                    title = input("\nWhat is the name of the book you would like to return? (Back)\n") # Ask the user for the book title
                    if title.lower() == "back": # If user wants to go back to the main menu
                        return
                    unique_id = input("\nWhat is your Library ID: ") # Ask the user for their Library ID

                    book_found = None # Initialize book_found to None
                    for book in books: # Loop through the books
                        if book[1].lower() == title.lower(): # If the book is found
                            book_found = book # Set book_found to the book by title and author
                            break

                    if book_found is not None: # If the book is found
                        if book_found[6] == 0: # If the book is not available
                            user_found = None # Initialize user_found to None
                            for user in users: # Loop through the users
                                if user[2] == unique_id: # If the user is found
                                    user_found = user # Set user_found to the user
                                    break

                            if user_found is not None: # If the user is found
                                    return_date = date.today() # Get the current date
                                    query = "UPDATE borrowed_books SET return_date = %s WHERE title = %s AND user = %s" # Query to add the return date of the borrowed book in the borrowed_books table
                                    cursor.execute(query, (return_date, title, user_found[1]))
                                    query = "UPDATE books SET availability = %s WHERE title = %s" # Query to update the availability of the book in the books table
                                    cursor.execute(query, (1, title))
                                    conn.commit()
                                    database() # Grab book info / borrowed books info from MySQL

                                    print(f"\n{user_found[1]}, you have successfully returned '{book_found[1]}' to the library! 📖")
                                    print("Book status updated in the database")                    
                                    return        
                                        
                            else: # If the user is not found
                                print(f"\nSorry, you are not a registered user in the library.\n")
                                return
                            
                        elif book_found[6] == 1: # If the book is available
                            print(f"\n📖 '{book_found[1]}' is not currently being borrowed.\n" 
                                    "Review your input and try again...\n")
                            continue

                    else: # If the book is not found
                        print(f"\nSorry, '{title}' is not available in the library database.\n")
                        continue

                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()


def search_book(books, users): # Method to search for a book
    while True:
        conn = connect_db() # Connect to the database
        if conn:
            try:
                cursor = conn.cursor() # Create a cursor object
                try:
                    search_input = input("\nWhat is the name of the book you would like to search for? (Back)\n")
                    if search_input.lower() == "back": # If user wants to go back to the main menu
                        return
                    
                    book_found = None # Initialize book_found to None
                    for book in books: # Loop through the books
                        if book[1].lower() == search_input.lower(): # If the book is found
                            book_found = book # Set book_found to the book
                            break

                    if book_found is not None: # If the book is found
                        query = "SELECT * FROM books WHERE title = %s" # Query to select the book info from the books table
                        cursor.execute(query, (search_input,))
                        book = cursor.fetchall()
                        database() # Grab book info / borrowed books info from MySQL

                        if book_found[6] == 1: # If the book is available
                            print(f"\n📖 '{book_found[1]}' is available in the library! Would you like to borrow it? (Yes/No)\n")
                            user_input = input() # Ask the user if they would like to borrow the book
                            if user_input.lower() == "yes": # If the user wants to borrow the book
                                borrow_book(books, users) # Directs the user to the borrow_book method
                                return # Return to the main menu after borrowing the book
                            elif user_input.lower() == "no": # If the user does not want to borrow the book
                                return # Return to the main menu
                            
                        elif book_found[6] == 0: # If the book is not available
                            print(f"\n📖 '{book_found[1]}' is in our library database, but is currently being borrowed.\n")
                            
                    else: # If the book is not found
                        print(f"\nSorry, '{search_input}' is not available in the library database.\n")
                        continue

                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()


def all_books(books): # Method to display all books
    while True:
        conn = connect_db() # Connect to the database
        if conn: # If the connection is successful
            try:
                cursor = conn.cursor()
                try:
                    print("\nAll Books in the Library: 📚")

                    query = "SELECT * FROM books" # Query to select all books from the books table
                    cursor.execute(query)
                    books = cursor.fetchall()
                    database() # Grab book info / borrowed books info from MySQL

                    if not books: # If there are no books in the library
                        print("\n~There are no books in the library yet~")

                    else: # If there are books in the library
                        for book in books: # Loop through the books
                            availability = "Available" if book[6] == 1 else "Unavailable" # Set the availability of the book
                            print(f"📖 {book[1]} by {book[2]} ({book[3]}), ISBN: {book[4]}, Publish Date: {book[5]}, {availability}")

                    input("\nPress enter to go back  ") # Ask the user to press enter to go back to the main menu
                    return # Return to the main menu
                
                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()
          
# # #-----------------------------------------------------------------------------------------------------------------------------------#

# # #----------------------------------------------------Methods for display_users----------------------------------------------------#
def add_user(users): # Method to add a new user
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                try:
                    name = input("\nWhat is your full name? (Back)\n")
                    if name.lower() == "back": # If user wants to go back to the main menu
                        return 
                    
                    unique_id = input("\nCreate a 3-4 digit Library ID # : ") 
                    if len(unique_id) < 3 or len(unique_id) > 4: # If the length of the Library ID is less than 3 or greater than 4
                        print("\nPlease enter a 3-4 digit Library ID #.\n")   
                        continue # Redirect the user to the beginning of the loop to try again

                    if any(user[2] == unique_id for user in users): # If the Library ID is already taken
                        print("\nSorry, this Library ID is already taken. Please try again.\n")
                        continue # Redirect the user to the beginning of the loop to try again

                    new_user = User(name, unique_id) # Create a new user object
                    users.append(new_user) # Add the new user to the users list

                    insert_info = (name, unique_id) # Insert the user info into the database
                    query = "INSERT INTO users (name, library_id) VALUES (%s, %s)" # Query to insert the user info into the users table
                    cursor.execute(query, insert_info)
                    conn.commit()

                    print(f"\nYou have successfully added '{name}' to the library! 👥\n")
                    print(f"~Succesfully added to the database~")
                    return # Return to the main menu
                
                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()

def user_details(users): # Method to view user details
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                try:
                    search_input = input("\nWhat is the name of the user you would like to search for? (Back)\n")
                    if search_input.lower() == "back": # If user wants to go back to the main menu
                        return
                    
                    user_found = None # Initialize user_found to track if the user is found
                    for user in users: # Loop through the borrowed books
                        if user[1].lower() == search_input.lower(): # If the user is found 
                            user_found = user # Set user_found to the user to be searched for in the users list
                            break # Break the loop if the user is found

                    if user_found is not None: # If the user has borrowed books
                        cursor.execute("SELECT borrowed_books.title, books.author FROM borrowed_books JOIN books ON borrowed_books.book_id = books.id WHERE user = %s", (search_input,)) # Query to select the title, and author column from the specified tables then joins them and searches for the user that matches the search_input (user's name)
                        borrowed_data = cursor.fetchall() # Grabs the column title from the borrowed_books table and the column author from the books table
                        database() # Grab user info / borrowed books info from MySQL

                        if borrowed_data: # If the user has borrowed books
                            borrow_data = [f"📖 '{book[0]}' by {book[1]}" for book in borrowed_data] # List comprehension to get the borrowed books
                            print(f"\n 👥 {user_found[1]} has borrowed the following books:{', '.join(borrow_data)}\n") # Prints user and borrowed books separated by a ","
                        
                        else: # If the user has not borrowed any books
                            print(f"\n 👥 {user_found[1]} has not borrowed any books yet.\n") 
                            input("\nPress enter to go back  ") 
                            return
                        
                        input("\nPress enter to go back  ") 
                        return
                        
                    else: # If the user is not found
                        print(f"\nSorry, '{search_input}' is not a registered user in the library.\n")
                        continue 

                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()     


def all_users(users): # Method to display all users
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()        
                try:
                    print("\nAll Users in the Library: 👥")
                    query = "SELECT * FROM users" # Query to select all users from the users table
                    cursor.execute(query) 
                    users = cursor.fetchall() # Fetch all the users from the users table
                    database() # Grab the user info from MySQL

                    if not users: # If there are no users in the library
                        print("\n~There are no users in the library yet~")

                    else: # If there are users in the library
                        for user in users: # Loop through the users
                            print(f"👥 {user[1]} - {user[2]}") # Using getter methods to get the privte attributes of user's name and Library ID

                    input("\nPress enter to go back  ")
                    return
                
                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()
        
# # #--------------------------------------------------------------------------------------------------------------------------------------#

# # #----------------------------------------------------Methods for display_authors----------------------------------------------------#
def add_author(authors): # Method to add a new author
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                try:
                    name = input("\nWhat is the name of the author you would like to add? (Back)\n")
                    if name.lower() == "back": # If user wants to go back to the main menu
                        return
                    
                    bio = input("\nWhat is the biography of the author? ")
                    new_author = Author(name, bio) # Create a new author object
                    authors.append(new_author) # Add the new author to the authors list

                    insert_info = (name, bio) # Insert the author info into the database
                    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)" # Query to insert the author info into the authors table
                    cursor.execute(query, insert_info)
                    conn.commit()

                    print(f"\nYou have successfully added '{name}' to the library! 📚\n")
                    print(f"~Succesfully added to the database~")
                    return
                
                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()        

def author_details(authors): # Method to view author details
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                try:
                    search_input = input("\nWhat is the name of the author you would like to search for? (Back)\n")
                    if search_input.lower() == "back": # If user wants to go back to the main menu
                        return
                    
                    author_found = None # Initialize author_found to None
                    for author in authors: # Loop through the authors
                        if author[1].lower() == search_input.lower(): # If the author is found
                            author_found = author # Set author_found to the author
                            break

                    if author_found is not None: # If the author is found
                        query = "SELECT * FROM authors WHERE name = %s" # Query to select the author info from the authors table
                        cursor.execute(query, (search_input,)) 
                        author = cursor.fetchall()
                        database() # Grab author info from MySQL

                        print(f"\n📚 '{author_found[1]}' Biography: {author_found[2]}\n") 
                        input("\nPress enter to go back  ")
                        return
                    
                    else: # If the author is not found
                        print(f"\nSorry, '{search_input}' is not an author in the library database.\n")
                        continue

                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()
        

def all_authors(authors): # Method to display all authors
    while True:
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()        
                try:                    
                    print("\nAll Authors in the Library: 📚")

                    query = "SELECT * FROM authors" # Query to select all authors from the authors table
                    cursor.execute(query)
                    authors = cursor.fetchall()
                    database() # Grab author info from MySQL

                    if not authors: # If there are no authors in the library
                        print("\n~There are no authors in the library yet~")

                    else: # If there are authors in the library
                        for author in authors: # Loop through the authors
                            print(f"📚 {author[1]}, BIO: {author[2]}")

                    input("\nPress enter to go back  ")
                    return
                
                except Exception as e: # Error handling
                    print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
                    continue
            finally:
                cursor.close()
                conn.close()
        
# #---------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    library() # Run the library function

