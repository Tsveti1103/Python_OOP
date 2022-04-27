class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            self.rented_books[user.username] = {book_name: days_to_return}
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'

    def return_book(self, author, book_name, user):
        if book_name in user.books:
            user.books.remove(book_name)
            if book_name in self.rented_books[user.username]:
                self.rented_books[user.username].pop(book_name)
            if author not in self.books_available:
                self.books_available[author] = []
            self.books_available[author].append(book_name)
        return f"{user.username} doesn't have this book in his/her records!"

