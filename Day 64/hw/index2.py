class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"
my_book = Book("1984", "George Orwell", 1949)
print(my_book)