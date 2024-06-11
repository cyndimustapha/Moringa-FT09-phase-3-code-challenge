from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:

    def __init__(self, title, content, author, magazine, id = None):  # Corrected __init_ method
        self._title = title
        self._content = content
        self._author = author
        self._magazine = magazine
        self._id = id
        if id is None:
            self._create_in_db()

    def _create_in_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self._title, self._content, self._author.id, self._magazine.id))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
    
    def __repr__(self):
        return f'<Article {self.title}>'