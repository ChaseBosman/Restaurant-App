from category_window import CategoryWindow


class TableTicket:
    def __init__(self, check_number, table_num, guests_num=1):
        self.check_num = check_number
        self.table_num = table_num
        self.guests = guests_num

    def get_table(self):
        return self.table_num

    def display_families(self, master):
        CategoryWindow(master)
