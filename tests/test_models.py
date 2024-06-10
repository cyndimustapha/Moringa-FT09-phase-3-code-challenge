import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.setup import create_tables

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_tables()

    def test_author_creation(self):
        #author = Author(1, "JESSE LANGAT")
        author = Author("JESSE LANGAT")
        self.assertEqual(author.name, "JESSE LANGAT")
        self.assertIsNotNone(author.id)

    def test_article_creation(self):
        #article = Article(1, "Test Title", "Test Content", 1, 1)
        author = Author("JESSE LANGAT")
        magazine = Magazine("CREME DE LA CITY", "Trending")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author.id, author.id)
        self.assertEqual(article.magazine.id, magazine.id)
        self.assertIsNotNone(article.id)


    def test_magazine_creation(self):
        magazine = Magazine(1, "CREME DE LA CITY")
        magazine = Magazine("CREME DE LA CITY", "Trending")
        self.assertEqual(magazine.name, "CREME DE LA CITY")
        self.assertEqual(magazine.category, "Trending")
        self.assertIsNotNone(magazine.id)

if __name__ == "__main__":
    unittest.main()