import sqlite3


bd = sqlite3.connect("library.db")
cursor = bd.cursor()
tables = [
    """
        CREATE TABLE IF NOT EXISTS book(
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            price REAL NOT NULL,
            name TEXT NOT NULL
        );
    """
]
for table in tables:
    cursor.execute(table)

sentences = [
        """
        INSERT INTO book (author, genre, price, name)
        VALUES
        ('Stephen King', 'Terror', 115,'Cementerio de animales'),
        ('Alfred Bester', 'Ciencia ficción', 200,'Las estrellas, mi destino'),
        ('Margaret Atwood', 'Ciencia ficción', 150,'El cuento de la criada');
        """
]
for sentence in sentences:
    cursor.execute(sentence);

bd.commit()
bd.close()

