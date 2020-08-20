from tkinter import *
from food_db_operations import FoodDbOperations
from items_window import ItemsWindow


class CategoryWindow(Toplevel):
    def __init__(self, master):
        self.top = Toplevel.__init__(self, master)
        self.geometry("450x300")

        self.selected_food_items = []
        self.selected_drink_items = []
        self.selected_items_total = 0

        # populate buttons
        self.populate_category_buttons()
        self.populate_non_category_widgets()

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
                self.category_buttons.append(Button(self, text=row[0], command=lambda category=row[0]:
                    self.open_drink_items_menu(category), padx=5, pady=5))
                self.category_buttons[self.category_count_drinks].grid(sticky=N+S+E+W,
                                                                       row=self.category_count_drinks, column=0)
                self.category_count_drinks += 1

            # add food type buttons
            cur.execute("select type_name from food_type")
            food = cur.fetchall()
            for row in food:
                self.category_buttons.append(Button(self, text=row[0], command=lambda category=row[0]:
                    self.open_food_items_menu(category), padx=5, pady=5))

                # add self.category_count_drinks to category_buttons index to account for button count in list
                self.category_buttons[self.category_count_food+self.category_count_drinks].\
                    grid(sticky=N+S+E+W, row=self.category_count_food, column=1)
                self.category_count_food += 1

    def populate_non_category_widgets(self):
        # Listbox which displays selected items
        self.selected_items_listbox = Listbox(self, width=25,)
        self.selected_items_listbox.grid(row=0, column=2,
                                        rowspan=max(self.category_count_food, self.category_count_drinks))
        self.selected_items_listbox.configure(justify=RIGHT)

        # Label displaying the "Total:" text
        self.total_display_label = Label(self, text="Total:", padx=10, pady=10)
        self.total_display_label.grid(row=max(self.category_count_food, self.category_count_drinks) + 1, column=1)

        # StringVar for use with the total_label which displays the actual sum of costs of items
        self.total_sum = StringVar()
        self.total_sum.set("$0.00")
        self.total_label = Label(self, textvariable=self.total_sum, padx=10, pady=10)
        self.total_label.grid(row=max(self.category_count_food, self.category_count_drinks) + 1, column=2, sticky=E)

        # Commit button to send in items, configured in table_ticket for the TableTicket class to take care of
        self.commit_items_button = Button(self, text="Commit Items")
        self.commit_items_button.grid(row=max(self.category_count_food, self.category_count_drinks) + 2, column=1)

    def open_food_items_menu(self, category):
        self.item_window = ItemsWindow(self.top, category, True)
        for item in range(0, self.item_window.item_count):
            self.item_window.item_buttons[item].config(command=lambda
                selected_item=self.item_window.item_buttons[item]['text']: self.add_food(selected_item))

    def open_drink_items_menu(self, category):
        self.item_window = ItemsWindow(self.top, category, False)
        for item in range(0, self.item_window.item_count):
            self.item_window.item_buttons[item].config(command=lambda
                selected_item=self.item_window.item_buttons[item]['text']: self.add_drink(selected_item))

    # this method is ran through open_drink_items_menu
    def add_drink(self, item):
        self.selected_drink_items.append(item)
        with FoodDbOperations() as cur:
            cur.execute("select drink_cost from drink_item where drink_name = ?", (item,))
            self.item_cost = cur.fetchone()
            self.selected_items_listbox.insert(END, item + "    " + str(self.item_cost[0]))
            self.item_window.selected_items_listbox.insert(END, item + "    " + str(self.item_cost[0]))
            self.selected_items_total += self.item_cost[0]
            self.total_sum.set("$" + str(float(self.selected_items_total)))

    # this method is ran through open_food_items_menu
    def add_food(self, item):
        self.selected_food_items.append(item)
        with FoodDbOperations() as cur:
            cur.execute("select food_cost from food_item where food_name = ?", (item,))
            self.item_cost = cur.fetchone()
            self.selected_items_listbox.insert(END, item + "    " + str(self.item_cost[0]))
            self.item_window.selected_items_listbox.insert(END, item + "    " + str(self.item_cost[0]))
            self.selected_items_total += self.item_cost[0]
            self.total_sum.set("$"+str(float(self.selected_items_total)))

