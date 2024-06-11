import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.setup import create_tables
from database.connection import get_db_connection

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_tables()

    def setUp(self):
        # Clean up the database before each test
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles')
        cursor.execute('DELETE FROM authors')
        cursor.execute('DELETE FROM magazines')
        conn.commit()
        conn.close()

    def test_author_creation(self):
        author = Author("CYNDI MUSTAPHA")
        self.assertEqual(author.name, "CYNDI MUSTAPHA")
        self.assertIsNotNone(author.id)

    def test_magazine_creation(self):
        magazine = Magazine("MODERN MUSE", "Trending")
        self.assertEqual(magazine.name, "MODERN MUSE")
        self.assertEqual(magazine.category, "Trending")
        self.assertIsNotNone(magazine.id)

    def test_article_creation(self):
        author = Author("CYNDI MUSTAPHA")
        magazine = Magazine("MODERN MUSE", "Trending")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author.id, author.id)
        self.assertEqual(article.magazine.id, magazine.id)
        self.assertIsNotNone(article.id)

    def test_author_articles(self):
        author = Author("CYNDI MUSTAPHA")
        magazine = Magazine("MODERN MUSE", "Trending")
        article1 = Article("Title 1", "Content 1", author, magazine)
        article2 = Article("Title 2", "Content 2", author, magazine)
        articles = author.articles()
        self.assertEqual(len(articles), 2)
        self.assertIn(article1.id, [a['id'] for a in articles])
        self.assertIn(article2.id, [a['id'] for a in articles])

    def test_author_magazines(self):
        author = Author("CYNDI MUSTAPHA")
        magazine1 = Magazine("MODERN MUSE", "Trending")
        magazine2 = Magazine("VOGUE", "Fashion")
        Article("Title 1", "Content 1", author, magazine1)
        Article("Title 2", "Content 2", author, magazine2)
        magazines = author.magazines()
        self.assertEqual(len(magazines), 2)
        self.assertIn(magazine1.id, [m['id'] for m in magazines])
        self.assertIn(magazine2.id, [m['id'] for m in magazines])

    def test_magazine_articles(self):
        author = Author("CYNDI MUSTAPHA")
        magazine = Magazine("MODERN MUSE", "Trending")
        article1 = Article("Title 1", "Content 1", author, magazine)
        article2 = Article("Title 2", "Content 2", author, magazine)
        articles = magazine.articles()
        self.assertEqual(len(articles), 2)
        self.assertIn(article1.id, [a['id'] for a in articles])
        self.assertIn(article2.id, [a['id'] for a in articles])

    def test_magazine_contributors(self):
        author1 = Author("CYNDI MUSTAPHA")
        author2 = Author("ANYONE")
        magazine = Magazine("MODERN MUSE", "Trending")
        Article("Title 1", "Content 1", author1, magazine)
        Article("Title 2", "Content 2", author2, magazine)
        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 2)
        self.assertIn(author1.id, [c['id'] for c in contributors])
        self.assertIn(author2.id, [c['id'] for c in contributors])

    def test_magazine_article_titles(self):
        author = Author("CYNDI MUSTAPHA")
        magazine = Magazine("MODERN MUSE", "Trending")
        Article("Title 1", "Content 1", author, magazine)
        Article("Title 2", "Content 2", author, magazine)
        titles = magazine.article_titles()
        self.assertEqual(len(titles), 2)
        self.assertIn("Title 1", titles)
        self.assertIn("Title 2", titles)

    def test_magazine_contributing_authors(self):
        author1 = Author("CYNDI MUSTAPHA")
        author2 = Author("ANYONE")
        magazine = Magazine("MODERN MUSE", "Trending")
        Article("Title 1", "Content 1", author1, magazine)
        Article("Title 2", "Content 2", author1, magazine)
        Article("Title 3", "Content 3", author1, magazine)
        Article("Title 4", "Content 4", author2, magazine)
        contributing_authors = magazine.contributing_authors()
        self.assertEqual(len(contributing_authors), 1)
        self.assertEqual(contributing_authors[0]['id'], author1.id)

if __name__ == "__main__":
    unittest.main()
