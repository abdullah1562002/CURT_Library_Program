import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Database Initialization

cred = credentials.Certificate("curt-task-1-firebase-adminsdk-s62aa-788aca2877.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://curt-task-1-default-rtdb.firebaseio.com"
})

database = db.reference("/")


# print(database.get())


# Application Classes

class Book:

    def __int__(self, title, author, cost, units):
        self.title = title
        self.author = author
        self.cost = cost
        self.units = units

    def getTitle(self, book_title):
        return book_title

    def getAuthor(self, book_name):
        self.author = database.child(book_name).get()
        return self.author['author']

    def getCost(self, book_name):
        self.author = database.child(book_name).get()
        return self.author['cost']

    def getUnits(self, book_name):
        self.author = database.child(book_name).get()
        return self.author['units']


class Section:

    def __init__(self):
        self.All_Library = None

    def __int__(self, secTitle, books):
        self.secTitle = secTitle
        self.books = books
        self.author = None

    def getSectionTitle(self, book_name):
        self.secTitle = database.child(book_name).get()
        return self.secTitle['section']

    def addBook(self, newTitle, newAuthor, newSection, newCost, newUnits):

        newBook = {f"{newTitle.title()}":

            {
                "author": f"{newAuthor.title()}",
                "section": f"{newSection.title()}",
                "cost": int(newCost),
                "units": int(newUnits)
            }
        }

        # Updating newBook to firebase
        database.update(newBook)


    def searchBookByTitle(self, book_Title):
        self.title = database.get()
        book_names = list(self.title.keys())
        # print(book_names)

        for book in book_names:
            if book == book_Title:
                Book_Name = Book.getTitle(self, book_title=book_Title)
                return Book_Name
        else:
            return "Book Not Found"

    def searchBookByAuthor(self, author):
        self.author = database.get()

        for i in self.author:
            # print(i)
            if self.author[i]["author"] == author:
                book_Title = i
                Book_Name = Book.getTitle(self, book_title=book_Title)
                return Book_Name
        else:
            return "Book Not Found"

    def deleteBook(self, book_name):
        database.child(f"{book_name.title()}").delete()



    def showBooks(self, section):
        self.section = database.get()
        Book_Names = []

        for book in self.section:
            # print(i)
            if self.section[book]["section"] == section:
                Book_Names.append(book)

        return Book_Names

    def showLibrary(self):
        self.All_Library = database.get()
        # print(self.All_Library)
        return self.All_Library

class Library:
    def __int__(self, title, sections, profit):
        self.title = title
        self.sections = sections
        self.profit = profit

    def booksOFSection(self, section):
        # Dictionary For Books of The same Section

        sections_Dict = {
            'section': section,
            'books': [],
            'author': [],
            'cost': [],
            'units': []
        }

        # fetching Latest Database Update
        self.sections = database.get()

        # looping through database and updating books of the same section list
        for element in self.sections:
            if self.sections[element]['section'] == section:
                sections_Dict['books'].append(element)  # adding book names to Dict
                sections_Dict['author'].append(self.sections[element]['author'])  # adding author names to Dict
                sections_Dict['cost'].append(self.sections[element]['cost'])  # adding books cost to Dict
                sections_Dict['units'].append(self.sections[element]['units'])  # adding book units to Dict

        return sections_Dict

    def addSection(self, section):
        # Adding book to passed section
        Section.addBook(self, newTitle="John Wick", newAuthor="Densel. L", newSection=section, newCost=320, newUnits=1)
        return Library.booksOFSection(self, section=section)

    def searchBookByTitle(self, section, title, ):
        sec_list = Library.booksOFSection(self, section=section)
        counter = 0
        book_list = []

        for element in sec_list['books']:
            if element == title.title():
                book_list = [title.title(), sec_list['author'][counter], section, sec_list['cost'][counter],
                             sec_list['units'][counter]]

            counter += 1
        if len(book_list == 0):
            return f"Book : {title.title()} is Not Found"

        return book_list

    def searchBookByAuthor(self, section, author):
        sec_list = Library.booksOFSection(self, section=section)
        counter = 0

        book_Dict = {
            "books": [],
            "author": author.title(),
            "section": section,
            "cost": [],
            "units": []

        }

        # print(sec_list)
        for element in sec_list['author']:
            if element == author.title() or element == author.upper():
                book_Dict['books'].append(sec_list['books'][counter])
                book_Dict['cost'].append(sec_list['cost'][counter])
                book_Dict['units'].append(sec_list['units'][counter])
            counter += 1

        if len(book_Dict['books']) == 0:
            return f"Book with {author.title()} is Not Found"

        return book_Dict

    def sellBook(self, title):
        # Dict for selled Books
        global selled_books
        selled_books = {
            'Book Name': [],
            'cost': []
        }

        # Getting Books Cost

        self.profit = int(database.child(f"{title.title()}/cost").get())

        # Appending Selled Books to Dict
        selled_books['Book Name'].append(title)
        selled_books['cost'].append(self.profit)

        # delete Sold Book from Dict
        database.child(f"{title.title()}").delete()
        return self.profit, selled_books

    def getTotalProfit(self):
        self.profit = 0
        profits_list = selled_books['cost']
        for element in profits_list:
            self.profit += element
        return self.profit, selled_books
