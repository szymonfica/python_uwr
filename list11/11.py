# Szymon Fica 337307
# Lista 11 Zadanie 1

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker, relationship, validates, declarative_base
from datetime import datetime
import argparse

engine = create_engine('sqlite:///mydb.db')#, echo=True)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    #id = Column("id", Integer, primary_key=True)
    title = Column("title", String, primary_key=True)
    author = Column("author", String)
    year = Column("year", DateTime)
    e = relationship('Event', backref='book')

    @validates('author')
    def validate_book_author(self, key, author):
        if len(author) < 2:
            raise ValueError("Incorrect author")
        return author
    
    def __repr__(self):
        return f"book: {self.title} {self.author} {self.year}"
    

class Friend(Base):
    __tablename__ = 'friends'

    email = Column("email", String, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    e = relationship('Event', backref='friend')

    @validates('email')
    def validate_friend_email(self, key, email):
        if len(email) < 5 or '@' not in email or '.' not in email:
            raise ValueError("Incorrect email address")
        return email
    
    def __repr__(self):
        return f"friend: {self.firstname} {self.lastname} {self.email}"

class Event(Base):
    __tablename__ = 'events'

    id = Column("id", Integer, primary_key=True)
    book_title = Column(String, ForeignKey('books.title'))
    friend_email = Column(String, ForeignKey('friends.email'))
    borrow_date = Column(DateTime)
    return_date = Column(DateTime)

    @validates('book_title')
    def validate_availability(self, key, value):
        result = session.query(Event).filter(
            Event.id != self.id
            and Event.book_title == self.book_title).first()
        if result != None:
            raise ValueError("Book is unavailable")
        return value
    
    def __repr__(self):
        return f"borrowed: {self.id} {self.book_title} {self.friend_email} {self.borrow_date} {self.return_date}"
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

add_book_parser = subparser.add_parser("add_book", help="Add a new book")
add_book_parser.add_argument("title", help="Title of the new book")
add_book_parser.add_argument("--name", required=False, nargs='+', help="Author's name", default=["Unknown"])
add_book_parser.add_argument("-d", required=False, nargs=1, help="Date of publication (format: yyyy-mm-dd)", default=["0001-01-01"])

add_friend_parser = subparser.add_parser("add_friend", help="Add a new friend")
add_friend_parser.add_argument("email", help="email address")
add_friend_parser.add_argument("--firstname", required=False, nargs='?', default='', help="Friend's firstname")
add_friend_parser.add_argument("--lastname", required=False, nargs='?', default='', help="Friend's lasttname")

add_borrowing_parser = subparser.add_parser("borrow", help="Borrow a book")
add_borrowing_parser.add_argument("title", help="Title of borrowed book")
add_borrowing_parser.add_argument("-f", help="Email of a friend who's borrowing a book")
add_borrowing_parser.add_argument("-d", required=False, nargs=1, help="Date (format: yyyy-mm-dd)", default=["0001-01-01"])

add_returning_parser = subparser.add_parser("return", help="Return a book")
add_returning_parser.add_argument("title", help="Title of borrowed book")
add_returning_parser.add_argument("-d", nargs=1, help="Date (format: yyyy-mm-dd)", default=["0001-01-01"])

book_list_parser = subparser.add_parser("book_list", help="Returns a list of book")
book_list_parser.add_argument("-a", required=False, nargs='+', default='', help="Search books written by _")

borrowed_list_parser = subparser.add_parser("borrowed_list", help="Returns a list of borrowed books")
borrowed_list_parser.add_argument("-f", required=False, nargs=1, default='', help="Search books borrowed by _ (email)")

args = parser.parse_args()

if args.command == "add_book":    
    authors_name = " ".join(args.name)
    publication_date = None
    if(args.d != ["0001-01-01"]):
        publication_date = datetime(int(args.d[0][0:4]), int(args.d[0][5:7]), int(args.d[0][8:10]))
    new_book = Book(title=args.title, author=authors_name, year=publication_date)
    session.add(new_book)
    session.commit()
elif args.command == "add_friend":
    new_friend = Friend(email=args.email, firstname=args.firstname, lastname=args.lastname)
    session.add(new_friend)
    session.commit()
elif args.command == "borrow": 
    gidx = 1
    r = session.query(Event).filter().all()
    if r:
        gidx = r[-1].id + 1
    new_date = datetime.today()
    if(args.d != ["0001-01-01"]):
        new_date = datetime(int(args.d[0][0:4]), int(args.d[0][5:7]), int(args.d[0][8:10]))
    new_event = Event(id=gidx, book_title=args.title, friend_email=args.f, borrow_date=new_date)
    session.add(new_event)
    session.commit()
elif args.command == "return":
    r = session.query(Event).filter(Event.book_title == args.title).first()
    new_date = datetime.today()
    if(args.d != ["0001-01-01"]):
        new_date = datetime(int(args.d[0][0:4]), int(args.d[0][5:7]), int(args.d[0][8:10]))
    r.return_date = new_date
    session.commit()
elif args.command == "book_list":
    result = []
    if args.a != '':
        authors_name = " ".join(args.a)
        result = session.query(Book).filter(Book.author == authors_name).all()
    else:
        result = session.query(Book).filter().all()
    print(result)
elif args.command == "borrowed_list":
    result = []
    if args.f != '':
        friends_email = args.f[0]
        result = session.query(Event).filter(Event.friend_email == friends_email).all()
    else:
        result = session.query(Event).filter().all()
    print(result)

#python3 11.py add_book TheGodfather --name Mario Puzo -d 1969-03-10
#python3 11.py add_book TheSicilian --name Mario Puzo -d 1984-11-01
#python3 11.py add_book TheNotebook -d 2004-01-01
#python3 11.py add_book Book1 --name Author1
#python3 11.py add_book Book2
    
#python3 11.py add_friend friend1@gmail.com
#python3 11.py add_friend friend2@gmail.com --firstname Andie
#python3 11.py add_friend friend3@gmail.com --firstname Ben --lastname Barry
    
#python3 11.py borrow TheGodfather -f friend2@gmail.com
#python3 11.py borrow Book2 -f friend2@gmail.com
#python3 11.py book_list -a Mario Puzo
#python3 11.py book_list
    
#python3 11.py return TheGodfather 2000-06-07

#python3 11.py book_list
#python3 11.py borrowed_list

#posts = session.query(Event).all()

#for post in posts:
#    print(post)




