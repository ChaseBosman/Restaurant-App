import threading
from tkinter import *
from committed_line_socket import CommittedLineSocket
from table_queue_structure import TableQueueStructure


class InProgressWindow:
    def __init__(self, master=None):
        self.master = master
        self.master.geometry("300x300")
        self.master.title("To-Do")

        self.create_widgets()

        self.active_socket = CommittedLineSocket()
        threading.Thread(target=self.active_socket.accept).start()

        self.table_queue = []

        self.add_order()

    def create_widgets(self):
        # Listbox which displays in progress items
        self.progress_listbox = Listbox(self.master, width=25, height=15)
        self.progress_listbox.grid(row=0, column=0, rowspan=1)
        self.progress_listbox.configure(justify=RIGHT)

        self.finished_items_button = Button(self.master, text="Finished", command=lambda: self.item_finished())
        self.finished_items_button.grid(row=1, column=0)

    def add_order(self):
        while len(self.active_socket.to_add) > 0:
            # retrieve first queued order retrieved from the socket
            new_order = self.active_socket.to_add.pop(0)
            # retrieve table and order numbers from the new order
            table_num = new_order.pop(0)
            order_num = new_order.pop(0)
            print(table_num, order_num)

            # add items to the screen
            for item in new_order:
                self.progress_listbox.insert(END, str(table_num) + '-' + str(order_num) + ', ' + str(item))

            # add items to the order queue structure, assume it is a new table until table found in table_queue
            new_table = True
            for table in self.table_queue:
                if table.get_table_num() == table_num:
                    # table has been found as already existing
                    table.add_order(order_num, new_order)
                    new_table = False

            # table was not found, create new table
            if new_table:
                self.create_new_table(table_num, order_num, new_order)

        self.master.after(3000, self.add_order)

    def create_new_table(self, table_num, order_num, new_order):
        new_table = TableQueueStructure(table_num, order_num, new_order)
        self.table_queue.insert(len(self.table_queue), new_table)

    def item_finished(self):
        item_selected = self.progress_listbox.curselection()
        # remove table from string, save order_num and item as order
        table, order = self.progress_listbox.get(item_selected[0]).split("-")
        # remove specific tables nth order and save food item
        table_order, food_item = order.split(", ")
        # pass into table struct and remove
        print(table, table_order, food_item)
        self.progress_listbox.delete(item_selected[0])


if __name__ == "__main__":
    root_window = Tk()
    curr_menu = InProgressWindow(master=root_window)
    root_window.mainloop()



