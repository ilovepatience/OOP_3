class Order:

    def __init__(self, items, total):
        self.items = items
        self.total = total

    def calculate_discount(self):
        return 0.1 if self.total > 100 else 0.05

    def apply_discount(self):
        discount = self.calculate_discount()
        self.total -= self.total * discount

    def process_order(self):
        self.apply_discount()
        self.print_order()

    def print_order(self):
        print(f"Order: {self.items}")
        print(f"Total after discount: {self.total}")


if __name__ == "__main__":
    order = Order(["Apple", "Banana", "Cherry"], 120)

    order.process_order()
