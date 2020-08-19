from tkinter import *
from food_db_operations import FoodDbOperations


class ItemsWindow(Toplevel):
    def __init__(self, master, category, is_food):
        self.top = Toplevel.__init__(self, master)
        self.geometry("350x200")
        # describes the food's category (baked, alc mixed)
        self.category = category
        # boolean, describes if menu is for food or a drink
        self.is_food = is_food
        self.populate_item_buttons()

    def populate_item_buttons(self):
        # This is a list and count of buttons containing food and drink categories
        self.item_buttons = []
        self.item_count = 0

        # Open food database through context manager
        if self.is_food:
            with FoodDbOperations() as cur:
                # add item buttons relating to category
                cur.execute("select food_name from food_item where food_type_id = "
                            "(select food_type_id from food_type where type_name = ?)", (self.category,))
                food = cur.fetchall()
                for row in food:
                    print(row[0])
                    self.item_buttons.append(
                        Button(self, text=row[0], padx=5, pady=5))
                    # add self.category_count_drinks to category_buttons index to account for button count in list
                    self.item_buttons[self.item_count].grid(sticky=N + S + E + W, row=self.item_count, column=25)
                    self.item_count += 1

        # chosen category is a drink, use drink_item table
        elif not self.is_food:
            with FoodDbOperations() as cur:
                # add item buttons relating to category
                cur.execute("select drink_name from drink_item where drink_type_id = "
                            "(select drink_type_id from drink_type where type_name = ?)", (self.category,))
                food = cur.fetchall()
                for row in food:
                    print(row[0])
                    self.item_buttons.append(
                        Button(self, text=row[0], padx=5, pady=5))
                    # add self.category_count_drinks to category_buttons index to account for button count in list
                    self.item_buttons[self.item_count].grid(sticky=N + S + E + W, row=self.item_count, column=25)
                    self.item_count += 1
