from tkinter import *
from membership_window import MembershipWindow


class PhoneNumberWindow(Toplevel):
    def __init__(self, master):
        self.top = Toplevel.__init__(self, master)
        self.geometry("240x200")
        self.title("Enter a number!")

        # populate buttons
        self.create_buttons()

    def del_text(self):
        self.phone_entry.delete(len(self.phone_entry.get()) - 1, END)

    # method to read phone num when enter_but is pressed
    def enter_text(self):
        MembershipWindow(self, self.phone_entry.get())
        # delete phone_entry window text
        self.phone_entry.delete(0, END)
        return

    def set_text(self, text):
        self.phone_entry.insert(len(self.phone_entry.get()), text)
        return

    def create_buttons(self):
        self.phone_label = Label(self, text="Phone #:")
        self.phone_entry = Entry(self)

        self.phone_label.grid(row=0, column=0)
        self.phone_entry.grid(row=0, column=1, columnspan=10)

        self.num0_but = Button(self, text=" 0 ", command=lambda: self.set_text("0"))
        self.num1_but = Button(self, text=" 1 ", command=lambda: self.set_text("1"))
        self.num2_but = Button(self, text=" 2 ", command=lambda: self.set_text("2"))
        self.num3_but = Button(self, text=" 3 ", command=lambda: self.set_text("3"))
        self.num4_but = Button(self, text=" 4 ", command=lambda: self.set_text("4"))
        self.num5_but = Button(self, text=" 5 ", command=lambda: self.set_text("5"))
        self.num6_but = Button(self, text=" 6 ", command=lambda: self.set_text("6"))
        self.num7_but = Button(self, text=" 7 ", command=lambda: self.set_text("7"))
        self.num8_but = Button(self, text=" 8 ", command=lambda: self.set_text("8"))
        self.num9_but = Button(self, text=" 9 ", command=lambda: self.set_text("9"))
        self.delete_but = Button(self, text="Delete", command=self.del_text)
        self.enter_but = Button(self, text="Enter", command=self.enter_text)

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