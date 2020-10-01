from client.table_select_window import TableSelectWindow
from tkinter import Tk

root_window = Tk()
curr_menu = TableSelectWindow(master=root_window)
root_window.mainloop()
