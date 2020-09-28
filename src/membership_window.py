from tkinter import *
from json_handler import JsonHandler
from s3_handler import S3Handler


class MembershipWindow(Toplevel):
    def __init__(self, master, phone_number):
        self.top = Toplevel.__init__(self, master)
        self.geometry("450x300")
        self.title("Member Screen")
        self.number = phone_number

        # populate buttons
        self.create_buttons()
        # insert previously entered phone number into to entry slot
        self.phone_entry.insert(0, phone_number)

    def create_buttons(self):
        self.phone_label = Label(self, text="Phone #:")
        self.phone_entry = Entry(self)
        self.first_label = Label(self, text="First name:")
        self.first_entry = Entry(self)
        self.last_label = Label(self, text="Last name:")
        self.last_entry = Entry(self)
        self.number_label = Label(self, text="House number:")
        self.number_entry = Entry(self)
        self.street_label = Label(self, text="Street:")
        self.street_entry = Entry(self)
        self.city_label = Label(self, text="City:")
        self.city_entry = Entry(self)
        self.state_label = Label(self, text="State:")
        self.state_entry = Entry(self)

        self.phone_label.grid(row=0, column=0)
        self.phone_entry.grid(row=0, column=1, columnspan=10)
        self.first_label.grid(row=1, column=0)
        self.first_entry.grid(row=1, column=1, columnspan=10)
        self.last_label.grid(row=2, column=0)
        self.last_entry.grid(row=2, column=1, columnspan=10)
        self.number_label.grid(row=3, column=0)
        self.number_entry.grid(row=3, column=1, columnspan=10)
        self.street_label.grid(row=4, column=0)
        self.street_entry.grid(row=4, column=1, columnspan=10)
        self.city_label.grid(row=5, column=0)
        self.city_entry.grid(row=5, column=1, columnspan=10)
        self.state_label.grid(row=6, column=0)
        self.state_entry.grid(row=6, column=1, columnspan=10)

        self.enter_but = Button(self, text="Enter", command=self.enter_text)
        self.enter_but.grid(row=7, column=3)

    def enter_text(self):
        # write the new member's data to json file
        JsonHandler.write_json(self.phone_entry.get(), self.first_entry.get(), self.last_entry.get(),
                               self.number_entry.get(), self.street_entry.get(), self.city_entry.get(),
                               self.state_entry.get())

        # upload json file to AWS S3
        if S3Handler.upload_file('data.txt', 'memberships', self.phone_entry.get() + '.txt'):
            print("Member added!")
        else:
            print("Error in adding member!")

        self.destroy()
        self.update()
