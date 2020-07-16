import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()


curs.execute("INSERT INTO family VALUES (1, 'Entrees')")
curs.execute("INSERT INTO family VALUES (2, 'Apps')")
curs.execute("INSERT INTO family VALUES (3, 'Sandwiches')")
curs.execute("INSERT INTO family VALUES (4, 'Baked')")

curs.execute("INSERT INTO food VALUES (0, 'Wings', 15, 2)")
curs.execute("INSERT INTO food VALUES (1, 'Potato Skins', 16, 2)")
curs.execute("INSERT INTO food VALUES (2, 'Parm Chkn Scampi', 21, 1)")
curs.execute("INSERT INTO food VALUES (3, 'Chicken Zoodles', 19, 1)")
curs.execute("INSERT INTO food VALUES (4, 'Basic Burg', 15, 3)")
curs.execute("INSERT INTO food VALUES (5, 'Chicken Sandwich', 14, 3)")
curs.execute("INSERT INTO food VALUES (6, 'Pizza', 20, 4)")
curs.execute("INSERT INTO food VALUES (7, 'Chicken Pot Pie', 19, 4)")



curs.execute("SELECT food.name FROM food, family where family.food_fam\
=food.food_fam AND family.name = 'Apps'")

rows = curs.fetchall()

for row in rows:
    print(row)


conn.commit()
conn.close()