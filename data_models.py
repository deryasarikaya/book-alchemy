from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """Represents an author in the library database."""

    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String)
    date_of_death = db.Column(db.String)
    books = db.relationship('Book', back_populates='author')

    def __repr__(self):
        """Return a detailed string representation of the Author instance."""
        return f"Author(id={self.id}, name={self.name})"

    def __str__(self):
        """Return a string representation of the Author instance."""
        return f"{self.name} (born: {self.birth_date})"


class Book(db.Model):
    """Represents a book in the library database."""

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = db.relationship('Author', back_populates='books')

    def __repr__(self):
        """Return a detailed string representation of the Book instance."""
        return f"Book(id={self.id}, title={self.title})"

    def __str__(self):
        """Return a string representation of the Book instance."""
        return f"{self.title} (ISBN: {self.isbn})"