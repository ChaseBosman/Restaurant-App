import ticket
import sqlite3
from tkinter import *
from functools import partial


class Table:
    def __init__(self, table_number, ticket_num):
        self.table_num = table_number
        self.ticket = ticket.ticket(ticket_num)

    def get_table(self):
        return self.table_num

    def add_item(self):
        return 


    ##############################################
    #Loops until user has selected item and then adds it to ticket through add_item()
    ##############################################
    '''
    def display_items(self, family_sel):
        self.items_buts = []
        self.food_item_count = 0
        conn = sqlite3.connect('food.db')
        curs = conn.cursor()
        curs.execute("SELECT food.name FROM food, family where family.food_fam\
        =food.food_fam AND family.name = ?", (family_sel))
        rows = curs.fetchall()
        
        items_window = Tk()
        items_window.geometry("200x200")
        
        for rcount, row in enumerate(rows, start = 1):
            self.items_buts.append(Button(items_window, text=row,command=lambda row = row:self.add_item(row)))
            #queues item
            self.items_buts[self.food_item_count].grid(row = self.food_item_count + 1, column = 0)
            self.food_item_count += 1
            
            tbl_label = Label(items_window, text = "Chooose an item:")
        tbl_label.grid(row = 0, column = 0)
        quit_but = Button(items_window, text="Quit",command=items_window.destroy)
        quit_but.grid(row =  0, column = 1)

        items_window.mainloop()
        
        conn.commit()
        conn.close()


    ##############################################
    #Loops until user has selected food family (Entree, App, Etc) and then enters items menu through display_items(Wings, Pizza, Etc)
    ##############################################
    def display_families(self):
        self.family_buts = []
        self.food_family_count = 0
        conn = sqlite3.connect('food.db')
        curs = conn.cursor()
        curs.execute("SELECT family.name FROM family")
        rows = curs.fetchall()
         
        table_window = Tk()
        table_window.geometry("200x200")

        for rcount, row in enumerate(rows, start = 1):
            self.family_buts.append(Button(table_window, text=row,command=lambda row = row:self.display_items(row)))
            self.family_buts[self.food_family_count].grid(row = self.food_family_count + 1, column = 0)
            self.food_family_count += 1
                                  
        tbl_label = Label(table_window, text = "Chooose a food family:")
        tbl_label.grid(row = 0, column = 0)
        quit_but = Button(table_window, text="Quit",command=table_window.destroy)
        quit_but.grid(row =  1, column = 1)

        table_window.mainloop()
        conn.commit()
        conn.close()
        return
        '''
