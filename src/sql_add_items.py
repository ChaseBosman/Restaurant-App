import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()


curs.execute("INSERT INTO food_types VALUES (1, 'Entrees')")
curs.execute("INSERT INTO food_types VALUES (2, 'Apps')")
curs.execute("INSERT INTO food_types VALUES (3, 'Sandwiches')")
curs.execute("INSERT INTO food_types VALUES (4, 'Baked')")

curs.execute("INSERT INTO drink_types VALUES (1, 'Fountain')")
curs.execute("INSERT INTO drink_types VALUES (2, 'Hot mixed')")
curs.execute("INSERT INTO drink_types VALUES (3, 'Non-Alcoholic')")
curs.execute("INSERT INTO drink_types VALUES (4, 'Beer')")

curs.execute("INSERT INTO food_item VALUES (0, 'Wings', 15, 2)")
curs.execute("INSERT INTO food_item VALUES (1, 'Potato Skins', 16, 2)")
curs.execute("INSERT INTO food_item VALUES (2, 'Parm Chkn Scampi', 21, 1)")
curs.execute("INSERT INTO food_item VALUES (3, 'Chicken Zoodles', 19, 1)")
curs.execute("INSERT INTO food_item VALUES (4, 'Basic Burg', 15, 3)")
curs.execute("INSERT INTO food_item VALUES (5, 'Chicken Sandwich', 14, 3)")
curs.execute("INSERT INTO food_item VALUES (6, 'Pizza', 20, 4)")
curs.execute("INSERT INTO food_item VALUES (7, 'Chicken Pot Pie', 19, 4)")



#curs.execute()

rows = curs.fetchall()

for row in rows:
    print(row)


conn.commit()
conn.close()