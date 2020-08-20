from category_window import CategoryWindow


class TableTicket:
    def __init__(self, check_number, table_num, guests_num=1):
        self.check_num = check_number
        self.table_num = table_num
        self.guests = guests_num
        self.food_committed = []
        self.drinks_committed = []

    def get_table(self):
        return self.table_num

    def display_families(self, master):
        self.category_window = CategoryWindow(master)
        self.category_window.commit_items_button.config(command=lambda: self.commit_changes())

    def commit_changes(self):
        self.food_committed = self.category_window.selected_food_items
        self.drinks_committed = self.category_window.selected_drink_items


