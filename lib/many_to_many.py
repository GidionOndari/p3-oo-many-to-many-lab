class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def contracts(self):
        """Return all Contract instances for this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all Books this author has contracts for"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return sum of all royalties from contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        """Return all Contract instances related to this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all Author instances related to this book through contracts"""
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    # author 
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("author must be an instance of Author")

    # book 
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception("book must be an instance of Book")

    # date
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("date must be a string")

    # royalties 
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception("royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts matching given date"""
        return [contract for contract in cls.all if contract.date == date]
