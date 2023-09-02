import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Library_System import *


class AddBookWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # Load Ui
        loadUi("Windows Designs/AddBook.ui", self)

        # define Widgets
        self.lineEdit_BookName = self.findChild(QLineEdit, "lineEdit_BookName")
        self.lineEdit_Author = self.findChild(QLineEdit, "lineEdit_Author")
        self.lineEdit_Section = self.findChild(QLineEdit, "lineEdit_Section")
        self.lineEdit_Cost = self.findChild(QLineEdit, "lineEdit_Cost")
        self.lineEdit_Units = self.findChild(QLineEdit, "lineEdit_Units")
        self.label_BookName = self.findChild(QLabel, "label_BookName")
        self.label_Author = self.findChild(QLabel, "label_Author")
        self.label_Section = self.findChild(QLabel, "label_Section")
        self.label_Cost = self.findChild(QLabel, "label_Cost")
        self.label_Units = self.findChild(QLabel, "label_Units")
        self.MessageLabel = self.findChild(QLabel, "MessageLabel")
        self.AddButton = self.findChild(QPushButton, "AddButton")

        # Functions
        self.AddButton.clicked.connect(self.AddData)

        # Show Ui
        self.show()

    def AddData(self):
        Data = Section().addBook(newTitle=self.lineEdit_BookName.text(), newAuthor=self.lineEdit_Author.text(),
                                 newSection=self.lineEdit_Section.text(), newCost=self.lineEdit_Cost.text(),
                                 newUnits=self.lineEdit_Units.text())

        self.MessageLabel.setText(f"{self.lineEdit_BookName.text().title()} \nis Add to\nLibrary Database")
        self.lineEdit_BookName.clear()
        self.lineEdit_Author.clear()
        self.lineEdit_Section.clear()
        self.lineEdit_Cost.clear()
        self.lineEdit_Units.clear()


class DeleteBookWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # Load Ui
        loadUi("Windows Designs/DeleteBook.ui", self)

        # define Widgets
        self.lineEdit_BookName = self.findChild(QLineEdit, "lineEdit_BookName")
        self.label_BookName = self.findChild(QLabel, "label_BookName")
        self.MessageLabel = self.findChild(QLabel, "MessageLabel")
        self.DeleteButton = self.findChild(QPushButton, "DeleteButton")

        # Functions
        self.DeleteButton.clicked.connect(self.DeleteData)

        # Show Ui
        self.show()

    def DeleteData(self):
        Data = Section().deleteBook(book_name=self.lineEdit_BookName.text().title())
        self.MessageLabel.setText(f"{self.lineEdit_BookName.text().title()} \nis Deleted from\nLibrary Database")
        self.lineEdit_BookName.clear()


class SellBookWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # Load Ui
        loadUi("Windows Designs/SellBook.ui", self)

        # define Widgets
        self.lineEdit_BookName = self.findChild(QLineEdit, "lineEdit_BookName")
        self.label_BookName = self.findChild(QLabel, "label_BookName")
        self.MessageLabel = self.findChild(QLabel, "MessageLabel")
        self.SellButton = self.findChild(QPushButton, "SellButton")

        # Functions
        self.SellButton.clicked.connect(self.SellBook)

        # Show Ui
        self.show()

    def SellBook(self):
        data = Library().sellBook(title=self.lineEdit_BookName.text().title())
        self.MessageLabel.setText(f"The Book : {self.lineEdit_BookName.text().title()}\nis Sold for price of : {data[0]}")
        self.lineEdit_BookName.clear()


# class GetProfitsWindow(QMainWindow):
#     def __init__(self):
#         super(QMainWindow, self).__init__()
#
#         # Load Ui
#         loadUi("Windows Designs/GetProfits.ui", self)
#
#         # define Widgets
#         self.GetProfitsTableWidget = self.findChild(QTableWidget, "tableWidget")
#         self.GetProfitsTableWidget.setColumnWidth(0, 650)
#         self.GetProfitsTableWidget.setColumnWidth(1, 250)
#         self.MessageLabel = self.findChild(QLabel, "Profits")
#
#         # Functions
#         self.GetProfits()
#         self.loadData()
#
#         # Show Ui
#         self.show()
#
#     def GetProfits(self):
#         data = Library().getTotalProfit()
#         self.MessageLabel.setText(f"{data[0]}")

    def loadData(self):
        soldList = Library().getTotalProfit()
        row = 0
        self.tableWidget.setRowCount(len(soldList))
        for book in soldList[1]:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(book['Book Name'][book]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(book['cost'][book]))
            row = row + 1


class BookListWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        # Load Ui
        loadUi("Windows Designs/BookListWindow.ui", self)

        # define Widgets
        self.BookListTableWidget = self.findChild(QTableWidget, "tableWidget")
        self.BookListTableWidget.setColumnWidth(0, 350)
        self.BookListTableWidget.setColumnWidth(1, 250)
        self.BookListTableWidget.setColumnWidth(2, 150)
        self.BookListTableWidget.setColumnWidth(3, 100)
        self.BookListTableWidget.setColumnWidth(4, 79)

        # Functions
        self.loadData()

        # Show Ui
        self.show()

    def loadData(self):
        Books = Section().showLibrary()
        row = 0
        self.tableWidget.setRowCount(len(Books))
        for book in Books:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(book))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(Books[book]["author"]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(Books[book]["section"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Books[book]["cost"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(Books[book]["units"])))
            row = row + 1


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load Ui
        loadUi("Windows Designs/LibraryMainWindow.ui", self)

        # Define Widgets
        self.BookListButton = self.findChild(QPushButton, "BookListButton")
        self.AddBookButton = self.findChild(QPushButton, "AddBookButton")
        self.DeleteBookButton = self.findChild(QPushButton, "DeleteBookButton")
        self.SearchByTitleButton = self.findChild(QPushButton, "SearchBookByTitleButton")
        self.SearchByAuthorButton = self.findChild(QPushButton, "SearchBookByAuthorButton")
        self.ShowLibrarySectionsButton = self.findChild(QPushButton, "ShowLibrarySectionsButton")
        self.SellBookButton = self.findChild(QPushButton, "SellBookButton")
        self.GetProfitsButton = self.findChild(QPushButton, "GetProfitsButton")

        # Button Function
        self.BookListButton.clicked.connect(self.show_BookList)
        self.AddBookButton.clicked.connect(self.show_AddBook)
        self.DeleteBookButton.clicked.connect(self.show_DeleteBook)
        self.SearchByTitleButton.clicked.connect(self.show_SearchByTitle)
        self.SearchByAuthorButton.clicked.connect(self.show_SearchByAuthor)
        self.SellBookButton.clicked.connect(self.show_SellBook)
        self.GetProfitsButton.clicked.connect(self.show_GetProfits)
        self.ShowLibrarySectionsButton.clicked.connect(self.show_ShowLibrarySections)

        self.show()

    def show_BookList(self):
        self.newwindow = BookListWindow()
        self.newwindow.setWindowTitle("Library Book List")
        self.newwindow.show()

    def show_AddBook(self):
        self.newwindow = AddBookWindow()
        self.newwindow.setWindowTitle("Add Book")
        self.newwindow.show()

    def show_DeleteBook(self):
        self.newwindow = DeleteBookWindow()
        self.newwindow.setWindowTitle("Delete Book")
        self.newwindow.show()

    def show_SearchByTitle(self):
        # self.newwindow = BookListWindow()
        # self.newwindow.show()
        pass

    def show_SearchByAuthor(self):
        # self.newwindow = BookListWindow()
        # self.newwindow.show()
        pass

    def show_SellBook(self):
        self.newwindow = SellBookWindow()
        self.newwindow.setWindowTitle("Sell Book")
        self.newwindow.show()

    # def show_GetProfits(self):
    #     self.newwindow = GetProfitsWindow()
    #     self.newwindow.setWindowTitle("Get Profits")
    #     self.newwindow.show()

    def show_ShowLibrarySections(self):
        # self.newwindow = BookListWindow()
        # self.newwindow.show()
        pass


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.setWindowTitle("Homepage")

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
