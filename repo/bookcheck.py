import mysql.connector
from configparser import ConfigParser

class BookRepository:
    def __init__(self, config_file):
        config = ConfigParser()
        config.read(config_file)

        host = config.get('Database', 'host')
        username = config.get('Database', 'username')
        password = config.get('Database', 'password')
        database = config.get('Database', 'database')

        self.connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def book_exists(self, book_title):
        query = "SELECT COUNT(*) FROM books WHERE title = %s"
        self.cursor.execute(query, (book_title,))
        result = self.cursor.fetchone()
        count = result[0]
        return count > 0

    def add_book(self, book_title):
        query = "INSERT INTO books (title) VALUES (%s)"
        self.cursor.execute(query, (book_title,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
