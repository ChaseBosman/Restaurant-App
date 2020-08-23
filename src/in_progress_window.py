import threading
from tkinter import *
from committed_line_socket import CommittedLineSocket


class InProgressWindow:
    def __init__(self, master=None):
        self.master = master
        self.master.geometry("300x300")
        self.create_widgets()
        self.active_socket = CommittedLineSocket()
        threading.Thread(target=self.active_socket.accept).start()
        self.add_item()

    def create_widgets(self):
        # Listbox which displays in progress items
        self.progress_listbox = Listbox(self.master, width=25, height=15)
        self.progress_listbox.grid(row=0, column=0, rowspan=1)
        self.progress_listbox.configure(justify=RIGHT)

        self.finished_items_button = Button(self.master, text="Finished")
        self.finished_items_button.grid(row=1, column=0)

    def add_item(self):
        while len(self.active_socket.to_add) > 0:
            # item = self.active_socket.to_add.pop(0)
            self.progress_listbox.insert(END, self.active_socket.to_add.pop(0))
        self.master.after(1000, self.add_item)


if __name__ == "__main__":
    root_window = Tk()
    curr_menu = InProgressWindow(master=root_window)
    root_window.mainloop()

