from tkinter import *
import table


class TableSelect:

    def __init__(self, master = None):
        # current count of tables
        self.ticket_count = 0
        self.table_count = 0
        self.table_objs = []
        # initialize and set Tk windows
        master.geometry("200x200")
        self.create_buttons()

    # method to delete text from entry
    def del_text(self):
        self.tbl_entry.delete(len(self.tbl_entry.get()) - 1, END)

    # method to read entry when enter is pressed and do proper call
    def enter_text(self):
        # Check if the current entered table is in the system
        for curr_table in self.table_objs:
            if curr_table.get_table() == self.tbl_entry.get():
                print("old table")
                #curr_table.display_families()
                return

        # At this point the table is considered a new table, and it is now being entered into the system
        print("new table")
        self.table_objs.append(table.Table(self.tbl_entry.get(), self.ticket_count))
        self.ticket_count += 1
        self.table_count += 1
        self.tbl_entry.delete(0, END)
        print(self.table_objs[self.table_count - 1].get_table())
        return

    def set_text(self, text):
        self.tbl_entry.insert(len(self.tbl_entry.get()), text)
        return

    def create_buttons(self):
        self.tbl_label = Label(root_window, text="View Table:")
        self.tbl_entry = Entry(root_window)

        self.tbl_label.grid(row=0, column=0)
        self. tbl_entry.grid(row=0, column=1, columnspan=10)

        self.num0_but = Button(root_window, text=" 0 ", command=lambda: self.set_text("0"))
        self.num1_but = Button(root_window, text=" 1 ", command=lambda: self.set_text("1"))
        self.num2_but = Button(root_window, text=" 2 ", command=lambda: self.set_text("2"))
        self.num3_but = Button(root_window, text=" 3 ", command=lambda: self.set_text("3"))
        self.num4_but = Button(root_window, text=" 4 ", command=lambda: self.set_text("4"))
        self.num5_but = Button(root_window, text=" 5 ", command=lambda: self.set_text("5"))
        self.num6_but = Button(root_window, text=" 6 ", command=lambda: self.set_text("6"))
        self.num7_but = Button(root_window, text=" 7 ", command=lambda: self.set_text("7"))
        self.num8_but = Button(root_window, text=" 8 ", command=lambda: self.set_text("8"))
        self.num9_but = Button(root_window, text=" 9 ", command=lambda: self.set_text("9"))
        self.delete_but = Button(root_window, text="Delete", command=self.del_text)
        self.enter_but = Button(root_window, text="Enter", command=self.enter_text)

        self.num1_but.grid(row=1, column=1)
        self.num2_but.grid(row=1, column=2)
        self.num3_but.grid(row=1, column=3)
        self.num4_but.grid(row=2, column=1)
        self.num5_but.grid(row=2, column=2)
        self.num6_but.grid(row=2, column=3)
        self.num7_but.grid(row=3, column=1)
        self.num8_but.grid(row=3, column=2)
        self.num9_but.grid(row=3, column=3)
        self.num0_but.grid(row=4, column=2)
        self.delete_but.grid(row=4, column=1)
        self.enter_but.grid(row=4, column=3)


if __name__ == "__main__":
    root_window = Tk()
    curr_menu = TableSelect(master=root_window)
    root_window.mainloop()
