# 📚 Book Alchemy – Digital Library

A Flask web application to manage your personal book collection.

## Features

- Add and delete authors and books
- View book covers via Open Library API
- Search books by title
- Sort books by title or author name

## Tech Stack

- Python / Flask
- SQLAlchemy / Flask-SQLAlchemy
- SQLite
- Jinja2

## Setup

1. Clone the repository:
```bash
git clone https://github.com/deryasarikaya/book-alchemy.git
cd book-alchemy
```

2. Install dependencies:
```bash
pip install flask sqlalchemy flask-sqlalchemy jinja2
```

3. Create the database:
```bash
python -c "from app import app, db; 
with app.app_context(): db.create_all()"
```

4. (Optional) Add sample data:
```bash
python seed.py
```

5. Run the app:
```bash
flask run
```

## Usage

- `/` – Home page with all books
- `/add_author` – Add a new author
- `/add_book` – Add a new book
- `/book/<id>/delete` – Delete a book