from category_window import CategoryWindow
import pickle


class TableTicket:
    def __init__(self, check_number, table_num, sock, guests_num=1):
        self.check_num = check_number
        self.table_num = table_num
        self.guests = guests_num
        self.food_committed = []
        self.drinks_committed = []
        self.sock = sock

    def get_table(self):
        return self.table_num

    def display_families(self, master):
        self.category_window = CategoryWindow(master)
        self.category_window.commit_items_button.config(command=lambda: self.commit_changes())
        self.repopulate_committed()

    def commit_changes(self):
        # Add food to personal commit list
        self.food_committed.extend(self.category_window.selected_food_items)
        self.drinks_committed.extend(self.category_window.selected_drink_items)

        # Send data to chefs
        self.send_data(self.category_window.selected_food_items)
        # Right now only configured to test on single server,however bar operates on same server setup as chefs
        # self.send_data(self.category_window.selected_food_items)

        # Changes committed, destroy window
        self.category_window.destroy()

    def send_data(self, data):
        self.sock.sendall(pickle.dumps(data))

    def repopulate_committed(self):
        for item in self.food_committed:
            self.category_window.repopulate_food(item)

        for item in self.drinks_committed:
            self.category_window.repopulate_drinks(item)

