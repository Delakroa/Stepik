import sqlite3

with sqlite3.connect("E:\\python_library\\Stepik\\SQL\\users.db") as con:
    cur = con.cursor()

data = [("Мастер и Маргарита", "Булгаков М.А.", 670.99, 3),
        ("Белая гвардия", "Булгаков М.А.", 540.50, 5),
        ("Идиот", "Достоевский Ф.М.", 460.00, 10),
        ("Братья Карамазовы", "Достоевский Ф.М.", 799.01, 2),
        ("Игрок", "Достоевский Ф.М.", 480.50, 10),
        ("Стихотворения и поэмы", "Есенин С.А.", 650.00, 15),
        ("", "Иванов С. С.", 50.00, 10),
        ("Дети полуночи", "Рушди Салман", 950.00, 5),
        ("Лирика", "Гумилев Н. С.", 460.00, 10),
        ("Поэмы", "Бехтерев С. С.", 460.00, 10),
        ("Капитанская дочка", "Пушкин А. С.", 520.50, 7),
        ]

def create_table():
    """IF NOT EXISTS - если таблица существует, то
    ошибки при создании такой же таблицы не будет."""
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                book_id INTEGER PRIMARY KEY,
                title VARCHAR(50),
                author VARCHAR(30),
                price DECIMAL(8, 2),
                amount INTEGER
                )""")


def add_values():
    """IF NOT EXISTS удалять если существует база данных"""
    cur.executemany("INSERT INTO users VALUES(null, ?, ?, ?, ?)", data) # null пропускаем PRIMARY KEY иначе ошибка
    con.commit()  # Фиксация БД


def delete_table():
    cur.execute("DROP TABLE users")


if __name__ == '__main__':
    create_table()
    add_values()
    # delete_table()
    # res = cur.execute("SELECT users FROM sqlite_master")
    # res.fetchone()