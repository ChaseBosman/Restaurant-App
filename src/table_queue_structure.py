from order_structure import OrderStructure


class TableQueueStructure:
    def __init__(self, table_num, order_num, items):
        self.table_num = table_num

        # active_orders holds a list of order objects, each order object holds a committed order
        self.active_orders = []
        self.active_orders_count = 0

    def add_order(self, order_num, items):
        new_order = OrderStructure(order_num, items)
        self.active_orders[self.active_orders_count] = new_order
        self.active_orders_count += 1



