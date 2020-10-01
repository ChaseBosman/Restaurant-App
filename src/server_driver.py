from server.in_progress_window import InProgressWindow
from tkinter import Tk

root_window = Tk()
curr_menu = InProgressWindow(master=root_window)
root_window.mainloop()
