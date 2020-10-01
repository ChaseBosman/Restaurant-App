class OrderStructure:
    def __init__(self, order_num, items):
        self.order_num = order_num

        # active_orders holds a list of order objects, each order object holds a committed order
        self.order_items = []
        self.order_items = items
        self.order_items_count = len(items)
        # count of items still being cooked on the line
        self.order_items_remaining = self.order_items_count

    def get_order_num(self):
        return self.order_num

    def decrease_items_remaining(self):
        self.order_items_remaining -= 1
        return self.order_items_remaining
