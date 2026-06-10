import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)


@app.route('/')
def home():
    """Display all books on the homepage, sorted by title or author name."""
    sort_by = request.args.get('sort_by', 'title')
    search = request.args.get('search', '')
    message = request.args.get('message')

    if search:
        books = Book.query.filter(Book.title.like(f'%{search}%')).all()
        if not books:
            message = f"No books found for '{search}'."
    elif sort_by == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.order_by(Book.title).all()

    return render_template('home.html', books=books, sort_by=sort_by, message=message)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """Render the add author form (GET) or save a new author to the database (POST)."""
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birth_date')
        date_of_death = request.form.get('date_of_death')
        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()
        message = f"Author '{name}' added successfully!"
    return render_template('add_author.html', message=message)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """Render the add book form (GET) or save a new book to the database (POST)."""
    message = None
    authors = Author.query.order_by(Author.name).all()
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')
        new_book = Book(isbn=isbn, title=title,
                        publication_year=publication_year,
                        author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        message = f"Book '{title}' added successfully!"
    return render_template('add_book.html', authors=authors, message=message)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    """Delete a book from the database and redirect to the homepage with a success message."""
    book = Book.query.get(book_id)
    author = book.author
    db.session.delete(book)
    db.session.commit()

    # Delete author if no more books
    if not author.books:
        db.session.delete(author)
        db.session.commit()

    return redirect(url_for('home', message=f"Book '{book.title}' deleted successfully!"))


if __name__ == '__main__':
    app.run(debug=True)