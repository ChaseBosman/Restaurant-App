from tkinter import *


class MembershipWindow(Toplevel):
    def __init__(self, master):
        self.top = Toplevel.__init__(self, master)
        self.geometry("450x300")
        self.title("Member Screen")


        # populate buttons
        #self.populate_category_buttons()
        #self.populate_non_category_widgets()