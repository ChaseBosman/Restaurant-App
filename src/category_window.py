from tkinter import *
from food_db_operations import FoodDbOperations


class CategoryWindow(Toplevel):
    def __init__(self, master):
        self.top = Toplevel.__init__(self, master)
        self.geometry("350x200")
        self.populate_category_buttons()

    def populate_category_buttons(self):
        # This is a list and count of buttons containing food and drink categories
        self.category_buttons = []
        self.category_count_drinks = 0
        self.category_count_food = 0

        # Open food database through context manager
        with FoodDbOperations() as cur:
            # add drink type buttons
            cur.execute("select type_name from drink_type")
            drinks = cur.fetchall()
            for row in drinks:
                print(row[0])
                self.category_buttons.append(Button(self, text=row[0], padx=5, pady=5))
                self.category_buttons[self.category_count_drinks].grid(sticky=N+S+E+W,
                                                                       row=self.category_count_drinks, column=0)
                self.category_count_drinks += 1

            # add food type buttons
            cur.execute("select type_name from food_type")
            food = cur.fetchall()
            for row in food:
                print(row[0])
                self.category_buttons.append(Button(self, text=row[0], padx=5, pady=5))
                # add self.category_count_drinks to category_buttons index to account for button count in list
                self.category_buttons[self.category_count_food+self.category_count_drinks].\
                    grid(sticky=N+S+E+W, row=self.category_count_food, column=25)
                self.category_count_food += 1
