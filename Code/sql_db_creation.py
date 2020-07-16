import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute("""CREATE TABLE ticket (
        ticket_id int NOT NULL,
        curr_date date NOT NULL,
        tip money NOT NULL,
            PRIMARY KEY (ticket_id, curr_date)
        )""")

curs.execute("""CREATE TABLE food_item_ordered (
        food_order_id PRIMARY KEY,
        ticket_id int NOT NULL,
        curr_date date NOT NULL,
        food_item_id int NOT NULL,
            FOREIGN KEY (food_item_id) REFERENCES food_item(food_item_id),
            FOREIGN KEY (ticket_id, curr_date) REFERENCES ticket(ticket_id, curr_date)
        )""")

curs.execute("""CREATE TABLE drink_item_ordered (
        drink_order_id PRIMARY KEY,
        ticket_id int NOT NULL,
        curr_date date NOT NULL,
        drink_item_id int NOT NULL,
            FOREIGN KEY (ticket_id, curr_date) REFERENCES ticket(ticket_id, curr_date),
            FOREIGN KEY (drink_item_id) REFERENCES drink_item(drink_item_id)
        )""")

curs.execute("""CREATE TABLE food_type (
        food_type_id PRIMARY KEY,
        type_name varchar(25) NOT NULL
        )""")

curs.execute("""CREATE TABLE food_item (
        food_item_id PRIMARY KEY,
        food_name varchar(25) NOT NULL,
        food_cost money NOT NULL,
        food_type_id int NOT NULL,
            FOREIGN KEY (food_type_id) REFERENCES food_type(food_type_id)
        )""")

curs.execute("""CREATE TABLE drink_type (
        drink_type_id PRIMARY KEY,
        type_name varchar(25) NOT NULL
        )""")

curs.execute("""CREATE TABLE drink_item (
        drink_item_id PRIMARY KEY,
        drink_name varchar(25) NOT NULL,
        drink_cost money NOT NULL,
        drink_type_id int NOT NULL,
            FOREIGN KEY (drink_type_id) REFERENCES drink_type(drink_type_id)
        )""")

conn.commit()
conn.close()



