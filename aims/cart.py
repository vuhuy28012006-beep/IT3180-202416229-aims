from aims.dvd import DigitalVideoDisc

MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def total_cost(self):
        return sum(dvd.cost for dvd in self.items)

    def print_cart(self):
        # Kiểm tra giỏ hàng có DVD hay không
        if not self.items:
            print("The cart is empty")
            return

        # Hiển thị danh sách DVD
        print("Cart contents:")

        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. Title: {dvd.title}, Cost: {dvd.cost:.2f} $")

        # Hiển thị tổng tiền
        print(f"Total cost: {self.total_cost():.2f} $")
    def sort_by_title(self):
        """Sort DVDs by title in ascending alphabetical order."""
        self.items.sort(key=lambda dvd: dvd.title.lower())

    def sort_by_cost(self):
        """Sort DVDs by cost in ascending order."""
        self.items.sort(key=lambda dvd: dvd.cost)