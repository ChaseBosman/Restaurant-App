import unittest
import client.phone_number_window
from tkinter import *


class TestPhoneNumberWindow(unittest.TestCase):
    def test_set_text(self):
        """
        Tests if the set text method works as needed for button entry for tables
        """
        root_window = Tk()
        phone = client.phone_number_window.PhoneNumberWindow(root_window)
        phone.set_text("H")
        phone.set_text("e")
        phone.set_text("l")
        phone.set_text("l")
        phone.set_text("o")
        self.assertEqual(phone.phone_entry.get(), "Hello")

    def test_del_text(self):
        """
        Tests if the delete method for the text window works properly
        """
        root_window = Tk()
        phone = client.phone_number_window.PhoneNumberWindow(root_window)
        phone.set_text("Hello")
        phone.del_text()
        phone.del_text()
        self.assertEqual(phone.phone_entry.get(), "Hel")


if __name__ == '__main__':
    unittest.main()
