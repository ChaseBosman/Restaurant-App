from category_window import CategoryWindow
from committed_waiter_socket import CommittedWaiterSocket


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
        self.repopulate_committed()

    def commit_changes(self):
        self.food_committed.extend(self.category_window.selected_food_items)
        self.drinks_committed.extend(self.category_window.selected_drink_items)
        comm_socket_food = CommittedWaiterSocket(self.category_window.selected_food_items, 8080)
        # comm_socket_drinks = CommittedWaiterSocket(self.category_window.selected_drink_items, 8081)
        # comm_socket.
        self.category_window.destroy()

    def repopulate_committed(self):
        for item in self.food_committed:
            self.category_window.repopulate_food(item)

        for item in self.drinks_committed:
            self.category_window.repopulate_drinks(item)

