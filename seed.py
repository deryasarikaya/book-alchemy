from app import app
from data_models import db, Author, Book

with app.app_context():
    authors = [
        Author(name="George Orwell", birth_date="1903-06-25", date_of_death="1950-01-21"),
        Author(name="J.K. Rowling", birth_date="1965-07-31"),
        Author(name="Ernest Hemingway", birth_date="1899-07-21", date_of_death="1961-07-02"),
        Author(name="Yuval Noah Harari", birth_date="1976-02-24"),
        Author(name="Franz Kafka", birth_date="1883-07-03", date_of_death="1924-06-03"),
    ]
    db.session.add_all(authors)
    db.session.commit()

    books = [
        Book(isbn="9780451524935", title="1984", publication_year=1949, author_id=authors[0].id),
        Book(isbn="9780747532743", title="Harry Potter and the Philosopher's Stone", publication_year=1997, author_id=authors[1].id),
        Book(isbn="9780684801223", title="The Old Man and the Sea", publication_year=1952, author_id=authors[2].id),
        Book(isbn="9780062316097", title="Sapiens", publication_year=2011, author_id=authors[3].id),
        Book(isbn="9780805209990", title="The Trial", publication_year=1925, author_id=authors[4].id),
        Book(isbn="9780451526342", title="Animal Farm", publication_year=1945, author_id=authors[0].id),
        Book(isbn="9780439064873", title="Harry Potter and the Chamber of Secrets", publication_year=1998, author_id=authors[1].id),
        Book(isbn="9780684801469", title="A Farewell to Arms", publication_year=1929, author_id=authors[2].id),
        Book(isbn="9780771038518", title="Homo Deus", publication_year=2015, author_id=authors[3].id),
        Book(isbn="9780805210583", title="The Metamorphosis", publication_year=1915, author_id=authors[4].id),
    ]
    db.session.add_all(books)
    db.session.commit()
    print("Done!")
