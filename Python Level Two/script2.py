class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f'\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\n'
    
    def __len__(self):
        return self.pages

my_book = Book('Random title', 'John Snow', 344)
print(my_book)
print(len(my_book)) 