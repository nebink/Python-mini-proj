class BookStore:
    noOfBooks = 0 # Class level variable

    def __init__(self, title, author, publisher, price):
        self.__title = title # private instance variable
        self.__author = author # private instance variable
        self.__publisher = publisher # private instance variable
        self.__price = price # private instance variable
        BookStore.noOfBooks += 1

    def BookInfo(self):
        print("Title:", self.__title)
        print("Author:", self.__author)
        print("Publisher:", self.__publisher)
        print("Price:", self.__price)

# Creating instances of the class
book1 = BookStore("The Alchemist", "Paulo Coelho", "HarperCollins Publishers", "$9.99")
book2 = BookStore("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", "Crown Publishers", "$16.00")
book3 = BookStore("To Kill a Mockingbird", "Harper Lee", "J. B. Lippincott & Co.", "$12.99")

# Displaying details of each book
print("Details of Book 1:")
book1.BookInfo()
print("\nDetails of Book 2:")
book2.BookInfo()
print("\nDetails of Book 3:")
book3.BookInfo()

# Displaying number of books created
print("\nNumber of books created:", BookStore.noOfBooks)
