import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()

'''
curs.execute("INSERT INTO food_type VALUES (1, 'Entrees')")
curs.execute("INSERT INTO food_type VALUES (2, 'Apps')")
curs.execute("INSERT INTO food_type VALUES (3, 'Sandwiches')")
curs.execute("INSERT INTO food_type VALUES (4, 'Baked')")

curs.execute("INSERT INTO drink_type VALUES (1, 'Fountain')")
curs.execute("INSERT INTO drink_type VALUES (2, 'Non Alc Mixed')")
curs.execute("INSERT INTO drink_type VALUES (3, 'Beer')")
curs.execute("INSERT INTO drink_type VALUES (4, 'Alc Mixed')")

curs.execute("INSERT INTO food_item VALUES (0, 'Wings', 15, 2)")
curs.execute("INSERT INTO food_item VALUES (1, 'Potato Skins', 16, 2)")
curs.execute("INSERT INTO food_item VALUES (2, 'Parm Chkn Scampi', 21, 1)")
curs.execute("INSERT INTO food_item VALUES (3, 'Chicken Zoodles', 19, 1)")
curs.execute("INSERT INTO food_item VALUES (4, 'Basic Burg', 15, 3)")
curs.execute("INSERT INTO food_item VALUES (5, 'Chicken Sandwich', 14, 3)")
curs.execute("INSERT INTO food_item VALUES (6, 'Pizza', 20, 4)")
curs.execute("INSERT INTO food_item VALUES (7, 'Chicken Pot Pie', 19, 4)")
curs.execute("INSERT INTO food_item VALUES (8, 'Ziti', 16, 4)")

curs.execute("INSERT INTO drink_item VALUES (0, 'Pepsi', 2.10, 1)")
curs.execute("INSERT INTO drink_item VALUES (1, 'Sprite', 2.10, 1)")
curs.execute("INSERT INTO drink_item VALUES (2, 'Shirley Temple', 3, 2)")
curs.execute("INSERT INTO drink_item VALUES (3, 'Roy Rodgers', 3, 2)")
curs.execute("INSERT INTO drink_item VALUES (4, 'Coors', 7, 3)")
curs.execute("INSERT INTO drink_item VALUES (5, 'Pacifico', 8, 3)")
curs.execute("INSERT INTO drink_item VALUES (6, 'Jack and Coke', 10, 4)")
curs.execute("INSERT INTO drink_item VALUES (7, 'Moscow Mule', 9, 4)")
'''

curs.execute('select * from drink_type')
rows = curs.fetchall()
#for row in rows:
 #   print(row)

print(rows)


conn.commit()
conn.close()
