from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

if __name__ == "__main__":
    main()
    try:

        create_tables()


        author1 = Author(name="JESSE LANGAT")
        print(f"Author ID: {author1.id}, Name: {author1.name}")


        magazine1 = Magazine(name="CREME DE LA CITY", category="Trending")
        print(f"Magazine ID: {magazine1.id}, Name: {magazine1.name}, Category: {magazine1.category}")


        article1 = Article(author=author1, magazine=magazine1, title="Feud brewing between the east and west", content="content about beef in nairobi city  ")
        print(f"Article ID: {article1.id}, Title: {article1.title}, Author: {article1.author.name}, Magazine: {article1.magazine.name}")
        print("Author's Articles:", author1.articles())
        print("Author's Magazines:", author1.magazines())
        print("Magazine's Articles:", magazine1.articles())
        print("Magazine's Contributors:", magazine1.contributors())
        print("Magazine's Article Titles:", magazine1.article_titles())
        print("Magazine's Contributing Authors:", magazine1.contributing_authors())

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "_main_":
    main()