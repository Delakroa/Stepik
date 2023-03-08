import sqlite3

with sqlite3.connect("E:/python_library/Stepik/SQL/book.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE book") # команда для удаления таблицы.
    # IF NOT EXISTS - если таблица существует, то ошибки при создании такой же таблицы не будет.
    cur.execute("""CREATE TABLE IF NOT EXISTS book(
                book_id INT PRIMARY_KEY AUTO_INCREMENT,
                title VARCHAR(50),
                author VARCHAR(30),
                price DECIMAL(8, 2),
                amount INT
                )""")

    cur.execute("""INSERT INTO IF NOT EXISTS book(title, author, price, amount)
                VALUES('Мастер и Маргарита', 'Булгаков М. А.', 670.99, 3);
                """)