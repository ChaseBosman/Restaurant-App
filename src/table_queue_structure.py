from order_structure import OrderStructure


class TableQueueStructure:
    def __init__(self, table_num, order_num, items):
        self.table_num = table_num

        # active_orders holds a list of order objects, each order object holds a committed order
        self.active_orders = []
        self.active_orders_count = 0

        self.add_order(order_num, items)

    def add_order(self, order_num, items):
        # create a new order data structure
        new_order = OrderStructure(order_num, items)
        # insert it into the table's order queue
        self.active_orders.insert(len(self.active_orders), new_order)
        self.active_orders_count += 1
        print(self.active_orders_count)

    def get_table_num(self):
        return self.table_num



