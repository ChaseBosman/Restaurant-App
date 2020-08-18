import sqlite3


class FoodDbOperations:
    def __init__(self, file='food.db'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


with FoodDbOperations() as cur:
    cur.execute('select type_name from drink_type')

    rows = cur.fetchall()
    for row in rows:
        print(*row)