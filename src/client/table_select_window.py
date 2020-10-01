from tkinter import *
from client.table_ticket import TableTicket
from client.phone_number_window import PhoneNumberWindow
import socket


class TableSelectWindow:

    def __init__(self, master=None):
        self.master = master
        # current count of tables
        self.ticket_count = 0
        self.table_count = 0
        self.table_objects = []
        # initialize and set Tk windows
        self.master.geometry("240x200")
        self.master.title("Choose a table")
        self.create_buttons()
        self.define_socket()

    # method to delete text from entry
    def del_text(self):
        self.tbl_entry.delete(len(self.tbl_entry.get()) - 1, END)

    # method to read entry when enter_but is pressed
    def enter_text(self):
        # Check if the current entered table is in the system
        for curr_table in self.table_objects:
            if curr_table.get_table() == self.tbl_entry.get():
                # if in table list then display available category options
                curr_table.display_families(self.master)
                self.tbl_entry.delete(0, END)
                return

        # With no return, the table is considered a new table and is now being entered into the system
        self.table_objects.append(TableTicket(self.sock, self.ticket_count, self.tbl_entry.get()))
        self.table_objects[-1].display_families(self.master)
        self.ticket_count += 1
        self.table_count += 1

        # delete tbl_entry window text
        self.tbl_entry.delete(0, END)
        return

    def membership(self):
        PhoneNumberWindow(self.master)
        return

    def set_text(self, text):
        self.tbl_entry.insert(len(self.tbl_entry.get()), text)
        return

    def create_buttons(self):
        self.tbl_label = Label(self.master, text="View Table:")
        self.tbl_entry = Entry(self.master)

        self.tbl_label.grid(row=0, column=0)
        self. tbl_entry.grid(row=0, column=1, columnspan=10)

        self.num0_but = Button(self.master, text=" 0 ", command=lambda: self.set_text("0"))
        self.num1_but = Button(self.master, text=" 1 ", command=lambda: self.set_text("1"))
        self.num2_but = Button(self.master, text=" 2 ", command=lambda: self.set_text("2"))
        self.num3_but = Button(self.master, text=" 3 ", command=lambda: self.set_text("3"))
        self.num4_but = Button(self.master, text=" 4 ", command=lambda: self.set_text("4"))
        self.num5_but = Button(self.master, text=" 5 ", command=lambda: self.set_text("5"))
        self.num6_but = Button(self.master, text=" 6 ", command=lambda: self.set_text("6"))
        self.num7_but = Button(self.master, text=" 7 ", command=lambda: self.set_text("7"))
        self.num8_but = Button(self.master, text=" 8 ", command=lambda: self.set_text("8"))
        self.num9_but = Button(self.master, text=" 9 ", command=lambda: self.set_text("9"))
        self.delete_but = Button(self.master, text="Delete", command=self.del_text)
        self.enter_but = Button(self.master, text="Enter", command=self.enter_text)
        self.membership = Button(self.master, text="Member", command=self.membership)

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
        self.membership.grid(row=5, column=2)

    def define_socket(self):
        host = '127.0.0.1'
        port = 8080
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        self.sock = sock


if __name__ == "__main__":
    root_window = Tk()
    curr_menu = TableSelectWindow(master=root_window)
    root_window.mainloop()
