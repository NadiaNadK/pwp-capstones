class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
      self.email = address
      print("User's email has been updated!")

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", " + " books read: " + len(self.books)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
          print("Same users")

    def read_book(self, book, rating = None):
      self.books[book:rating] = rating 

    def get_average_rating(self):
      total_rating = 0
      for rating in self.rating:
        total_rating += rating
        average_rating = total_rating/len(self.rating)
      return average_rating

    def __hash__(self):
      return hash((self.title, self.isbn))  


class Books:
    def __init__(self, title, isbn):
      self.title = title
      self.isbn = isbn
      self.ratings = []

    def get_title(self):
      return self.title

    def get_isbn(self):
      return self.isbn

    def set_isbn(self, new_isbn):
      self.isbn = new_isbn
      print("Book's ISBN has been updated")
      return self.isbn 

    def add_rating(self, rating):
      self.rating = []
      if rating >= 0 and rating <=4:
        self.rating.append(rating) 
      else:
        return "Invalid Rating"

    def __eq__(self, other_book):
      if self.title == other_book.title and self.isbn == other_book.isbn:
        print("Both of the books are same")

    def __hash__(self):
      return hash((self.title, self.isbn))  

class Fiction(Books):
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author

  def get_author(self):
    return self.author

  def __repr__(self):
    return "{title} by {author}".format(title=self.title, author= self.author)

class Non_Fiction(Books):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
  def __init__(self):
    self.users = {}
    self.books = {}

  def create_book(self, title, isbn):
    return Books(title, isbn)

  def create_novel(self, title, author, isbn):
    return Fiction(title, author, isbn)

  def create_non_fiction(self, title, subject,level, isbn):
    return Non_Fiction(title, subject, level, isbn)

  def add_book_to_user(self, book, email, rating = None):
    for user in self.user:
      if email not in self.email:
        return "No user with email {email}".format(email = email)
      else:
        user.read_book(book, rating)
        user.add_rating(book, rating)
        if book not in self.books:
          self.books[book] = 1
        else:
          self.books[book] += 1

    def add_user(self, name, email, user_books = None):
      if user_books:
        for book in user_books:
          self.add_book_to_user(name, email)
      return User(name, email)

    def print_catalog(self):
      for book in self.books:
        print(book)

    def print_users(self):
      for user in self.users:
        print(user)

    def most_read_book(self):
      most_read = 0
      for value in self.books.values():
        if value > most_read:
          return most_read

    def highest_rated_book(self):
      highest_rated = 0
      for book in self.books:
        rating = book.get_average_rating()
        if rating > highest_rated:
          highest_rated = rating
          return highest_rated

    def most_positive_user(self):
      high_rated = 0
      for user in self.users:
        rating = user.get_average_rating()
        if rating > high_rated:
          high_rated = rating
          return high_rated 
