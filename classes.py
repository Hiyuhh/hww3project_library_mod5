class Book:
    def __init__(self, title, author, ISBN, genre, publication_date, author_id, availability): # Constructor
        try:
            self.titles = title #(public attribute)
            self.authors = author #(public attribute)
            self.ISBNs = ISBN #(public attribute)
            self.genres = genre #(public attribute)
            self.publication_dates = publication_date #(public attribute)
            self.availability = availability # List to store the availability of the books (public attribute)
            self.author_id = author_id
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
    
    # def __str__(self): # Method to return the title and author of the book
    #     try:
    #         return f"{self.titles} by {self.authors}"
    #     except Exception as e:
    #         print(f"\n\n\n༼ つ ◕_◕ ༽つError while converting Book to string: {e} ..Try again! ")


class User: 
    def __init__(self, name, library_id): # Constructor
        try:
            self.__name = name # Private attribute
            self.__library_id = library_id # Private attribute
            self.borrowed_books = [] # List to store the borrowed books (public attribute)
            self.borrow_date = [] # List to store the borrowed dates (public attribute)
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")

#----------------------------------------------------Getter and Setter for private attributes----------------------------------------------------#
    def get_name(self): # Getter for private attribute name
        try:
            return self.__name
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError while getting user name: {e} ..Try again! ")

    def set_name(self, name): # Setter for private attribute name
        try:
            self.__name = name
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError while seeting user name: {e} ..Try again! ")

    def get_library_id(self): # Getter for private attribute library_id
        try:
            return self.__library_id
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError while getting library ID: {e} ..Try again! ")

    def set_library_id(self, library_id): # Setter for private attribute library_id
        try:
            self.__library_id = library_id
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError while setting library ID: {e} ..Try again! ")

#---------------------------------------------------------------------------------------------------------------------------------------------#

class Author: 
    def __init__(self, name, bio): # Constructor
        try:
            self.name = name
            self.biography = bio
        except Exception as e:
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
